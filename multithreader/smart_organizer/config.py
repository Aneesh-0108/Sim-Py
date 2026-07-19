from pathlib import Path


EXTENSION_MAP = {
    "Images": [".jpg",".jpeg",".png",".gif",".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Video": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".json"]
}

#DIctionary Comprehension:
#Image is an category and jpg is a extension
#hereat first we look for a extension then matchup with a category thats why extension:category,then we look inside extensions
LOOKUP_MAP = {ext:category for category,extension in EXTENSION_MAP.items() for ext in EXTENSION_MAP.items()}

