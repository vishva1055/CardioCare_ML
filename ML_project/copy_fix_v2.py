import shutil
import os
import sys

src = r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\8d8100d1-5be0-4581-83b7-06d28aac05a4\about_hero_medical_ai_1772544852188.png"
dst = r"c:\SEM-6\ML LAB\ML_project\static\img\about_hero.png"

def log_print(msg):
    print(msg)
    sys.stdout.flush()

try:
    log_print(f"Checking source: {src}")
    if os.path.exists(src):
        log_print("Source exists.")
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        log_print("Copy done.")
        if os.path.exists(dst):
            log_print(f"Success: {dst} exists.")
        else:
            log_print("Fail: Destination does not exist.")
    else:
        log_print("Source does not exist.")
except Exception as e:
    log_print(f"Exception: {str(e)}")
