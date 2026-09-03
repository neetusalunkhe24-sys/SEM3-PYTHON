#9e.

print("S109 Neetu Salunkhe")

import pandas as pd

# Read the movie dataset
df = pd.read_csv("movie_ratings1.csv")  

print("ORIGINAL DATASET:")
print("=" * 80)
print(df.to_string(index=False))

# 1. Check missing values (Boolean mask)
print("\n" + "=" * 80)
print("MISSING VALUES (True = Missing, False = Present):")
print("=" * 80)
print(df.isnull())

# 2. Count missing values in each column
print("\n" + "=" * 80)
print("COUNT OF MISSING VALUES PER COLUMN:")
print("=" * 80)
print(df.isnull().sum())

# 3. Replace missing Rating values with average Rating
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

# 4. Replace missing Votes values with average Votes
df["Votes"] = df["Votes"].fillna(df["Votes"].mean())

# 5. Replace missing Language values with mode (most frequent)
df["Language"] = df["Language"].fillna(df["Language"].mode()[0])

print("\n" + "=" * 80)
print("CLEANED DATASET (Missing Values Replaced):")
print("=" * 80)
print(df.to_string(index=False))

# Additional analysis
print("\n" + "=" * 80)
print("SUMMARY AFTER CLEANING:")
print("=" * 80)
print(f"Total missing values after cleaning: {df.isnull().sum().sum()}")
print(f"\nAverage Rating: {df['Rating'].mean():.2f}")
print(f"Average Votes: {df['Votes'].mean():.0f}")
print(f"\nMost Common Language: {df['Language'].mode()[0]}")
