import shutil
import os

src = r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\8d8100d1-5be0-4581-83b7-06d28aac05a4\about_hero_medical_ai_1772544852188.png"
dst = r"c:\SEM-6\ML LAB\ML_project\static\img\about_hero.png"

try:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(src, dst)
    print(f"Successfully copied image to {dst}")
except Exception as e:
    print(f"Error: {e}")
