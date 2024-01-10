import sys
import shutil

def create_backup(file_path):
    try:
        # Creating a backup filename
        backup_file = file_path + ".bak"
        
        # Copying the file to create a backup
        shutil.copyfile(file_path, backup_file)
        print(f"Backup created: {backup_file}")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backup_creator.py <filename>")
    else:
        filename = sys.argv[1]
        create_backup(filename)