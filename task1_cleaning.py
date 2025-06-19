import pandas as pd
import numpy as np

# Step 1: Load dataset
df = pd.read_csv("food_coded.csv", encoding='ISO-8859-1')

# Step 2: Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 3: Check missing values
print("Missing values:\n", df.isnull().sum())

# Step 4: Fill missing values
for col in ['calories_day', 'type_sports', 'weight']:
    if col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

# Step 5: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 6: Remove duplicate columns
df = df.loc[:, ~df.columns.duplicated()]

# Step 7: Save cleaned file
df.to_csv("cleaned_food_data.csv", index=False)

print("✅ Data cleaning done successfully!")
