
import pandas as pd

# STEP 1: Load raw dataset
df = pd.read_csv("data/raw/titanic.csv")

print("Original Dataset Shape:", df.shape)

# STEP 2: Remove exact duplicate rows
df = df.drop_duplicates()

print("Shape After Removing Duplicates:", df.shape)

# STEP 3: Handle missing values

# Replace missing Age with median
df["age"] = df["age"].fillna(df["age"].median())

# Replace missing Embarked with mode
df["embarked"] = df["embarked"].fillna(
    df["embarked"].mode()[0]
)

# Replace missing Embark Town with mode
df["embark_town"] = df["embark_town"].fillna(
    df["embark_town"].mode()[0]
)

# Replace missing Deck with Unknown
df["deck"] = df["deck"].fillna("Unknown")

# STEP 4: Standardize text values
text_columns = df.select_dtypes(include="str").columns

for col in text_columns:
    df[col] = df[col].str.strip().str.lower()

# STEP 5: Correct data types
df["survived"] = df["survived"].astype("int64")
df["pclass"] = df["pclass"].astype("category")
df["sex"] = df["sex"].astype("category")
df["embarked"] = df["embarked"].astype("category")
df["class"] = df["class"].astype("category")
df["adult_male"] = df["adult_male"].astype("bool")
df["alone"] = df["alone"].astype("bool")

# STEP 6: Validate cleaned dataset
print("\n----- MISSING VALUES AFTER CLEANING -----")
print(df.isnull().sum())

print("\n----- DUPLICATES AFTER CLEANING -----")
print(df.duplicated().sum())

print("\n----- FINAL DATA TYPES -----")
print(df.dtypes)

# STEP 7: Save cleaned dataset
df.to_csv("data/processed/titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final Dataset Shape:", df.shape)

# STEP 8: Final verification

cleaned_df = pd.read_csv("data/processed/titanic_cleaned.csv")

print("\n----- FINAL VERIFICATION -----")

print("Rows:", cleaned_df.shape[0])
print("Columns:", cleaned_df.shape[1])

print("Total Missing Values:",
      cleaned_df.isnull().sum().sum())

print("Total Duplicate Rows:",
      cleaned_df.duplicated().sum())

print("\nData Cleaning Completed Successfully!")
