import pandas as pd

data = pd.read_csv("sales_data.csv")
print(data.info()) # Number of rows and columns
print(data.columns) #column names
print(data["sales"].mean()) # Average sales
