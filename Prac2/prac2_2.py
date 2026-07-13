# Original nested tuple of subjects
nested_tuple = (
    ("Artificial Intelligence", 401),
    ("Data Structures", 402),
    ("Cloud Computing", 403)
)

# Sorting the nested tuple by subject code (index 1)
sorted_subjects = sorted(nested_tuple, key=lambda x: x[1])

# Display the sorted result
print("Sorted Subjects (by subject code):", sorted_subjects)
