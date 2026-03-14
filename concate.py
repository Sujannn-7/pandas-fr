import pandas as pd

df_region1 = pd.DataFrame({
    "Name": ["Steve", "Chris"],
    "CustomerID": [1, 2]
})

df_region2 = pd.DataFrame({
    "Name": ["Sam", "Peter"],
    "CustomerID": [3, 4]
})


#concatenate vertically
df_ver = pd.concat([df_region1, df_region2],axis=0, ignore_index=True)
print(df_ver)

#concatenate horizontally
df_hori = pd.concat([df_region1, df_region2],axis=1, ignore_index=True)
print("\n", df_hori)