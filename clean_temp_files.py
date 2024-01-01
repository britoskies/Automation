import os, tempfile

def delete_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        for file in files:
            filepath = os.path.join(directory, file)
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                    print(f"Deleted: {filepath}")
                elif os.path.isdir(filepath):
                    delete_files_in_directory(filepath)
            except Exception as e:
                print(f"Error deleting {filepath}: {e}")
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")

def clean_temporary_files():
    temp_dir = tempfile.gettempdir()
    print(f"Cleaning temporary files in {temp_dir}")
    delete_files_in_directory(temp_dir)

clean_temporary_files()