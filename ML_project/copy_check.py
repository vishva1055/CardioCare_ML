import shutil
import os

src = r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\8d8100d1-5be0-4581-83b7-06d28aac05a4\about_hero_medical_ai_1772544852188.png"
dst = r"c:\SEM-6\ML LAB\ML_project\static\img\about_hero.png"

with open("copy_check.txt", "w") as f:
    f.write(f"Source: {src}\n")
    if os.path.exists(src):
        f.write("Source exists.\n")
        try:
            shutil.copy2(src, dst)
            f.write("Copy executed.\n")
            if os.path.exists(dst):
                f.write(f"Success: Destination exists. Size: {os.path.getsize(dst)}\n")
            else:
                f.write("Failure: Destination missing after copy.\n")
        except Exception as e:
            f.write(f"Exception: {str(e)}\n")
    else:
        f.write("Error: Source does not exist.\n")
