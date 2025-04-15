import unittest
from datetime import datetime
from Library_cli import Book, Ebook, Member, Library

class TestLibraryManagement(unittest.TestCase):

    # SetUp Runs before each test and 
    def setUp(self):
        self.book = Book(1, "Python Programming", "John Doe", 3) 
        self.ebook = Ebook(2, "Machine Book", "Jane Doe", 5)
        self.member = Member(1, "Alice")
        self.library = Library()

    def test_book_initialization(self):
        self.assertEqual(self.book.book_id, 1) 
        self.assertEqual(self.book.title, "Python Programming") 
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.copies, 3)
    
    def test_ebook_initialization(self):
        self.assertEqual(self.ebook.book_id, 2)
        self.assertEqual(self.ebook.title, "Machine Book")
        self.assertEqual(self.ebook.author, "Jane Doe")
        self.assertEqual(self.ebook.file_size, 5)
    
    def test_member_initialization(self):
        self.assertEqual(self.member.member_id, 1)
        self.assertEqual(self.member.name, "Alice")
        self.assertEqual(self.member.borrowed_books, [])
        self.assertEqual(self.member.transaction_history, [])
    
    def test_library_add_book(self):
        self.library.add_book(self.book)
        self.assertIn(self.book, self.library.books)
    
    def test_library_add_member(self):
        self.library.add_member(self.member)
        self.assertIn(self.member, self.library.members)
    
    def test_member_borrow_book(self):
        self.member.borrow_book(self.book)
        self.assertIn("Python Programming", self.member.borrowed_books)
        self.assertEqual(self.book.copies, 2)
    
    def test_member_borrow_ebook(self):
        self.member.borrow_book(self.ebook)
        self.assertIn("Machine Book", self.member.borrowed_books)
    
    def test_member_return_book(self):
        self.member.borrow_book(self.book)
        self.member.return_book(self.book)
        self.assertNotIn("Python Programming", self.member.borrowed_books)
        self.assertEqual(self.book.copies, 3)
    
    def test_library_remove_book(self):
        self.library.add_book(self.book)
        self.library.remove_book(1)
        self.assertNotIn(self.book, self.library.books)
    
    def test_library_remove_member(self):
        self.library.add_member(self.member)
        self.library.remove_member(1)
        self.assertNotIn(self.member, self.library.members)
    
    def test_library_issue_book(self):
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.library.issue_book(1, 1)
        self.assertIn("Python Programming", self.member.borrowed_books)
        self.assertEqual(self.book.copies, 2)
    
    def test_library_return_book(self):
        self.library.add_book(self.book)
        self.library.add_member(self.member)
        self.library.issue_book(1, 1)
        self.library.return_book(1, 1)
        self.assertNotIn("Python Programming", self.member.borrowed_books)
        self.assertEqual(self.book.copies, 3)
    
    def test_update_book(self):
        self.library.add_book(self.book)
        self.library.update_book(1, title="Advanced Python", author="John Smith", copies=5)
        self.assertEqual(self.book.title, "Advanced Python")
        self.assertEqual(self.book.author, "John Smith")
        self.assertEqual(self.book.copies, 5)
    
    def test_update_member(self):
        self.library.add_member(self.member)
        self.library.update_member(1, "Bob")
        self.assertEqual(self.member.name, "Bob")
    
    def test_search_books(self):
        self.library.add_book(self.book)
        found_books = self.library.search_books("Python")
        self.assertIn(self.book, found_books)
    
    def test_display_transaction_history(self):
        self.member.borrow_book(self.book)
        self.member.return_book(self.book)
        history = self.member.transaction_history
        self.assertTrue(any("Borrowed" in entry for entry in history))
        self.assertTrue(any("Returned" in entry for entry in history))

if __name__ == '__main__':
    unittest.main()
