import os
import requests
import pandas as pd
import re
import subprocess
import time
import urllib.parse

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

url = "https://civitai.com/api/v1/models"

# Get user input for the creator username
creator_username = input("Enter the creator username: ")

# Create a directory for the creator's files
folder_name = creator_username.replace(" ", "_")
folder_path = os.path.join(script_directory, folder_name)
os.makedirs(folder_path, exist_ok=True)

# Check if the creator exists
params = {
    "username": creator_username,
    "page": 1
}
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code != 200:
    print(f"That creator does not exist. Please try again.")
    exit()

model_info = []

page_count = 0
while params["page"] <= 10:
    response = requests.get(url, params=params, headers=headers)

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
            if description is not None:
                description = re.sub('<.*?>', '', description)  # Remove HTML tags
                description = re.sub(r'\s+', ' ', description)  # Remove extra whitespace
            latest_version = max(item['modelVersions'], key=lambda x: x['updatedAt'])
            trained_words = latest_version.get('trainedWords')
            files = latest_version.get('files', [])
            download_url = next((file['downloadUrl'] for file in files), None)
            if download_url:
                model_version_id = re.search(r'models/(\d+)', download_url)
                if model_version_id:
                    model_version_id = model_version_id.group(1)
                    file_name = f"{name}_{model_version_id}.pt"  # Customize the file name as desired
                    file_name_encoded = urllib.parse.quote(file_name)  # Encode the file name
                    file_path = os.path.join(folder_path, file_name_encoded)
                    print(f"Downloading file: {file_name}")
                    try:
                        subprocess.run(["wget", download_url, "--content-disposition", "-O", file_path], check=True)
                        print(f"Download completed for file: {file_name}")
                        time.sleep(5)  # Pause for 5 seconds
                    except Exception as e:
                        print(f"Failed to download file: {file_name}")
                        print(f"Error: {e}")
                else:
                    print(f"Failed to extract model version ID from download URL: {download_url}")
            else:
                print(f"No download URL found for file: {name}")

            model_info.append({
                'Name': name,
                'Type': item_type,
                'Description': description,
                'Download URL': download_url,
                'Trained Words': trained_words
            })

        params["page"] += 1
        page_count += 1

    else:
        print("Request failed with status code:", response.status_code)
        break

# Create a DataFrame from the model information
df = pd.DataFrame(model_info)

# Create the file path for the CSV file in the creator's directory
csv_file_name = f"{creator_username}_model_information.csv"
csv_file_path = os.path.join(folder_path, csv_file_name)

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)
print(f"CSV file created successfully with {page_count} pages.")
print(f"Files and CSV saved in the '{folder_name}' folder")

# Pause before closing the script
input("Press Enter to exit...")
