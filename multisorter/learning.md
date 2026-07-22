pathlib — Object-oriented filesystem paths

while building packages,the program msut be structured properly


1. When to use a List Comprehension [...]
Use a list comprehension when your final goal is to produce a flat sequence (a list) of items.

clean_files = []

for file in raw_files:
    clean_files.append(file.upper())

Instead,
clean_files = [file.upper() for file in raw_files] 

2.When to use Dictionary Comprehension

Use a dictionary comprehension when your final goal is to produce Key-Value pairs for lightning-fast lookups, indexing, or grouping.

Normal_Way :

user_roles = {"Admin":"Name","Guest":"John"}
name_to_role = {}
for role,name in user_roles.items:
    name_to_rule[name] = role

name_to_role = {name:role for role,name in user_roles.items()}    

config.py doesn't automatically scan anything on its own—it only moves when you explicitly tell it to iterate over the data structure.

If you just loop over EXTENSION_MAP, Python will only look at the keys ("Images", "Documents"). It completely ignores the extensions side!

To force Python to look at both sides at the same time, you use .items()


[ STEP 1: PHYSICAL SCAN ]
  pathlib.iterdir() looks inside your physical ~/Downloads folder.
  It discovers a real file named "resume.pdf".
       │
       ▼
[ STEP 2: EXTRACT STRING ]
  Your code chops off the end of the filename to get the string ".pdf".
       │
       ▼
[ STEP 3: TEXT LOOKUP ]
  Your code takes that text string ".pdf" and asks config.py's LOOKUP_MAP:
  "Hey, where does this text string go?"
  LOOKUP_MAP looks at its pre-sorted dictionary and answers: "Documents".
       │
       ▼
[ STEP 4: PHYSICAL MOVE ]
  shutil.move() physically relocates the real file into the "Documents" folder.


  organizer.py needs a cleaned base  directory  so it can create new sub directories
  it needs the directoty and list of files



  while destination.exists():
    new_filename = {stem}({counter}){suffix}
    destination =  target_folder/file_path.name
    counter+=1

this is for the files with same name  iteration:
# Guess 2 inside loop: Downloads/Documents/report(1).pdf
# Guess 3 inside loop: Downloads/Documents/report(2).pdf 

parents=True: Creates any missing parent folders in the path automatically (prevents FileNotFoundError).

exist_ok=True: Prevents a crash if the folder already exists (prevents FileExistsError).



#for creating packages build system and project are required

#this is project metadata
[project]
name = "multisorter"
version = "0.1.0"
description= "A ultithreaded CLI file organizer written in Python"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

only key="value pairs in toml files





     