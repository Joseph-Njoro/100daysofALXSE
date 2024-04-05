def isalphabetical(char:
    ""Check if a character is an alphabetical character (A-Z or a-z)"""
    return char.isalpha()

def renam_files(files):
    ""Rename files in a directory to start with alphabetical characters,
    deleting any non-alphabetic characters. Replace spaces with underscores.
    """
    renamed_files = []
    for file in files:
        # Get the filename and extension
        name, ext = os.path.splitext(file)
        
        # Replace spaces with underscores and remove non-alphabetic characters in the filename
        new_name = ''.join(char if char.isalpha() or char.isspace() else '_' for char in name)
        
        # Remove leading/trailing underscores and consecutive underscores
        new_name = '_'.join(filter(None, new_name.split('_')))
        
        # If the new name is empty, delete the file
        if not new_name:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error deleting {file}: {e}")
            continue
        
        # If the new name is the same as an existing file, skip this file
        if new_name in renamed_files:
            try:
                os.remove(file)
            except Exception as e:
                print(f"Error deleting {file}: {e}")
            continue
        
        # Rename the file
        new_file = os.path.join(os.path.dirname(file), new_name + ext)
        try:
            os.rename(file, new_file)
            renamed_files.append(new_name)
        except Exception as e:
            print(f"Error renaming {file}: {e}")

if __name__ == "__main__":
    # Get a list of all files in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    
    # Rename the files
    rename_files(files)