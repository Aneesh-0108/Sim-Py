#Managing multiple files across multiple threads

#concurrent.futures containsd ThreadPoolExecutor and ProcessPoolExecutor
 #Future objects


from concurrent.futures import ThreadPoolExecutor,as_completed
from pathlib import Path
from smart_organizer.organizer import move_file

#a list of files to be moved to destimation:base_dir with max files being shared 4 at a time
def organize_files_in_parallel(files_to_move: list[Path], base_dir:Path,max_workers=4):
    results=[]
    
    #create a pool of threads
    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        future_to_file = {
            executor.submit(move_file,file_path,base_dir):file_path
            for file_path in files_to_move
        }

        for future in as_completed(future_to_file):
            file_path = future_to_file[future]  
            
            try:
                destination = future.result()
                results.append((file_path,destination,True,None))
            except Exception as exc:
                results.append((file_path,None,False,str(exc)))
    return results            

