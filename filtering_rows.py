import pandas as pd

data = {
    "Name": ["Chirs", "Steve", "Robert", "Tony", "Mark", "Natasha", "Jeremy", "Tom", "Teddy", "Marshall" ],
    "Age": [24, 58, 45, 55, 22, 46, 67, 56, 43, 56],
    "Salary": [50000, 45000, 43000, 56000, 45000, 50000, 34000, 54000, 60000, 45000],
    "Rating": [4.5, 4.0, 3.9, 4.6, 4.7, 4.1, 4.3, 4.1, 4.33, 4.19]
}

df = pd.DataFrame(data)
df.index += 1

high_salary = df[df["Salary"]>50000]
print("People with salary greater than Rs. 50000")
print(high_salary)

#Salary greater than 50000 and rating greater than 4.2
print("\nPeople with salary greater than 50000 and rating greater than 4.2")
condition = df[(df["Salary"] > 50000) & (df["Rating"] > 4.2)]
print(condition)

condition1 = df[(df["Salary"] > 50000) | (df["Rating"] > 4.5)]
print("\n",condition1)