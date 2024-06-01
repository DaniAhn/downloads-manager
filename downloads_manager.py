import os
import shutil
import sys
from send2trash import send2trash

# Dictionary mapping folder names to a list of corresponding file extensions
FOLDERS = {
    'Documents': ['.txt', '.pdf', '.docx', '.odt', '.rtf', '.epub', '.pptx'],
    'Photos': ['.jpg', '.png', '.webp', '.gif', '.jpeg', '.bmp', '.svg'],
    'Videos': ['.mp4', '.webm', '.wmv', '.mkv', '.mov', '.mpeg', '.mpg'],
    'Audio': ['.mp3', '.wav', '.m4a', '.wma', '.ogg', '.mid', '.midi'],
    'Executables': ['.bat', '.bin', '.exe', '.msi', '.sh', '.wsf'],
    'Compressed': ['.7z', '.zip', '.rar', '.arj', '.pkg'],
    'Other':[]
}

CRIT_FILES = ['.parts', '.ini', '.cfg', '.json']

def main() -> None: 
    """
    Main entry point of the program.
    """
    # Creates Downloads path
    downloads_path = get_downloads_path()

    check_org_folders(downloads_path)
    organize_files(downloads_path)

    # Creates a list of command line arguments
    arg_list = sys.argv[1:]
    # Checks whether 'sort' or 'clear' options are selected
    if arg_list[0] == 'sort':
        organize_files(downloads_path)
    elif arg_list[0] == 'clear':
        # Checks if the second argument is a valid option
        if arg_list[1] in FOLDERS.keys() or arg_list[1] == 'All':
            confirm_clear(downloads_path, arg_list[1])

def confirm_clear(downloads_path: str, option: str) -> None:
    """
    Provides the user a prompt to confirm their selected option.

    Args:
        downloads_path (str): The path to the Downloads folder.
        option (str): The selected option to clear.
    """
    while True:
        choice = input(f'Are you sure you want to clear {option}? (y/n): ')
        if choice == 'y':
            clear_directory(downloads_path, option)
            break
        elif choice == 'n':
            break
        else:
            print('Invalid choice. Please enter (y/n).')


def get_downloads_path() -> str:
    """
    Returns the file path to the Downloads folder.
    """
    if os.name == 'nt': # if OS is Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    else: # if OS is Unix-like OS (Linux, MacOS)
        return os.path.join(os.environ['HOME'], 'Downloads')
    
def check_org_folders(downloads_path: str) -> None:
    """
    Checks if the Downloads folder contains each folder in the FOLDERS dictionary.
    If a folder is not found, it is created.

    Args:
        downloads_path (str): The path to the Downloads folder.
    """
    for folder in FOLDERS.keys():
        # Creates folder path
        folder_path = os.path.join(downloads_path, folder)
        # Creates folder if not found in Downloads
        if not os.path.isdir(folder_path):
            print(f'{folder} not found; creating {folder}')
            os.makedirs(folder_path, exist_ok=True)

def organize_files(downloads_path: str) -> None:
    """
    Organizes files into their respective folders based on file extension.

    Args:
        downloads_path (str): The path to the Downloads folder.
    """
    # Inspects each file in Downloads
    for file in os.listdir(downloads_path):
        # Creates variables to store file path, filename and file extension
        file_path = os.path.join(downloads_path, file)
        filename, file_ext = os.path.splitext(file)

        # Ignores if file is a directory
        if os.path.isdir(file_path):
            continue
        
        # Ignores if file extension is in CRIT_FILES
        if file_ext in CRIT_FILES:
            continue

        is_sorted = False
        print(file)

        # Inspects each folder if it contains a matching file extension
        for folder in FOLDERS.keys():
            # Terminates the loop if a match is found
            if is_sorted:
                break

            for ext in FOLDERS[folder]:
                if file_ext == ext:
                    # Moves file to corresponding folder
                    folder_path = os.path.join(downloads_path, folder)
                    print(f'Moving {file} to {folder_path}')
                    shutil.move(file_path, folder_path)
                    is_sorted = True
                    break
        # If no match is found, file is moved to "Other"
        if is_sorted == False:
            folder_path = os.path.join(downloads_path, 'Other')
            print(f'Moving {file} to {folder_path}')
            shutil.move(file_path, folder_path)

        print('\n')

def clear_directory(downloads_path: str, option:str) -> None:
    """
    Clears every file in the specified directory.
    If 'All' is selected, clears every file in each organized folder in Downloads.

    Args:
        downloads_path (str): The path to the Downloads folder.
        option (str): The selected option to clear.
    """
    if option == 'All':
        folder_path = downloads_path
        for folder in FOLDERS.keys():
            print(f'Clearing {folder}...')
            folder_path = os.path.join(downloads_path, folder)
            clear_files(folder_path)
    else:
        print(f'Clearing {option}...')
        folder_path = os.path.join(downloads_path, option)
        clear_files(folder_path)

    print('Cleared!')

def clear_files(folder_path: str) -> None:
    """
    Moves every file in the specified directory to the Recycle Bin.

    Args: 
        folder_path (str): The path to the specified directory.
    """
    for file in os.listdir(folder_path):
        filename, file_ext = os.path.splitext(file)
        # Ignores if file extension is in CRIT_FILES
        if file_ext in CRIT_FILES:
            continue
        file_path = os.path.join(folder_path, file)
        print(f'Cleared {file}')
        send2trash(file_path)

if __name__ == '__main__':
    main()