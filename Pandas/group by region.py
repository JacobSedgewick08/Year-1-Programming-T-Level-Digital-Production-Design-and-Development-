import pandas as pd
data = pd.read_csv("sales_data.csv")

region_sales = data.groupby("region")["sales"].sum()# group by region and calculate total sales
sorted_sales = region_sales.sort_values(ascending=False)#sort results

print(sorted_sales)
