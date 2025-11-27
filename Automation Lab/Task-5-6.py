import shutil
import datetime
from pathlib import Path

# Correct base folder
path = Path(r"C:\Python Automation\Automation Lab")

# Ensure subfolders exist
(path / "Images").mkdir(exist_ok=True)
(path / "Docs").mkdir(exist_ok=True)

# Loop through files in the folder
for file in path.iterdir():
    if file.is_file():  # Skip folders

        # Move Images
        if file.suffix.lower() in [".png", ".jpg", ".jpeg"]:
            shutil.move(str(file), str(path / "Images" / file.name))

        # Move PDFs
        elif file.suffix.lower() == ".pdf":
            shutil.move(str(file), str(path / "Docs" / file.name))

print("✅ Files organized at", datetime.datetime.now())



