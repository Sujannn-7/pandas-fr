import pandas as pd

data = {
    "value": [10, 20, None, 40, None, 60], 
    "value1": [1, 4, None, 16, 25, None]
}

df = pd.DataFrame(data)
print(df)

df.interpolate(method="linear", axis=0, inplace=True)
print(df)

df.interpolate(method="polynomial", axis=0, inplace=True)
print(df)
