import matplotlib.pyplot as plt
import pandas as pd

 ### Print first 5 data ###

df = pd.read_csv("video_games_dataset.csv")
#print(df.head())


 ### Basic Plot ###
#plt.plot(df["Release_Year"],df["Sales_Millions"], marker="o", linestyle="-", color="b")
#plt.xlabel("Release Year")
#plt.ylabel("Sales (Millions)")
#plt.title("Yearly Sales Trend")
#plt.show()


 ### Scatter Plot ###
#plt.scatter(df["User_Score"], df["Sales_Millions"], color="red")
#plt.xlabel("User Score")
#plt.ylabel("Sales (Millions)")
#plt.title("User Scores vs Sales")
#plt.show()


 ### Bar Charts ### 
#genre_counts = df["Genre"].value_counts()
#genre_counts.plot(kind="bar", color=["blue", "green", "red", "purple", "orange"])
#plt.xlabel("Genre")
#plt.ylabel("Number of games")
#plt.title("Games Per Genre")
#plt.show()


 ### Histograms ###
#plt.hist(df["Sales_Millions"], bins=10, color="blue", edgecolor="black")
#plt.xlabel("Sales (Millions)")
#plt.ylabel("Frequency")
#plt.title("Sales Distribution")
#plt.show()


 ### Pie Charts ### 
#platform_counts = df["Platform"].value_counts()
#plt.pie(platform_counts, labels=platform_counts.index, autopct="%1.1f%%")
#colors=["blue", "green", "red", "purple"]
#plt.title("Platform Distribution")
#plt.show()


 ### Customising Plots ### 
#plt.plot(df["Release_Year"], df["Sales_Millions"], linestyle="--", color="purple", linewidth=2, label="Sales Trend")
#plt.legend()
#plt.grid(True)
#plt.show()


 ### SubPlots ###
#fig, axs = plt.subplots(1, 2, figsize=(10, 5))
#axs[0].hist(df["Sales_Millions"], bins=10, color="blue", edgecolor="black")
#axs[0].set_title("Sales Dristribution")
#axs[1].scatter(df["User_Score"], df["Sales_Millions"], color="red")
#axs[1].set_title("User Score vs Sales")
#plt.show()


### Activity 3 ### 
#genre_counts = df["Genre"].value_counts()
#genre_counts.plot(kind="bar", color=["blue", "green", "red", "purple", "orange"])
#plt.xlabel("Genre")
#plt.ylabel("Number of games")
#plt.title("Games Per Genre")
#plt.show()


### Activity 4 ###
#plt.hist(df["Sales_Millions"], bins=15, color="blue", edgecolor="black")
#plt.xlabel("Sales (Millions)")
#plt.ylabel("Frequency")
#plt.title("Sales Distribution")
#plt.show()


### Activity 5 ###
#platform_counts = df["Platform"].value_counts()
#plt.pie(platform_counts, labels=platform_counts.index, autopct="%1.1f%%")
#colors=["blue", "green", "red", "purple"]
#plt.title("Platform Distribution")
#plt.show()


### Activity 6 ###
#fig, axs = plt.subplots(1, 2, figsize=(10, 5))
#axs[0].hist(df["Sales_Millions"], bins=10, color="blue", edgecolor="black")
#axs[0].set_title("Sales Dristribution")
#axs[1].scatter(df["User_Score"], df["Sales_Millions"], color="red")
#axs[1].set_title("User Score vs Sales")
#plt.show()

### Activity 7 ###
top_5 = df.nlargest(5, "Sales_Millions")
plt.scatter(df["User_Score"], df["Sales_Millions"], color="red")
plt.xlabel("User Score")
plt.ylabel("Sales (Millions)")
plt.title("User Scores vs Sales")
for _, row in top_5.iterrows():
    plt.text(row["User_Score"], row["Sales_Millions"], row["Game"], fontsize=9, ha='right')
plt.show()
