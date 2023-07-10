import os
import requests
import pandas as pd
import re
import subprocess
import time
import urllib.parse
from unidecode import unidecode

# List of required libraries
required_libraries = ['requests', 'pandas', 'unidecode']

# Check if all required libraries are installed
missing_libraries = []
for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        missing_libraries.append(library)

if missing_libraries:
    print("The following required libraries are missing:")
    for library in missing_libraries:
        print(library)
    print("Please install the missing libraries and try again.")
    exit(1)

# Get the directory where the script is stored
script_directory = os.path.dirname(os.path.abspath(__file__))

# Check if the previous directory file exists
previous_directory_file = os.path.join(script_directory, "previous_directory.txt")
if os.path.exists(previous_directory_file):
    with open(previous_directory_file, "r") as file:
        previous_directory = file.read().strip()
else:
    previous_directory = ""

# Ask the user for the directory where the creator folders will be created
creator_folders_directory = input(f"Enter the directory where the creator folders should be created (leave blank to use the previous directory: {previous_directory}): ")
creator_folders_directory = creator_folders_directory.strip()

# If no directory is provided, use the previous directory as the default
if not creator_folders_directory:
    creator_folders_directory = previous_directory

# Check if the provided directory exists
if not os.path.isdir(creator_folders_directory):
    print(f"The directory '{creator_folders_directory}' does not exist. Using the script directory instead.")
    creator_folders_directory = script_directory

# Save the current directory as the previous directory
with open(previous_directory_file, "w") as file:
    file.write(creator_folders_directory)

base_url = "https://civitai.com/api/v1/models"
creator_names = input("Enter the creator usernames (separated by commas): ").split(",")

for username in creator_names:
    username = username.strip()

    # Create a directory for the creator's files
    creator_folder_name = username.replace(" ", "_")
    creator_folder_path = os.path.join(creator_folders_directory, creator_folder_name)
    os.makedirs(creator_folder_path, exist_ok=True)

    # Check if the creator exists
    params = {
        "username": username,
        "page": 1
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(f"{base_url}?username={username}", headers=headers)

    if response.status_code != 200:
        print(f"The creator '{username}' does not exist. Skipping...")
        continue

    page_count = 0
    max_pages = 10
    model_info = []
    while params["page"] <= max_pages:
        response = requests.get(f"{base_url}?username={username}&page={params['page']}", headers=headers)

        if response.status_code == 200:
            data = response.json()

            if 'items' not in data or len(data['items']) == 0:
                print("No more results found.")
                break

            # Extract relevant information from the response data
            items = data['items']
            for item in items:
                name = item['name']
                item_type = item['type']
                description = item['description']
                latest_version = max(item['modelVersions'], key=lambda x: x['updatedAt'])
                trained_words = latest_version.get('trainedWords')
                files = latest_version.get('files', [])
                download_url = next((file['downloadUrl'] for file in files), None)

                if download_url:
                    # Remove special characters and foreign language characters from the folder name
                    model_folder_name = re.sub(r'[^\w\s-]', '', unidecode(name))
                    model_folder_path = os.path.join(creator_folder_path, model_folder_name)
                    os.makedirs(model_folder_path, exist_ok=True)

                    file_name = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(download_url).path))
                    file_path = os.path.join(model_folder_path, file_name)

                    if os.path.exists(file_path):
                        choice = input(f"The file '{file_name}' already exists in the directory. Do you want to overwrite it? (Y/N): ")
                        if choice.strip().lower() != 'y':
                            print(f"Skipping file '{file_name}'...")
                            continue

                    print(f"Downloading file for model: {name}")
                    try:
                        subprocess.run(["wget", download_url, "--content-disposition", "-P", model_folder_path, "--quiet", "--show-progress"], check=True)
                        print(f"Download completed for model: {name}")
                        time.sleep(5)  # Pause for 5 seconds

                        # Create a DataFrame with the model information
                        model_info.append({
                            'Name': name,
                            'Type': item_type,
                            'Description': description,
                            'Download URL': download_url,
                            'Trained Words': trained_words
                        })

                    except Exception as e:
                        print(f"Failed to download file for model: {name}")
                        print(f"Error: {e}")
                else:
                    print(f"No download URL found for model: {name}")

            params["page"] += 1
            page_count += 1

        else:
            print("Request failed with status code:", response.status_code)
            break

    # Create a master DataFrame from the model information
    master_df = pd.DataFrame(model_info)

    # Create the file path for the master CSV file in the creator's folder
    master_csv_file_name = f"{username}_master_model_information.csv"
    master_csv_file_path = os.path.join(creator_folder_path, master_csv_file_name)

    # Save the master DataFrame to a CSV file
    master_df.to_csv(master_csv_file_path, index=False)
    print(f"Master CSV file created successfully with {page_count} pages for creator: {username}")

    # Generate separate CSV files for each downloaded file
    for index, row in master_df.iterrows():
        name = row['Name']
        model_folder_name = re.sub(r'[^\w\s-]', '', unidecode(name))
        model_folder_path = os.path.join(creator_folder_path, model_folder_name)
        csv_file_name = f"{name.replace(':', '_')}_model_information.csv"
        csv_file_path = os.path.join(model_folder_path, csv_file_name)

        # Filter the master DataFrame for the current model
        model_data = master_df.loc[master_df['Name'] == name]

       # Saving downloaded files

        # Save the filtered DataFrame to a CSV file
        model_data.to_csv(csv_file_path, index=False)
        print(f"CSV file created successfully for model: {name}")

    print(f"Files and CSVs saved in separate folders based on the model names, within the creator folder: {username}")
    print(f"Master CSV file saved in the creator folder: {username}")

# Pause before closing the script
input("Press Enter to exit...")
