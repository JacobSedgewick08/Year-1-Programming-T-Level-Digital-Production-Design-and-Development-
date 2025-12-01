import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("circuits.csv")


country = input("Please enter a country with capital as first letter: ")
filtered_country = data[data["country"]==country]
print(filtered_country)

location = input("Please enter the location of the race with a capital as the first letter: ")
filtered_locati