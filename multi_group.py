import pandas as pd

data = {
    "Name": ["Chris", "Steve", "Robert", "Tony", "Mark", "Natasha", "Jeremy", "Tom", "Teddy", "Marshall" ],
    "Age": [24, 58, 45, 45, 22, 46, 67, 56, 45, 56],
    "Salary": [50000, 45000, 43000, 56000, 45000, 50000, 34000, 54000, 60000, 45000],
    "Rating": [4.5, 4.0, 3.9, 4.6, 4.7, 4.1, 4.3, 4.1, 4.33, 4.19]
} 

df = pd.DataFrame(data)

grouped = df.groupby(["Name", "Age"], as_index= False)["Salary"].sum()
print(grouped)