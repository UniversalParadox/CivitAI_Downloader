# CivitAI_Downloader
Small project that I made for a friend to easily download CivitAI models from one creator.

Requirements
Python
Pandas for Python



What does this do?

This project uses the CivitAI REST API to find, extract, and download all files created by a specific user.
To be more specific, this files does the following.

User inputs the creator's username.
Script then searches for the user in CivitAI and will confirm/deny if the user exists.
If the user does not exist, it will ask for you to try again.
If the user does exist, it will then use the civitAI API to query and then extract information to push to a CSV file.
Once the information is extracted and parsed, it will find download URL for the files and begin to download them.
In order to make sure all downloads are done without isssue, there is a baked in 3 second wait period between downloads.

Below is the information stored into the CSV file.

Name

Type of File

Description

API download link

Trigger Words (if LORA file)




Files within this repository

.wget-hsts - Protection with using wget

COPYING.txt - GNU3 License Copy

LICENSE - GNU3 License

README.md - This file

Run.bat - Simple windows batch file to run the script.

civitai.py - Script itself

wget.ext - https://www.gnu.org/software/wget/
