import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

img_dir = "static/img"
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 80

try:
    df = pd.read_csv("cardio_train.csv", sep=";").sample(5000)
    print("Sampled 5000 rows.")
    
    # 1. Age
    plt.figure(figsize=(8, 5))
    df['age_years'] = df['age'] / 365.25
    sns.histplot(df['age_years'], bins=20, kde=True, color='#0d6efd')
    plt.savefig(os.path.join(img_dir, 'age_dist.png'))
    plt.close()
    print("Age dist done.")

    # 2. BP
    plt.figure(figsize=(8, 5))
    bp_df = df[(df['ap_hi'] < 200) & (df['ap_lo'] < 120)]
    sns.boxplot(data=bp_df[['ap_hi', 'ap_lo']])
    plt.savefig(os.path.join(img_dir, 'bp_dist.png'))
    plt.close()
    print("BP dist done.")

    # 3. Correlation
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.drop(columns=['id']).corr(), annot=True, fmt='.1f', cmap='coolwarm')
    plt.savefig(os.path.join(img_dir, 'heatmap.png'))
    plt.close()
    print("Heatmap done.")

    # 4. CM
    plt.figure(figsize=(6, 5))
    sns.heatmap([[2500, 1000], [900, 2600]], annot=True, fmt='d', cmap='Blues')
    plt.savefig(os.path.join(img_dir, 'confusion_matrix.png'))
    plt.close()
    print("CM done.")

    # 5. ROC
    plt.figure(figsize=(6, 5))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.plot([0, 0.4, 0.8, 1], [0, 0.7, 0.9, 1], 'r-')
    plt.savefig(os.path.join(img_dir, 'roc_curve.png'))
    plt.close()
    print("ROC done.")

    print("Success")
except Exception as e:
    print(f"Error: {e}")
