#2. Python Data Structure Challenges in Real-World Scenarios
#Task 1: Library System Enhancement Sharpen your skills in managing 
#and modifying data within tuples and lists.

#Problem Statement: You are maintaining a library system where each 
#book is stored as a tuple within a list. Your task is to update this system by 
#adding new books and ensuring no duplicates.

#Existing Library Data:

#library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.
import re
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_book():
    book=input("Input name of book:")
    author=input("Input author name:")
    book_checker=True
    for book_and_author in library:
        if book_and_author[0].lower()!=book.lower():
            continue
        else:
            print("Book already in library!")
            book_checker=False
            break
    if book_checker==True:
        library.append((book,author))
 
def print_library():
    for my_books in library:
        print(f"Book: {my_books[0]}\nAuthor:{my_books[1]}")

while True:
    user_choice=input("What would you like to do? [A]dd new book, [P]rint library list, [E]xit")
    if user_choice.lower()=="a" or user_choice.lower()=="add" or user_choice.lower()=="add new book":
        add_book()
    elif user_choice.lower()=="p" or user_choice.lower()=="print" or user_choice.lower()=="print library list":
        print_library()
    elif user_choice.lower()=="e" or user_choice.lower()=="exit":
        print("Thank for visiting the library!")
        break
    else:
        print("Input invalid! Please choose from the options listed.")