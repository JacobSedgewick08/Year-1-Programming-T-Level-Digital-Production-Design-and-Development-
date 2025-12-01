import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("streaming.csv")
#menu = int(input("Welcome to the menu would you like to:\n1.Filter by average rating\n2.Filter by genre\n3. Filter by Title\n"))

#Filter by average rating
#if menu == 1:
 #   Average=int(input("Please enter the average rating you would like the show to be above: "))
  #  filtered_data = data[data["AvgRating"]>Average]
   # print(filtered_data)

#Filter by genre
#if menu == 2:
 #   genre = input("please enter the genre you would like to view: ")
  #  filter_genre = data[data["Genre"]==genre]
   # print(filter_genre)

#Filter by title
#if menu == 3:
 #   Title = input("Please enter the title of the movie you would like to view: ")
  #  filter_movie = data[data["Title"]==Title]
   # print(filter_movie)

plt.bar(data["Genre"], data["WatchHours"])

plt.xlabel("Genre")
plt.ylabel("Watch Hours per genre")
plt.title("Watch hours per genre")
plt.show