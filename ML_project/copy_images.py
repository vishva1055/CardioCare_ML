import shutil
import os

files = {
    r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\714c786f-ddab-4e56-bf9f-e3b3af407e2c\age_distribution_chart_1772523787529.png": "age_dist.png",
    r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\714c786f-ddab-4e56-bf9f-e3b3af407e2c\bp_distribution_chart_1772523803209.png": "bp_dist.png",
    r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\714c786f-ddab-4e56-bf9f-e3b3af407e2c\correlation_heatmap_1772523828657.png": "heatmap.png",
    r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\714c786f-ddab-4e56-bf9f-e3b3af407e2c\confusion_matrix_chart_1772523911449.png": "confusion_matrix.png",
    r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\714c786f-ddab-4e56-bf9f-e3b3af407e2c\roc_curve_chart_1772523932122.png": "roc_curve.png",
    r"C:\Users\Deep Gojariya\.gemini\antigravity\brain\8d8100d1-5be0-4581-83b7-06d28aac05a4\about_hero_medical_ai_1772544852188.png": "about_hero.png"
}

dest_dir = r"c:\SEM-6\ML LAB\ML_project\static\img"
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for src, name in files.items():
    dest = os.path.join(dest_dir, name)
    print(f"Copying {src} to {dest}...")
    shutil.copy(src, dest)

print("All files copied successfully.")
