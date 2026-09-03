#9f.

print("S109 Neetu Salunkhe")

import pandas as pd

# Read the movie dataset
df = pd.read_csv("movie_ratings.csv")

print("ORIGINAL DATASET:")
print("=" * 80)
print(df.to_string(index=False))

# 1. Create a "Popularity" column based on Votes
# "Popular" if Votes >= 150000, "Average" if 100000-149999, "Less Popular" if < 100000
df["Popularity"] = df["Votes"].apply(
    lambda x: "Popular" if x >= 150000 else ("Average" if x >= 100000 else "Less Popular")
)

# 2. Create a "Rating_Category" column using Rating
# Function to calculate rating category
def calculate_rating_category(rating):
    if rating >= 8.5:
        return "Excellent"
    elif rating >= 8.0:
        return "Very Good"
    elif rating >= 7.5:
        return "Good"
    elif rating >= 7.0:
        return "Average"
    else:
        return "Below Average"

# Create Rating_Category column
df["Rating_Category"] = df["Rating"].apply(calculate_rating_category)

print("\n" + "=" * 80)
print("DATASET WITH NEW COLUMNS (Popularity & Rating_Category):")
print("=" * 80)
print(df.to_string(index=False))

# 3. Additional analysis - Create "Recommendation" column
df["Recommendation"] = df.apply(
    lambda row: "Must Watch" if row["Rating"] >= 8.5 and row["Votes"] >= 200000 
    else "Recommended" if row["Rating"] >= 8.0 
    else "Good" if row["Rating"] >= 7.5
    else "Skip", axis=1
)

print("\n" + "=" * 80)
print("DATASET WITH RECOMMENDATION COLUMN:")
print("=" * 80)
print(df[["Movie", "Rating", "Votes", "Rating_Category", "Popularity", "Recommendation"]].to_string(index=False))

# 4. Summary statistics
print("\n" + "=" * 80)
print("SUMMARY STATISTICS:")
print("=" * 80)
print(f"Number of movies: {len(df)}")
print(f"Average Rating: {df['Rating'].mean():.2f}")
print(f"Average Votes: {df['Votes'].mean():.0f}")
print("\nRating Category Distribution:")
print(df["Rating_Category"].value_counts())
print("\nPopularity Distribution:")
print(df["Popularity"].value_counts())
print("\nRecommendation Distribution:")
print(df["Recommendation"].value_counts())
