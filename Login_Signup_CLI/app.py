import json


# Adds user
def addUser():
    """"Adds a user to the bot"""
    username = input("Set Username:\n")
    password = input("Set Password:\n")
    bal = 0
    # Check if user with username already already exists or not
    for i in data:
        # If it exists, complain to user
        if i["username"] == username:
            return "User with username %s already exists" % username
    # If user doesn't already exist, add user to data variable
    data.append({
        "username": username,
        "password": password,
        "bal": bal
    })
    # Dump data to data.json. Therefore mutating the json file
    with open("data.json", "w") as edit:
        json.dump(data, edit)
    return "added user with name: %s, password: %s" % (username, password)


# Removes user
def removeUser(username, password):
    """Removes user from bot data"""
    for i, j in data:
        if j["username"] == username and j["password"] == password:
            del data[i]
            return "Removed User %s. Remaining users: %i" % (username, len(data))
    return "Couldn't find user: %s. Please check and try again" % username


def validUser(username, password):
    """Checks if entered username and password are valid"""
    # print(data)
    # print("verifying credentials")
    for i in data:
        if i["username"] == username and i["password"] == password:
            # print("all good!")
            return True
    # print("username or password is not valid")
    return False


def findIndex(username):
    for i, j in enumerate(data):
        if j["username"] == username:
            return i


def login():
    # print("trying to log in...")
    while True:
        username = input("Enter Username:\n")
        password = input("Enter Password:\n")
        # print("verifying credentials...")
        if validUser(username, password):
            # print("verfied credentials. all good!")
            try:
                print("logged in as %s" % username)
                global logged_in
                logged_in = True
                break
            except Exception:
                raise Exception
        else:
            print("User doesn't exist")
            newUser = input("create new user? [Y/n]\n").lower()
            if newUser == "y":
                print(addUser())
            else:
                print("Ok then. Try logging in again.")
    global user_index, userstate
    user_index = findIndex(username)
    userstate = data[user_index]


def checkLogin():
    # print(userstate)
    # print(userstate)
    # global userstate
    # print(userstate)
    # print("checking login...")
    if not logged_in:
        # print("No saved user state available. Sign in again.")
        # username = login()[0]
        # # print(username)
        # for i, k in enumerate(data):
        #     # print(i)
        #     if k["username"] == username:
        #         for j in k:
        #             userstate[j] = k[j]
        #         user_index = i
        #         # print("user_index" in globals())
        #         # userstate = i
        #         # print(userstate)
        login()
    # else:
    #     print("Continuing with previous user state...")
    #     print("Logged in as %s" % userstate['username'])
    #     # global logged_in
    #     # logged_in = True
    else:
        print("User %s is already logged in" % userstate['username'])


def update():
    if logged_in:
        data[user_index] = userstate


def end_process():
    update()
    with open("data.json", "w") as datafile:
        json.dump(data, datafile)
    with open("user_state.json", "w") as statefile:
        json.dump(userstate, statefile)
    print("Exiting bot...")
    exit()


def logout():
    # print(logged_in)
    # if not loggedIn:
    #     print("Already logged out")
    #     return
    update()
    # userstate = {}
    global userstate
    userstate = {}
    with open("user_state.json", "w") as statefile:
        json.dump(userstate, statefile)
    global logged_in
    logged_in = False
    # print("logged_in" in globals())
    print("Successfully logged out")


def checkLogout():
    if logged_in:
        logout()
    else:
        print("Already logged out.")


def getBal():
    if not logged_in:
        print("Please log in first")
        return
    print("Username: %s, Balance: %s" % (userstate["username"], userstate["bal"]))


def work(command):
    def chooseJob():
        job_list = ["programmer", "coder", "mathematician", "physicist", "teacher", "artist"]
        while True:
            print("what would you like to work as:")
            for i in job_list:
                print("> %s" % i)
            work_choice = input().strip()
            if work_choice in job_list:
                userstate["job"] = work_choice
                print("You work as a/an %s now." % work_choice)
                break
            else:
                print("That is not a valid option")
    
    def resign():
        sure = input("Are you sure you want to resign your job as " \
            "a/an %s? [Y/n]" % userstate["job"]).lower() == "y"
        if sure:
            occupation = userstate["job"]
            del userstate["job"]
            print("You no longer work as a/an %s" % occupation)
        else:
            print("You were just about to enter the boss's room.")
            print("You have kept your job as a/an %s" % userstate["job"])

    def salary():
        pass

    def workwork():
        pass
    print("Working work : %s" % command)
    # try:
    #     job = userstate["job"]
    # except KeyError:
    #     print("You don't have a job yet!")
    #     print("type:\n\twork choose to view job list")
    # work_commands = {"choose": chooseJob, "resign": resign, "sal": salary, }
    # command = input().split()
    # try:
    #     command



def main():
    if logged_in:
        print("Continuing with previous user state...")
        print("Logged in as %s" % userstate['username'])
    else:
        print("No saved user state available. Sign in again")
        print("to get access to user commands")
    # print(userstate)
    while True:
        command = input().split()
        try:
            commandList[command[0]]()
        except KeyError:
            pass
        except ValueError:
            commandList[command[0]](command)


with open("data.json", "r") as file1:
    data = json.load(file1)

with open("user_state.json", "r") as file2:
    userstate = json.load(file2)

commandList = {"login": checkLogin, "exit": end_process, \
    "logout": checkLogout, "bal": getBal, "work": work}

logged_in = userstate != {}

if logged_in:
    user_index = findIndex(userstate["username"])

# print(data)
# print(userstate)

main()
checkLogin()
