# Created by Snehashish Laskar
# Created on 15-03-2021
# Contact: snehashish.laskar@gmail.com
# This is a Simple Login and Signup cli made to interact with json
import json
# Opening the data and log files to read and extract data from them
with open("data.json", "r") as file:
    data = json.load(file)

with open("log.json", "r") as file2:
    data2 = json.load(file2)
# Defining the Signup command
def signup():
    while True:
        # Getting the username and password
        username = input("Please choose a username: ")
        password = input("Please choose a password: ")
        confirm = input("Please confirm your password: ")
        # Checking if conformation password matches the password
        if password == confirm:
            # Writing to the json file to storw the username and password
            with open("data.json", "w") as file:
                json.dump([{"username": username, "password": password}], file)
            break
        else:
            print("passwords do not match")

# Defining the Login method
def login():
    # Defining a function that checks if the username and password entered are in the json file
    def validUser(username, password):
        for i in data:
            if i["username"] == username and i["password"] == password:
                return True
        return False
    
    for i in data:
        # Checking if there is a logged in user
        if data2 == []:
            while True:
                print("Log in Page!")
                # Getting the username and password
                username = input("Please enter your username: \n")
                password = input("Please enter your password: \n")
                # Validating the username and password using the validUser method
                if validUser(username, password):
                    # Writing to the json file to store the current logged in user's credentials
                    with open("log.json", "w") as file:
                        data2.append({"username": username, "password": password})
                        json.dump(data2, file)
                        print("You are logged in")
                        break
                # Checking if the password is incorrect
                elif username == i["username"] and password != i["password"]:
                    print("incorrect password")
                # Creating a new user if the entered username is invalid By the signup methid defined above
                else:
                    print("That user does not exist do you want to create a new one[Y/N] ?")
                    dec = input("->")
                    if dec == "Y"or "y":
                        signup()
                    else:
                        print("try loging in again:")
        # Checking if a user is already logged in
        elif data2[0]["username"] == i["username"]:
            return True
# Creating a logout function that logs out the user
def logout():
    with open("log.json", "w") as file:
        json.dump([], file)


        