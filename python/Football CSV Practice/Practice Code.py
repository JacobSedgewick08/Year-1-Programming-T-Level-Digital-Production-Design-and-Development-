import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


 ### Print All Data ###

data = pd.read_csv("goalscorers 1.csv")
#print(data)



 ### Penalty vs Non-Penalty Goals ###

#nonpenalty_goals = data[data["penalty"]==False].shape[0]
#penalty_goals = data[data["penalty"]==True].shape[0]

#x = ["Penalty Goals", "Non-Penalty Goals"]
#y = [penalty_goals, nonpenalty_goals]
#plt.bar(x,y, color=["green", "red"])
#plt.title ("Penalty goals vs Non-Penalty goals")
#plt.show()

 ### Time of goal Pie Chart ###

#firsthalf_goals = data[data["minute"]<=45].shape[0]
#secondhalf_goals = data[data["minute"]>45].shape[0]
#extratime_goals = data[data["minute"]>90].shape[0]
#Type_of_goal = ["First Half", "Second Half", "Extra Time"]
#df = [firsthalf_goals, secondhalf_goals, extratime_goals]

#fig = plt.figure(figsize=(10, 7))
#plt.pie(df, labels=Type_of_goal)

#plt.show()


 ### Time of goal bar chart ###

firsthalf_goals = data[data["minute"]<=45].shape[0]
secondhalf_goals = data[data["minute"]>45].shape[0]
extratime_goals = data[data["minute"]>90].shape[0]
x = ["First Half Goals", "Second Half Goals", "Extra Time Goals"]
y = [firsthalf_goals, secondhalf_goals, extratime_goals]
plt.bar(x, y, color=["palegreen", "cyan", "crimson"])
plt.title ("Goals per Half")
plt.show()


 ### Own Goal vs Normal Goal Pie chart ### 

#own_goals = data[data["own_goal"]==True].shape[0]
#normal_goals = data[data["own_goal"]==False].shape[0]
#goal_type = ["Own Goal", "Normal Goal"]
#df = [own_goals, normal_goals]
#fig = plt.figure(figsize=(5,10))
#plt.pie(df, labels=goal_type)
#plt.title("Own goal vs normal goal")
#plt.show()


 ### Own goals vs normal goal Bar chart ###

#own_goals = data[data["own_goal"]==True].shape[0]
#normal_goals = data[data["own_goal"]==False].shape[0]
#x = ["Own Goals", "Normal Goals"]
#y = [own_goals, normal_goals]
#plt.bar (x,y, color=["purple", "pink"])
#plt.title("Own goals vs Normal goal bar chart")
#plt.show()




 ### Team home vs away goals Bar chart ### 

#team = input("Please enter a national team")
#home_goals = data[data["home_team"] == team].shape[0]
#away_goals = data[data["away_team"] == team].shape[0]

#x = ["Home Goals", "Away Goals"]
#y = [home_goals, away_goals]
#plt.bar (x, y, color=["green", "red"])
#plt.title(team, "- Home goals vs Away goals")
#plt.show()



