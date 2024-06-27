#-------------------------------------------------------------------------------
# Name:        replaceWithUnderscoresFiles
# Purpose:     To replace hyphens and spaces with underscores in a string.
#
# Author:      dylan
#
# Created:     21/05/2024
#
# Pathnames Used:
# target_folders = ["C:/Users/dylan/OneDrive/Pictures/GIFS"]
# target_folders = ["C:/Users/dylan/OneDrive/Pictures/Memes/Videos"]
# target_folders = ["C:/Users/dylan/OneDrive/Pictures/Memes/Pictures"]
# target_folders = ["F:/Clips/Audio/Songs"]
#-------------------------------------------------------------------------------
import os

def replaceWithUnderscores(input_string):
    return input_string.replace('-', '_').replace(' ', '_').lower()

def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            new_filename = replaceWithUnderscores(filename)
            if new_filename != filename:
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
                print(f"Renamed {filename} to {new_filename}")

target_folders = ["F:/Clips/Audio/Songs"]

for folder in target_folders:
    if os.path.isdir(folder):
        print(f"Folder edited: {folder}")
        process_files_in_folder(folder)
    else:
        print(f"Folder '{folder}' not found.")

print("Finished.")