
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set_theme(style="whitegrid")

# Load cleaned Titanic dataset
df = pd.read_csv("data/processed/titanic_cleaned.csv")

# Display first five records
print("\n----- FIRST 5 RECORDS -----")
print(df.head())

# Dataset shape
print("\n----- DATASET SHAPE -----")
print(df.shape)

# Dataset information
print("\n----- DATASET INFORMATION -----")
df.info()

# Statistical summary
print("\n----- STATISTICAL SUMMARY -----")
print(df.describe(include="all"))

# Missing values
print("\n----- MISSING VALUES -----")
print(df.isnull().sum())

# Unique values
print("\n----- UNIQUE VALUES -----")
print(df.nunique())

# Survival distribution
print("\n----- SURVIVAL COUNT -----")
print(df["survived"].value_counts())

print("\n----- SURVIVAL PERCENTAGE -----")
print(df["survived"].value_counts(normalize=True) * 100)


# ==========================================
# SURVIVAL ANALYSIS
# ==========================================

# 1. Survival by Gender
print("\n----- SURVIVAL BY GENDER -----")

gender_analysis = df.groupby("sex", observed=True).agg(
    total_passengers=("survived", "count"),
    survivors=("survived", "sum"),
    survival_rate=("survived", "mean")
)

gender_analysis["survival_rate"] *= 100

print(gender_analysis.round(2))


# 2. Survival by Passenger Class
print("\n----- SURVIVAL BY PASSENGER CLASS -----")

class_analysis = df.groupby("class", observed=True).agg(
    total_passengers=("survived", "count"),
    survivors=("survived", "sum"),
    survival_rate=("survived", "mean")
)

class_analysis["survival_rate"] *= 100

print(class_analysis.round(2))


# 3. Survival by Age Group
print("\n----- SURVIVAL BY AGE GROUP -----")

df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teenager", "Young Adult", "Adult", "Senior"],
    include_lowest=True
)

age_analysis = df.groupby("age_group", observed=True).agg(
    total_passengers=("survived", "count"),
    survivors=("survived", "sum"),
    survival_rate=("survived", "mean")
)

age_analysis["survival_rate"] *= 100

print(age_analysis.round(2))


# 4. Survival by Embarkation Town
print("\n----- SURVIVAL BY EMBARKATION TOWN -----")

embark_analysis = df.groupby("embark_town", observed=True).agg(
    total_passengers=("survived", "count"),
    survival_rate=("survived", "mean")
)

embark_analysis["survival_rate"] *= 100

print(embark_analysis.round(2))


# ==========================================
# DATA VISUALIZATION
# ==========================================

# Chart 1: Survival Rate by Gender
plt.figure(figsize=(8, 5))
sns.barplot(
    x=gender_analysis.index,
    y=gender_analysis["survival_rate"]
)
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("charts/survival_by_gender.png")
plt.close()


# Chart 2: Survival Rate by Passenger Class
plt.figure(figsize=(8, 5))
sns.barplot(
    x=class_analysis.index,
    y=class_analysis["survival_rate"]
)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("charts/survival_by_class.png")
plt.close()


# Chart 3: Survival Rate by Age Group
plt.figure(figsize=(9, 5))
sns.barplot(
    x=age_analysis.index.astype(str),
    y=age_analysis["survival_rate"]
)
plt.title("Survival Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("charts/survival_by_age.png")
plt.close()


# Chart 4: Survival Rate by Embarkation Town
plt.figure(figsize=(9, 5))
sns.barplot(
    x=embark_analysis.index,
    y=embark_analysis["survival_rate"]
)
plt.title("Survival Rate by Embarkation Town")
plt.xlabel("Embarkation Town")
plt.ylabel("Survival Rate (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.savefig("charts/survival_by_embarkation.png")
plt.close()


print("\n----- CHART GENERATION -----")
print("All 4 charts saved successfully in the charts folder!")

