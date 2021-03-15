# Made by Snehashish Laskar
# Made on 15-03-2021
# Developer Contact: snehashish.laskar@gmail.com

import json


with open("data.json", "r") as file:
    data = json.load(file)

read = []
reading = []

def listofcommands():
    print("Type a to add a book")
    print("Type l to search and get info about a book ")
    print("Type r to see all the books that you have read")
    print("Type re to see the books that you are reading")
    print("Type c to change the status of a book")
    print("Type rm to remove a book")



def AddBook():
    book_name = input("Enter the name of the book: ")
    book_author = input("Enter the Author of the book: ")
    book_status = input("Enter the status of the book (type read if already completed, type reading if you are in the middle of the book or type new if you have not started yet): ")
    with open("data.json", "w") as file:
        data.append({"name": book_name, "author": book_author, "status": book_status})
        json.dump(data, file)
    print(f"added the book {book_name} whose author is {book_author} in the archive")

def LookUpBook():
    book_name = input("Enter the name of the book you are looking for: ")
    for i in data:
        if i["name"] == book_name:
            name = i["name"]
            author = i["author"]
            status = i["status"]
            print(f"name of the book is {name}")
            print(f"author of the book is {author}")
            if status == "read":
                print("you have read this book")
            elif status == "reading":
                print("you are reading this book")
            elif status == "new":
                print("you have to start this book")

def list_Read_Books():
    for i in data:
        if i["status"] == "read":
            read.append(i)
    print(read)

def list_reading_books():
    for i in data:
        if i["status"] == "reading":
            reading.append(i)
    print(reading)

def change_status():
    book_name = input("Please enter the book's name that you wanna change the status of:")
    new_status = input("Please enter the new status of the book: ()")
    for i in data:
        name = i["name"]
        author = i["author"]
        if book_name == i["name"]:
            with open("data.json", "w") as file:
                i["status"] = new_status
                json.dump(data, file)

def remove_book():
    book_name = input("please enter the name of the book you wanna remove:")
    for i,j in enumerate(data):
        if j["name"] == book_name:
            del data[i]
            with open("data.json", "w") as file:
                json.dump(data, file)
        print("Done!")
        
commands = {"a": AddBook, "l" : LookUpBook, "r" : list_Read_Books, "re" : list_reading_books, "s":listofcommands, "rm" : remove_book, "c": change_status}
                  
def main():
    print("type s to see all the valid commands")
    
    while True:
        
        command = input("> ")
        for i, j in commands.items():
            if i == command:
                j()
                
                





       
main()
        
