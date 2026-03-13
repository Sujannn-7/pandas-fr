import pandas as pd

data = {
    "Name": ["Chris", "Steve", "Robert", "Tony", "Mark", "Natasha", "Jeremy", "Tom", "Teddy", "Marshall" ],
    "Age": [24, 58, 45, 55, 22, 46, 67, 56, 43, 56],
    "Salary": [50000, 45000, 43000, 56000, 45000, 50000, 34000, 54000, 60000, 45000],
    "Rating": [4.5, 4.0, 3.9, 4.6, 4.7, 4.1, 4.3, 4.1, 4.33, 4.19]
} 

df = pd.DataFrame(data)
if df["Salary"]>50000:
    print(df)

avg_salary = df["Salary"].mean()
print("Average salary: ", avg_salary)

min_salary = df["Salary"].min()
print(f"Minimum Salary: {min_salary}")

max_salary = df["Salary"].max()
print(f"Maximum Salary: {max_salary}")

sum_salary = df["Salary"].sum()
print(f"The sum of salary is: {sum_salary}")

median_salary = df["Salary"].median()
print(f"Median Salary: {median_salary}")

std_salary = df["Salary"].std()
print(f"Standard Deviation of Salary: {std_salary}")

