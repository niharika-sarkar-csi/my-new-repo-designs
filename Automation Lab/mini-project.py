import os
import shutil
import pandas as pd
import pyautogui
import smtplib
from email.message import EmailMessage
from datetime import datetime
import time


# ------------------------
# 1. Detect New Files
# ------------------------
DESIGNS_DIR = "Designs"
ARCHIVE_DIR = "Archive"

today = datetime.today().strftime("%Y-%m-%d")
archive_today = os.path.join(ARCHIVE_DIR, today)

# Create folder Archive/YYYY-MM-DD
os.makedirs(archive_today, exist_ok=True)

files = os.listdir(DESIGNS_DIR)
new_files = []

for file in files:
    filepath = os.path.join(DESIGNS_DIR, file)
    if os.path.isfile(filepath):
        new_files.append(filepath)

if not new_files:
    print("No new files found.")
    exit()


# ------------------------
# 2. Move files to archive
# ------------------------
moved_files = []

for f in new_files:
    shutil.move(f, archive_today)
    moved_files.append(os.path.basename(f))


# ------------------------
# 3. Create CSV report
# ------------------------
summary_data = []

for file in moved_files:
    full_path = os.path.join(archive_today, file)
    size = os.path.getsize(full_path)
    modified = datetime.fromtimestamp(os.path.getmtime(full_path))

    summary_data.append({
        "filename": file,
        "size_bytes": size,
        "modified_date": modified
    })

df = pd.DataFrame(summary_data)

summary_filename = f"summary_{today}.csv"
df.to_csv(summary_filename, index=False)

print(f"Summary saved: {summary_filename}")


# ------------------------
# 4. Take screenshot of folder
# ------------------------
time.sleep(2)
pyautogui.screenshot("summary_folder.png")
print("📸 Screenshot captured!")


# ------------------------
# 5. Send Email Notification
# ------------------------
def send_email():
    msg = EmailMessage()
    msg["Subject"] = f"Daily Design Files Report – {today}"
    msg["From"] = "niharikaofficial.2023@gmail.com"
    msg["To"] = "niharika.sarkar@cloudspikes.ca"

    msg.set_content(
        f"""
Hello,

Your daily design automation report is ready.

New files moved: {len(moved_files)}
Archive folder: Archive/{today}
Summary CSV: {summary_filename}

Regards,
Automation Bot
"""
    )

    # Attach CSV file
    with open(summary_filename, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="csv",
            filename=summary_filename
        )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("niharika.sarkar@cloudspikes.ca", "000999@@Niharika")
        server.send_message(msg)

    print("📧 Email notification sent!")


send_email()
import schedule
import time
import subprocess

def job():
    subprocess.run(["python", "bot.py"])

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
