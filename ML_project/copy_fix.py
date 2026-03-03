import shutil
import os

src = r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\8d8100d1-5be0-4581-83b7-06d28aac05a4\about_hero_medical_ai_1772544852188.png"
dst = r"c:\SEM-6\ML LAB\ML_project\static\img\about_hero.png"
log_path = r"c:\SEM-6\ML LAB\ML_project\copy_log.txt"

def log(msg):
    with open(log_path, "a") as f:
        f.write(msg + "\n")
    print(msg)

if os.path.exists(log_path):
    os.remove(log_path)

log(f"Starting copy from {src} to {dst}")
try:
    if os.path.exists(src):
        log(f"Source file found (size: {os.path.getsize(src)})")
        # Ensure directory exists
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        log(f"Copy operation completed")
        if os.path.exists(dst):
            log(f"VERIFIED: File exists at {dst} (size: {os.path.getsize(dst)})")
        else:
            log(f"ERROR: File missing at {dst} after copy attempt")
    else:
        log(f"ERROR: Source file NOT FOUND at {src}")
except Exception as e:
    log(f"EXCEPTION: {str(e)}")
