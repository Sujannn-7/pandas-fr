import pandas as pd

data = {
    "Name": ["Chris", "Steve", "Robert", "Tony", None , "Natasha", "Jeremy", "Tom", "Teddy", None],
    "Age": [24, 58, 45, None, 22, 46, 67, 56, 43, None],
    "Salary": [50000, 45000, 43000, 56000, 45000, 50000, 34000, 54000, 60000, 45000],
    "Rating": [4.5, 4.0, None, 4.6, 4.7, 4.1, None, 4.1, 4.33, None]
}

df = pd.DataFrame(data)

# df["Salary"] = df["Salary"].fillna(df["Salary"].mean(), inplace=True)
# df["Rating"] = df["Rating"].fillna(df["Rating"].mean(), inplace=True)
# df["Age"] = df["Age"].fillna(df["Age"].mean(), inplace=True)
# df["Name"] = df["Name"].fillna("Unknown", inplace=True)
# print(df)

df.fillna({"Name": "Unknown", 
           "Rating": df["Rating"].mean(),
           "Age": df["Age"].mean(),
           "Salary": df["Salary"].mean()}, inplace=True)
print(df)