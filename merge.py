import pandas as pd

df_customers = pd.DataFrame({
    'Cust_Id':[1, 2, 3, 4, 5],
    'Cust_Name': ["Chris", "Robert", "Buchanen", "Jeremy", "Elizabeth"]
})

df_order = pd.DataFrame({
    'Cust_Id':[1, 2, 3, 4, 6],
    'Cust_order': [1500, 260, 1140, 2600, 7000]
})

# print("Inner Join")
# df_merged = pd.merge(df_customers, df_order, on="Cust_Id", how="inner" )
# print(df_merged)

# print("\n Outer join")
# df_merged1 = pd.merge(df_customers, df_order, on="Cust_Id", how="outer" )
# print(df_merged1)

df_merged2 = pd.merge(df_customers, df_order, how="cross")
print(df_merged2)

# df_merged3 = pd.merge(df_customers, df_order, on="Cust_Id", how="left" )
# print(df_merged3)

# df_merged4 = pd.merge(df_customers, df_order, on="Cust_Id", how="right" )
# print(df_merged4)


