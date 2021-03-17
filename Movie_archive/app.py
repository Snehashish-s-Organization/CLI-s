# Made by Snehashish Laskar
# Made on 15-03-2021
# Developer Contact: snehashish.laskar@gmail.com
# This is a simple movie archive manager that stores info about movies 
import json

# Opening the data.json file to extract data

with open("data.json", "r") as file:
    data = json.load(file)

watched = []
watching = []

# Defining all the Valid Commands
def listofcommands():
    print("Type a to add a movie")
    print("Type l to search and get info about a movie ")
    print("Type w to see all the movies that you have watched")
    print("Type wa to see the movies that you are watching")
    print("Type c to change the status of a movie")
    print("Type rm to remove a movie")
    print("Type q to quit")


# Creating a function to add a movie to the archive
def AddMovie():
    # Getting info about the movie from the user
    movie_name = input("Enter the name of the Movie: ")
    movie_director = input("Enter the Director of the movie: ")
    movie_status = input("Enter the status (watched, watching, new) of the Movie: ")
    # Opening the JSON file and storing the info about the movie
    with open("data.json", "w") as file:
        data.append({"name": movie_name, "director": movie_director, "status": movie_status})
        json.dump(data, file)
    print(f"added the movie {movie_name} whose director is {movie_director} in the archive")

# Creating a function to look up a certain movie and tell the user the info
def LookUpmovie():
    # Getting the name of the movie
    movie_name = input("Enter the name of the movie you are looking for: ")
    for i in data:
        # Checking if the entered movie is in the archive
        if i["name"] == movie_name:
            name = i["name"]
            director = i["director"]
            status = i["status"]
            print(f"name of the movie is {name}")
            print(f"director of the movie is {director}")
            # Checking the status of the movie
            if status == "watched":
                print("you have watched this movie")
            elif status == "watching":
                print("you are watching this movie")
            elif status == "new":
                print("you have to start this movie")
        else:
            print("This movie is not there in the archive")

# Defining a function that will list all the movies that have been watched
def list_watched_movies():
    for i in data:
        if i["status"] == "watched":
            watched.append(i)
    print(watched)
# Defining a function that will list all the movies that the user is watching
def list_watching_movies():
    for i in data:
        if i["status"] == "watching":
            watching.append(i)
    print(watching)
# Defining a function that will change the status of the movie
def change_status():
    # Getting the movie's name and the changed status
    movie_name = input("Please enter the movie's name that you wanna change the status of:")
    new_status = input("Please enter the new status of the movie: ()")
    for i in data:
        name = i["name"]
        director = i["director"]

        if movie_name == i["name"]:
            with open("data.json", "w") as file:
                i["status"] = new_status
                json.dump(data, file)
# Defining a function that will remove a certain movie from the archive
def remove_movie():
    movie_name = input("please enter the name of the movie you wanna remove:")
    for i,j in enumerate(data):
        if j["name"] == movie_name:
            del data[i]
            with open("data.json", "w") as file:
                json.dump(data, file)
            print("Done!")
        else:
            print("That movie is not in the archive")

# Defining a dictionary of commands
commands = {"q": exit, "a": AddMovie, "l" : LookUpmovie, "r" : list_watched_movies, "re" : list_watching_movies, "s":listofcommands, "rm" : remove_movie, "c": change_status}

# Defining a function that will notify the user about the movies
def notify():
    for i in data:
        if i["status"] == "new":
            name = i["name"]
            print(f"Hey! You are yet to start watching {name}! If you alwatchedy have then change the status to watching!\n") 
        elif i["status"] == "watching":
            name = i["name"]
            print(f"Hey! You should finish watching the movie {name}! If you alwatchedy have then change the status to watched!\n") 

# Main Proccess 
def main():
    print("type s to see all the valid commands")
    
    while True:
        
        command = input("> ")
        for i, j in commands.items():
            if i == command:
                j()
                
notify()              
main()
        
