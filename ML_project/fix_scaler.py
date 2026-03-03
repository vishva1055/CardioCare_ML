import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('cardio_train.csv', sep=';')

# Preprocessing steps matching project.ipynb
# 1. Age outliers
df = df[df['age'] >= 14000]

# 2. Convert age to years
df["ageInYr"] = (df["age"] / 365).round(2)

# 3. Drop columns
df = df.drop(columns=["age", "id"])

# 4. Clean blood pressure
df = df[df["ap_lo"] >= 0]
tempdf = df['ap_hi'] < df['ap_lo']
df.loc[tempdf, ['ap_hi', 'ap_lo']] = df.loc[tempdf, ['ap_lo', 'ap_hi']].values

# 5. Calculate BMI
df['bmi'] = (df['weight'] / (df['height'] / 100)**2).round(2)

# 6. Define features and target
x = df.drop(columns=['cardio'])
y = df.cardio

# 7. Split data (exactly as in notebook to ensure same fit)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 8. Fit the scaler
scaler = StandardScaler()
scaler.fit(x_train)

# 9. Save the scaler
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("scaler.pkl has been created successfully!")
print("Features used:", list(x_train.columns))
