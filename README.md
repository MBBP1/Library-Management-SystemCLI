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

## Usage
Once the program starts, you will be presented with a menu. Select an option by entering the corresponding number:
0. Add Ebook
1. Add Book
2. Add Member
3. Display Books
4. Display Members
5. Issue Book
6. Return Book
7. Display Transaction History
8. Remove Member
9. Update Member
10. Update Book
11. Search For Books
12. Remove Book
13. Exit

Follow the on-screen instructions to enter the necessary details.







