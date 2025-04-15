# Library Management System

## Overview
This Library Management System is a console-based application that allows users to manage books, e-books, and members within a library. The system provides functionalities to add, update, remove, and display books and members, as well as manage book borrowing and returning transactions.

## Features
- Add, update, remove, and search for books (physical and e-books)
- Add, update and remove members
- Borrow and return books
- Track transaction history per member
- View available books
- View members
- CLI-based interaction for easy terminal use
- Error handling for invalid inputs

Classes Overview

    Book: Represents a physical book with an ID, title, author, and available copies.

    Ebook: Inherits from Book, but instead of copies, tracks file size in MB.

    Member: Represents a library user who can borrow and return books.

    Library: Handles all core operations like adding/removing books and members, issuing/returning books, and displaying/searching data.

Requirements

    Python 3.6 or later

    No external libraries required

Usage

When the program is run, you will be presented with a numbered menu. You can perform actions like:

    Add a book or member

    Display all books or members

    Borrow or return a book

    Update or remove books/members

    Search books by title or author

    View all transaction history

All input is handled via the terminal. Follow the on-screen instructions to enter the necessary details.

Project Structure

    Book and Ebook classes demonstrate polymorphism.

    Member keeps track of borrowed books and transactions.

    Library class manages the overall system.

    Input validation is done through a helper function getInt().

Author

Mikkel Bentsen-Petersen
Created: March 25, 2025


How to Run

    Clone the repository:

git clone https://github.com/your-username/library-management-system.git

Navigate to the project directory:

cd library-management-system

Run the program:

    python3 library.py

    Make sure you have Python 3 installed on your system.




