"""
Created by Snehashish Laskar
Created on 25-03-2021
Developer contact: snehashish.laskar@gmail.com
Github: https://github.com/snehashish090
This is a book suggesting CLI
"""

# Importing Json module as i am storing data i form of json
import json

# Opening the file to get data
with open("dataq.json", "r") as file:
    data = json.load(file)

# Defining an user
user = "snehashish"

# Defining a function that will add a student to the list of people who have borrowed a book
def add_student():
    book_name = input("enter the book name")
    name = input("Enter student who as read the book: ")

    for i in data:
        if i["name"] == book_name:
            i["borrowed by"].append(name)

    with open("dataq.json", "w") as file:
        json.dump(data, file)

# Defining a function that will add a brand new book to the library
def add_new_book():
    name = input("enter the name of the book you want to add: ")
    typ = input("enter the type of the book: ")
    print("As the book is new ther are no readers")

    with open("dataq.json", "w") as file:
        data.append({
            "name": name,
            "type": typ,
            "borrowed by": []
        })
        json.dump(data, file)
        print(f"added book {name} to library")

# Defining a function that will add an existing book to the library
def existing_book():
    name = input("enter the name of the book: ")
    typ = input("enter the type of the book: ")
    print("you can add readers later")

    with open("dataq.json", "w") as file:
        data.append({
            "name": name,
            "type": typ,
            "borrowed by": []
        })
        json.dump(data, file)
    print(f"added book {name}")

# Defining a function that will suggest the user based on the input
def suggest_book():
    books = []
    typ = input("enter the type of the book: ")
    for book in data:
        if book["type"] == typ:
            if user in book["borrowed by"]:
                return True
            else:
                books.append(book["name"])
    print("here are some books you can read: ")
    for i in books:
        print(i)

# Defining all the actions
commands = {"s": suggest_book, "e": existing_book,
            "n": add_new_book, "as": add_student}

# Main CLI Loop
while True:
    command = input(">")
    for i, j in commands.items():
        if i == command:
            j()
