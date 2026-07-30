#5c.

import pandas as pd

# Dictionary
stress_level = {
    "Student1": "High",
    "Student2": "Medium",
    "Student3": "Low",
    "Student4": "High",
    "Student5": "Medium"
}

# Create Series
series = pd.Series(stress_level)

print(series)
