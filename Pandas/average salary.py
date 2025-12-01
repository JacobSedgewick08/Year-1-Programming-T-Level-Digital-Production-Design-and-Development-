import pandas as pd
employee_data = pd.read_csv("employee_data.csv")

cleaned_data = employee_data.dropna()
avg_salary = cleaned_data.groupby("department")["salary"].mean()
print(avg_salary)
