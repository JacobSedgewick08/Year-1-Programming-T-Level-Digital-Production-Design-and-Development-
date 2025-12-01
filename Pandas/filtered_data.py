import pandas as pd

data = pd.read_csv("sales_data.csv")

filtered_data = data[data["sales"]>500] #Filter rows
filtered_data["profit_margin"]=filtered_data["profit"]/filtered_data["sales"]
print(filtered_data)
