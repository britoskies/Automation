import os, shutil
from datetime import datetime

# Get the files from the downloads folder
# Send them to their respective folder depending on their extension

####################################################################

# Util functions
def get_download_path():
    home_directory = os.path.expanduser('~')
    return os.path.join(home_directory, 'Downloads')

def get_listdir(directory_path):
    try:
        return os.listdir(directory_path)
    except OSError:
        print(f"Failed to access directory: {directory_path}")
        return []
    
def right(text, separator):
    charindex = text.rfind(separator)
    if charindex != -1: 
        return text[charindex+1:]
    else:
        return ""

def left(text, separator):
    charindex = text.rfind(separator)
    if charindex != -1: 
        return text[:charindex]
    else:
        return ""
    
def check_folder_exists(foldername, dir):
    folders_in_dir = get_listdir(dir)
    return foldername in folders_in_dir

# None functions
def create_new_folder(dir, foldername):
    try:
        folderdir = str(f"{dir}\\{foldername}")
        os.mkdir(folderdir)
    except FileExistsError:
        print("Error! This file already exists inside this folder")

def remove_file(filepath):
    try:
        os.remove(filepath)
    except OSError as e:
        print(f"Error: {e}")

def move_file(source_dir, destination_dir, file):
    file_exists = check_folder_exists(file, destination_dir.replace(file, ""))
    if file_exists:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_file_name = f'{left(file, ".")} - {timestamp}.{right(file, ".")}'
        new_destination = f'{destination_dir.replace(file, "")}{new_file_name}'
        shutil.copyfile(source_dir, new_destination)
        remove_file(source_dir)
    else:
        shutil.move(source_dir, destination_dir)

##################### Globals #####################

download_path = get_download_path()
files_in_downloads_dir = get_listdir(download_path)

##################### Program flow #####################
for file in files_in_downloads_dir:
    filename = left(file, ".")
    file_extension = right(file, ".")
    file_path = str(f"{download_path}\\{file}")
    file_destination = str(f"{download_path}\\{file_extension}\\{file}")
    folder_exists = False

    if file_extension and file_extension != "ini":
        folder_exists = check_folder_exists(file_extension, download_path)  
    else:
        continue

    if folder_exists:
        move_file(file_path, file_destination, file)
    else:
        create_new_folder(download_path, file_extension)
        move_file(file_path, file_destination, file)