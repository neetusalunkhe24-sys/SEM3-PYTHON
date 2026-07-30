import pandas as pd

# Load the dataset
df = pd.read_csv("StressLevelDataset.csv")

# Statistical summary
print("Statistical Information:")
print(df.describe(include='all'))

# Dataset information
print("\nDataset Information:")
print(df.info())
