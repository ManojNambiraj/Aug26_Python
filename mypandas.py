# Pandas:

import pandas as pd

# marks = pd.Series([75, 82, 99, 67, 45])

# print(marks)

# marks = pd.Series(
#     [75, 82, 99, 67, 45], 
#     index=["Tamil", "Eng", "maths", "Computer", "EVS"]
# )

# print(marks)
# print(marks["Tamil"])

# data = {
#     "Name": ["Raj", "Arun", "Rani", "Kavitha", "Raj", "Arun", "Rani", "Kavitha", "Raj", "Arun", "Rani", "Kavitha"],
#     "Age": [21, 22, 20, 19,21, 22, 20, 19, 21, 22, 20, 19],
#     "Marks": [75, 88, 92, 57, 75, 88, 92, 57, 75, 88, 92, 57]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.head())
# print(df.tail())

data = pd.read_csv("data.csv")

print(data)