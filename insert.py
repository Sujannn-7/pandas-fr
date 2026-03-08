import pandas as pd

data = {
    "Name": ["Chirs", "Steve", "Robert", "Tony", "Mark", "Natasha", "Jeremy", "Tom", "Teddy", "Marshall" ],
    "Age": [24, 58, 45, 55, 22, 46, 67, 56, 43, 56],
    "Salary": [50000, 45000, 43000, 56000, 45000, 50000, 34000, 54000, 60000, 45000],
    "Rating": [4.5, 4.0, 3.9, 4.6, 4.7, 4.1, 4.3, 4.1, 4.33, 4.19]
}

df = pd.DataFrame(data)
df.index += 1
print(df)

df.insert(0, "Employee_id", [10, 20, 30, 40, 50, 60, 70, 80, 90, 100  ])
print(df)

df.insert(0, "Name", "Sujan")