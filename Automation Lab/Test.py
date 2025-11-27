import os
import shutil
from datetime import datetime

DESIGNS_DIR = "Designs"
ARCHIVE_DIR = "Archive"

# Create folder Archive/YYYY-MM-DD
today = datetime.today().strftime("%Y-%m-%d")
archive_today = os.path.join(ARCHIVE_DIR, today)
os.makedirs(archive_today, exist_ok=True)

# Read all files from Designs
files = os.listdir(DESIGNS_DIR)

png_files = []

# Filter only PNG files
for file in files:
    if file.lower().endswith(".png"):   # ONLY PNG
        filepath = os.path.join(DESIGNS_DIR, file)
        if os.path.isfile(filepath):
            png_files.append(filepath)

if not png_files:
    print("No new PNG files found.")
    exit()

# Move PNG files to archive
for f in png_files:
    shutil.move(f, archive_today)
    print(f"Moved: {os.path.basename(f)}")

print("\n✔ All PNG files moved successfully!")
