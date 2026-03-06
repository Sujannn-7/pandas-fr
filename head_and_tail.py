import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

n = int(input("Enter a number: "))

print("Displaying First n Rows")
print(df.head(n))

print("Displaying Last n Rows")
print(df.tail(n))

print("Displaying first 5 Rows")
print(df.tail())
