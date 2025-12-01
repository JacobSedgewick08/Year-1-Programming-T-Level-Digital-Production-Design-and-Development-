import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_dataset.csv")
#print(df[["Name", "Age"]])

 ### Print singular column ###
#print(df.iloc[1])

 ### Print over 30 ###
#over_30 = df[df["Age"]>30]
#print (over_30)

 ### Delete a Column ###
#df = df.drop(columns=["Salary"])
#print (df)

 ### Sort data in order ###
#df = df.sort_values("Age", ascending=False)
#print (df)

 ### Adding a column ###
#df["Bonus"] = ["Salary" * 1.10]


 ### Task 1 ###
#print(df.head(10)) 

 ### Task 2 ###
#print(df[["Name", "Age"]])
#over_30 = df[df["Age"]>30]
#print(over_30)

#df = df.sort_values("Age", ascending=False)
#print(df)

 ### Task 3 ###

#bonus = 1.10
#df["Bonus"] = df["Salary"] * bonus
#print(df)

#mean_salary = df["Salary"].mean()
#print("The average salary is", mean_salary,"per year")
#mean_experience = df["Experience_Years"].mean()
#print("The average experience is",mean_experience,"years")
#mean_age = df["Age"].mean()
#print("The average age is",mean_age," years old")


### Task 4 ###

#department = input("Please enter one of the following\nHR\nFinance\nIT\nMarketing\n")
#df = df[df["Department"]==department]
#mean_salary = df["Salary"].mean()
#print(df)
#print("The mean salary for",department,"is",mean_salary,"per year")


#plt.hist(df["Salary"], bins=5, color="blue", edgecolor="black")
#plt.xlabel("Salary")
#plt.ylabel("Number of employees")
#plt.title("Salary Distribution")
#plt.show()

#plt.scatter(df["Experience_Years"], df["Salary"], color="red")
#plt.xlabel("Experience (Years)")
#plt.ylabel("Salary")
#plt.title("Experience vs salary")
#plt.show()

department_counts = df["Department"].value_counts()
department_counts.plot(kind="bar", color=["blue", "green", "red", "purple"])
plt.xlabel("Department")
plt.ylabel("Number of employees")
plt.title("Employees per department")
plt.xticks(rotation=45)
plt.show()