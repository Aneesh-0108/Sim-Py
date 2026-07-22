import os
#for automated file and directory management
import shutil

from smart_organizer.config import LOOKUP_MAP
from pathlib import Path

#we need to focus on the problm of files having same name ,like naming like report(1),(2).pdf to solve itor else the contents will be overwritten by another file of same name

#report.pdf,report-stem,suffix-.pdf

#expected datatype is path and return type is path
def get_unique_destination(target_folder:Path,file_path:Path) -> Path:
    
    destination = target_folder/file_path.name
    stem = file_path.stem
    suffix = file_path.suffix

    counter = 1

    while destination.exists():
        new_filename = f"{stem}({counter}){suffix}"
        destination = target_folder/file_path.name
        counter+=1
        
    return destination
#Path is expected datatype and path is the return object
def move_file(file_path:Path,base_dir) -> Path:
    category = LOOKUP_MAP.get(file_path.suffix.lower(), 'Others')

    target_folder = base_dir/category

    target_folder.mkdir(parents=True,exist_ok=True)

    destination = get_unique_destination(target_folder,file_path)

#shutil requires string object
    shutil.move(str(file_path), str(destination))
 
    return destination





