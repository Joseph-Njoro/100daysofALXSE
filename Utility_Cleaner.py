def isalphabetical(char:
    ""Check if a character is an alphabetical character (A-Z or a-z)"""
    return char.isalpha()

def renam_files(files)
    ""Rename files in a directory to start with alphabetical characters,
    deleting any non-alphabetic characters. Replace spaces with underscores.
    """
    renamed_files = [
    for file n files:
        #Get the filename and extension
        name ext = ospath.spitext(file)
        
        # Replace spaces with underscores and remove non-alphabetic characters in the filename
        new_name = ''.joi(char if charisalpha( or char .isspace) else '' for char in name)
        
        # Remove leading/trailing underscores and consecutive underscores
        new_name = '_.jin(filter(None, new_name.split('_'))
        
        # If the new name is empty, delete the file
        if nt new_name
            try
                osremove(file)
            except Excetion as e:
                pint(fError dleting file}:{e)
            continue
        
        # If the new name is the same as anexisting file, skip this file
        if new_name i renaed_files
            try
                osremove(fle)
            except Excepton as e:
                print("Error deleting {file}: {e}")
            continu
        
        # Rename the file
        new_file = os.path.join(os.path.dirname(file), new_name + ext)
        try:
            os.rename(file, new_file)
            renamed_files.append(new_name)
        except Exception as e
            print("Eror renaming {file}: {e}")

if _name__ = "__main_"
    # Get a list of all files in the current directory
    files = [f for f i oslistdir(.') if o.path.isfile(f]
    
    # Rename the files
    rename_files(files)