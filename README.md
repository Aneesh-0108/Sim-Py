# Sim-Py

**Sim-Py** is a collection of Python projects built to  focus on  different areas of Python

---

## Repository Structure

```
Sim-Py/
│
├── expensetracker/    # CLI Expense Tracker
└── multisorter/       # Multithreaded File Organizer
```

---

# 1. Expense Tracker

A command-line application for managing personal expenses with persistent JSON storage.

## Features

- Add expenses
- View all expenses
- Search expenses
- Filter by category
- Delete expenses
- Calculate total expenses
- Persistent JSON storage

## Concepts Covered

- Functions and modular programming
- File handling
- JSON serialization
- CRUD operations
- Exception handling
- CLI application development

## Tech Stack

- Python
- JSON

## Run

```bash
cd expensetracker
python main.py
```

---
2. MultiSorter
A multithreaded command-line utility that organizes files into category folders based on their file extensions.

Example:

Plaintext


Downloads/

resume.pdf
photo.jpg
song.mp3
movie.mp4
↓

Plaintext


Downloads/

Documents/
Images/
Audio/
Videos/
Features
Scan any directory safely skipping subdirectories

Categorize files by extension

Automatically create destination category folders

Move files concurrently using multithreaded worker pools

Handle duplicate filenames safely

Packaged as an installable, global CLI tool (multisorter)

Concepts Covered
File system traversal (pathlib, os)

File operations (shutil)

Concurrency (concurrent.futures.ThreadPoolExecutor)

Package architecture & relative imports (smart_organizer)

Modern Python packaging (pyproject.toml with setuptools)

Executable entry points (project.scripts)

Shell PATH configuration (~/.local/bin)

Installation & Setup
Navigate to the project root:

Bash


cd multisorter
Install in editable mode:

Bash


pip install -e . --break-system-packages
(Optional) Ensure ~/.local/bin is in your shell PATH:

Bash


echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
Usage
Once installed, you can execute multisorter from any directory in your system:

Bash


# Organize a specific directory
multisorter ~/Downloads

# Specify custom worker thread count (default: 4)
multisorter ~/Downloads -w 8

# Organize the current directory
multisorter .
```

---
