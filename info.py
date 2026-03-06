import pandas as pd

df = pd.read_json("sample_Data.json")
print(df.info())

data = {
    "Name": ["Chris", "Robert", "Steve", "Jeremy"],
    "Age": [27, 28, 47, 58],
    "Address": ["Brooklyn", "New York", "Massachusetts", "Houston"]
}

df1 = pd.DataFrame(data)
print(df1.info())
