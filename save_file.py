import pandas as pd

data = {
    "Name": ["Chris", "Robert", "Steve", "Jeremy"],
    "Age": [27, 28, 47, 58],
    "Address": ["Brooklyn", "New York", "Massachusetts", "Houston"]
}

df = pd.DataFrame(data)
df.index = df.index+1
print(df)



# df.to_csv("Output.csv", index=False)
# df.to_json("Output.json", index=False)
df.to_excel("Output.xlsx", index=False)