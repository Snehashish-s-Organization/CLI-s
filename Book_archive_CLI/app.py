
# Made by Snehashish Laskar
# Made on 15-03-2021
# Developer Contact: snehashish.laskar@gmail.com
# This is a simple book archive manager that stores info about books 
import json

# Opening the data.json file to extract data

with open("data.json", "r") as file:
    data = json.load(file)

read = []
reading = []

# Defining all the Valid Commands
def listofcommands():
    print("Type a to add a book")
    print("Type l to search and get info about a book ")
    print("Type r to see all the books that you have read")
    print("Type re to see the books that you are reading")
    print("Type c to change the status of a book")
    print("Type rm to remove a book")


# Creating a function to add a book to the archive
def AddBook():
    # Getting info about the book from the user
    book_name = input("Enter the name of the book: ")
    book_author = input("Enter the Author of the book: ")
    book_status = input("Enter the status of the book (type read if already completed, type reading if you are in the middle of the book or type new if you have not started yet): ")
    
    # Opening the JSON file and storing the info about the book
    with open("data.json", "w") as file:
        data.append({"name": book_name, "author": book_author, "status": book_status})
        json.dump(data, file)
    print(f"added the book {book_name} whose author is {book_author} in the archive")

# Creating a function to look up a certain book and tell the user the info
def LookUpBook():
    # Getting the name of the book
    book_name = input("Enter the name of the book you are looking for: ")
    for i in data:
        # Checking if the entered book is in the archive
        if i["name"] == book_name:
            name = i["name"]
            author = i["author"]
            status = i["status"]
            print(f"name of the book is {name}")
            print(f"author of the book is {author}")
            # Checking the status of the book
            if status == "read":
                print("you have read this book")
            elif status == "reading":
                print("you are reading this book")
            elif status == "new":
                print("you have to start this book")
        else:
            print("This book is not there in the archive")

# Defining a function that will list all the books that have been read
def list_Read_Books():
    for i in data:
        if i["status"] == "read":
            read.append(i)
    print(read)
# Defining a function that will list all the books that the user is reading
def list_reading_books():
    for i in data:
        if i["status"] == "reading":
            reading.append(i)
    print(reading)
# Defining a function that will change the status of the book
def change_status():
    # Getting the book's name and the changed status
    book_name = input("Please enter the book's name that you wanna change the status of:")
    new_status = input("Please enter the new status of the book: ()")
    for i in data:
        name = i["name"]
        author = i["author"]

        if book_name == i["name"]:
            with open("data.json", "w") as file:
                i["status"] = new_status
                json.dump(data, file)
# Defining a function that will remove a certain book from the archive
def remove_book():
    book_name = input("please enter the name of the book you wanna remove:")
    for i,j in enumerate(data):
        if j["name"] == book_name:
            del data[i]
            with open("data.json", "w") as file:
                json.dump(data, file)
        print("Done!")

# Defining a dictionary of commands
commands = {"a": AddBook, "l" : LookUpBook, "r" : list_Read_Books, "re" : list_reading_books, "s":listofcommands, "rm" : remove_book, "c": change_status}

# Defining a function that will notify the user about the books
def notify():
    for i in data:
        if i["status"] == "new":
            name = i["name"]
            print(f"Hey! You are yet to start reading {name}! If you already have then change the status to reading!\n") 
        elif i["status"] == "reading":
            name = i["name"]
            print(f"Hey! You should finish reading the book {name}! If you already have then change the status to read!\n") 

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
        
