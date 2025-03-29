"""
Library Management System
==========================
This provides a simple Library Management System that allows users to manage books, e-books,
and members within a library.

Features:
- Add, update, remove, and display books and members.
- Borrow and return books with transaction tracking.
- Search books by title or author.
- Display transaction history of members.
- Console-based user interface for interaction.

Author: [Mikkel Bentsen-Petersen]
Date: [2025-03-25]
"""

from datetime import datetime

# Class that represents a physical book in the library.
class Book:
    def __init__(self, book_id, title, author, copies):  # Initializes a book with ID, title, author, and number of copies.
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    # Method that displays book details.
    def display_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}") # Udskriver bogens information


####################################################################################################################################################################################


# Class that represents an e-book, inheriting from Book. (Polymorphism)
class Ebook(Book):
    def __init__(self, book_id, title, author, file_size):  # Initializes a e-book with extra attributs for file size
        super().__init__(book_id, title, author, copies=None)  
        self.file_size = file_size

    # Method that displays e-book details.
    def display_info(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, File Size: {self.file_size} MB") 


####################################################################################################################################################################################


# Class that represents a library member.
class Member:
    def __init__(self, member_id, name):  
        self.member_id = member_id  
        self.name = name  
        self.borrowed_books = []       # List
        self.transaction_history = []  # List

    # Method that displays member details.
    def display_info(self):
        print(f"ID: {self.member_id}, Name: {self.name}, Borrowed Books: {', '.join(self.borrowed_books) if self.borrowed_books else 'None'}") 

    # Method that handles book borrowing.
    def borrow_book(self, book):
        if isinstance(book, Ebook):  
            self.borrowed_books.append(book.title)  
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            self.transaction_history.append(f"Borrowed Ebook '{book.title}' on {transaction_time}")  
            print(f"{self.name} borrowed Ebook '{book.title}'")  
        elif book.copies > 0:  
            book.copies -= 1  
            self.borrowed_books.append(book.title) 
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
            self.transaction_history.append(f"Borrowed '{book.title}' on {transaction_time}")  
            print(f"{self.name} borrowed '{book.title}'")  
        else:
            print(f"Sorry, '{book.title}' is not available.")  

    # Method that handles book returning.
    def return_book(self, book):
        if book.title in self.borrowed_books: 
            if not isinstance(book, Ebook):  
                book.copies += 1  
            self.borrowed_books.remove(book.title) 
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            self.transaction_history.append(f"Returned '{book.title}' on {transaction_time}") 
            print(f"{self.name} returned '{book.title}'") 
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")  

    # Method that displays transactions history
    def display_transaction_history(self):
        print(f"\nTransaction History for {self.name}:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transaction history.")


####################################################################################################################################################################################


# Class that manages books and members in the library.
class Library:
    def __init__(self):
        self.books = []  # List
        self.members = []  # List
        
    # Method that adds a book to the library.
    def add_book(self, book):
        if any(b.book_id == book.book_id for b in self.books):
            print(f"Book/Ebook with ID: {book.book_id} already exists")
        else:
            self.books.append(book)
            print(f"Book/Ebook '{book.title}' added to the library.")

    # Method that removes a book.
    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ID {book_id} not found.")
    
    # Method that updates a books book_id, title, author and number of copies or file size. 
    def update_book(self, book_id, title=None, author=None, copies=None, file_size=None):
        for book in self.books:
            if book.book_id == book_id:
                if title:
                    book.title = title
                if author:
                    book.author = author
                if isinstance(book, Ebook):
                    if file_size is not None:
                        book.file_size = file_size
                else:
                    if copies is not None:
                        book.copies = copies

                print(f"Book '{book_id}' updated successfully.")
                return
        print(f"Book with ID {book_id} not found.")

    # Method that adds a member to the library.
    def add_member(self, member):
        if any(m.member_id == member.member_id for m in self.members):
            print(f"Member with ID: {member.member_id} already exists")
        else:
            self.members.append(member)
            print(f"Member '{member.name}' added to the library.")

    # Method that removees a member from the library.
    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member '{member.name}' removed from the library.")
                return
        print(f"Member with ID {member_id} not found.")

    # Method that updates a members name.
    def update_member(self, member_id, new_name):
        for member in self.members:
            if member.member_id == member_id:
                old_name = member.name
                member.name = new_name
                print(f"Member '{old_name}' renamed to '{new_name}'.")
                return
            print(f"Member with ID {member_id} not found.")

    # Method that displays all books in the library.
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            if isinstance(book, Ebook):
                print("[Ebook] ", end="")
            else:
                print("[Book]  ", end="")
            book.display_info()
        input("\nPress Enter to continue...")

    # Method that shows all members in the library.
    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            member.display_info()
        input("\nPress Enter to continue...")

    # Method that allows a member to borrow a book.
    def issue_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)
        if member and book:
            member.borrow_book(book)
        else:
            print("Invalid member ID or book ID.")

    # Method that allows a member to return a book.
    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)
        if member and book:
            member.return_book(book)
        else:
            print("Invalid member ID or book ID.")

    # Method that allows you to search for a book.
    def search_books(self, search_term):
        found_books = [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]
        if found_books:
            print("\nSearch Results:")
            for book in found_books:
                book.display_info()
        else:
            print(f"No books found matching '{search_term}'.")
        
        return found_books  # Tilføj returnering af listen   

    # Method that displays transactions history for all members.
    def display_transaction_history(self):
        for member in self.members:
            member.display_transaction_history()
        input("\nPress Enter to continue...")


####################################################################################################################################################################################


# Funktion that ensure only holenumbers(int) allowed
def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


####################################################################################################################################################################################


# Main funktion that runs the Library Management System - [CLI].
def main():
    library = Library()


    while True:
        print("\nLibrary Management System")
        print("0. Add Ebook")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Display Books")
        print("4. Display Members")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Display Transaction History")
        print("8. Remove Member")
        print("9. Update Member")
        print("10. Update Book")
        print("11. Search For Books")
        print("12. Remove Book")
        print("13. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "0":
            book_id = getInt("Enter EBook ID: ")
            title = input("Enter EBook Title: ")
            author = input("Enter EBook Author: ")
            file_size = getInt("Enter File Size (MB): ")
            library.add_book(Ebook(book_id, title, author, file_size))
        elif choice == "1":
            book_id = getInt("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            copies = getInt("Enter Number of Copies: ")
            library.add_book(Book(book_id, title, author, copies))
        elif choice == "2":
            member_id = getInt("Enter Member ID: ")
            name = input("Enter Member Name: ")
            library.add_member(Member(member_id, name))
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            library.display_members()
        elif choice == "5":
            member_id = getInt("Enter Member ID: ")
            book_id = getInt("Enter Book ID: ")
            library.issue_book(member_id, book_id)
        elif choice == "6":
            member_id = getInt("Enter Member ID: ")
            book_id = getInt("Enter Book ID: ")
            library.return_book(member_id, book_id)
        elif choice == "7":
            library.display_transaction_history()
        elif choice == "8":
            member_id = getInt("Enter Member ID: ")
            library.remove_member(member_id)
        elif choice == "9":
            member_id = getInt("Enter Member ID: ")
            new_name = input("Input The Rename: ")
            library.update_member(member_id, new_name)
        elif choice == "10":
            book_id = getInt("Enter The ID Of The Book You Want To update: ")
            title = input("Enter New Book Title: ")
            author = input("Enter Book Author: ")
            copies = getInt("Enter Number of Copies: ")
            library.update_book(book_id, title, author, copies)
        elif choice == "11":
            search_term = input("Search For Book: ")
            library.search_books(search_term)
        elif choice == "12":
            book_id = getInt("Enter The ID Of The Book You Want To Remove: ")
            library.remove_book(book_id)
        elif choice == "13":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
