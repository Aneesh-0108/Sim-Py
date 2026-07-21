
from pathlib import Path

def validate_and_scan(raw_path:str):

#Path-file system object

#expand-user and resolve to clean the path
    directory = Path(raw_path).expanduser().resolve()

    if not directory.exists():
        raise FileNotFoundError(f"The path {raw_path} doesnt exist")
    if not directory.is_dir():
        raise NotADirectoryError(f"The path {raw_path} is a file,not a diretory")
    
    #Iterates through th edirectory and checks for files
    #interdir() and .is_file()

    files_to_move = [item for item in directory.interdir() if item.is_file()]

    return directory,files_to_move
