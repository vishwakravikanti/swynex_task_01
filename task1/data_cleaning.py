# ============================================
# TITANIC DATASET CLEANING PROJECT
# ============================================

import pandas as pd
import seaborn as sns
import os

# STEP 1: Load the dataset directly from Seaborn

print("=" * 50)
print("TITANIC DATA CLEANING PROJECT")
print("=" * 50)

df = sns.load_dataset("titanic")

print("\nDataset loaded successfully!")

# STEP 2: Explore the dataset

print("\nOriginal Dataset Shape:")
print(df.shape)

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

# STEP 3: Check missing values

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# STEP 4: Create a copy

df_cleaned = df.copy()

# STEP 5: Handle missing numerical values

df_cleaned["age"] = df_cleaned["age"].fillna(
    df_cleaned["age"].median()
)

df_cleaned["fare"] = df_cleaned["fare"].fillna(
    df_cleaned["fare"].median()
)

# STEP 6: Handle missing categorical values

df_cleaned["embarked"] = df_cleaned["embarked"].fillna(
    df_cleaned["embarked"].mode()[0]
)

df_cleaned["embark_town"] = df_cleaned["embark_town"].fillna(
    "Unknown"
)

df_cleaned["deck"] = df_cleaned["deck"].cat.add_categories(
    ["Unknown"]
).fillna("Unknown")

# STEP 7: Handle missing values in other columns

df_cleaned["embark_town"] = df_cleaned[
    "embark_town"
].astype("category")

# STEP 8: Handle data types

categorical_columns = [
    "sex",
    "embarked",
    "class",
    "who",
    "deck",
    "embark_town",
    "alive",
    "alone"
]

for column in categorical_columns:
    df_cleaned[column] = df_cleaned[column].astype("category")

# STEP 9: Inspect duplicate records

print("\nDuplicate Rows:")
print(df_cleaned.duplicated().sum())

# We retain duplicate rows because identical records
# are not automatically proof of data-entry errors.

# STEP 10: Verify missing values after cleaning

print("\nMissing Values After Cleaning:")
print(df_cleaned.isnull().sum())

# STEP 11: Display cleaned dataset information

print("\nCleaned Dataset Shape:")
print(df_cleaned.shape)

print("\nCleaned Dataset Preview:")
print(df_cleaned.head())

print("\nCleaned Dataset Data Types:")
print(df_cleaned.dtypes)

# STEP 12: Save the cleaned dataset

os.makedirs("output", exist_ok=True)

df_cleaned.to_csv(
    "output/titanic_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved to:")
print("output/titanic_cleaned.csv")

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")