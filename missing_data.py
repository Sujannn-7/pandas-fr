import pandas as pd

data = {
    "Name": ["Chirs", "Steve", "Robert", "Tony", None , "Natasha", "Jeremy", "Tom", "Teddy", None],
    "Age": [24, 58, 45, None, 22, 46, 67, 56, 43, None],
    "Salary": [50000, 45000, 43000, 56000, 45000, 50000, 34000, 54000, 60000, 45000],
    "Rating": [4.5, 4.0, None, 4.6, 4.7, 4.1, None, 4.1, 4.33, None]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())

print(df.isnull().sum())