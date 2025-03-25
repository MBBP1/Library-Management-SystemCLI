import unittest
from datetime import datetime
from Library_cli import Book, Ebook, Member, Library

class TestLibraryManagement(unittest.TestCase):

    def setUp(self):
        """Initialize test objects before each test."""
        self.book = Book(book_id=1, title="Python Basics", author="John Doe", copies=3)
        self.ebook = Ebook(book_id=2, title="Advanced Python", author="Jane Smith", file_size=5)
        self.member = Member(member_id=1001, name="Alice")
        self.library = Library()
        self.library.add_book(self.book)
        self.library.add_book(self.ebook)
        self.library.members.append(self.member)

    def test_book_initialization(self):
        """Verify that a book is initialized correctly."""
        self.assertEqual(self.book.title, "Python Basics")
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.copies, 3)

    def test_ebook_initialization(self):
        """Verify that an e-book is initialized correctly."""
        self.assertEqual(self.ebook.title, "Advanced Python")
        self.assertEqual(self.ebook.file_size, 5)

    def test_member_borrow_book(self):
        """Check if a member can borrow a book."""
        self.member.borrow_book(self.book)
        self.assertIn("Python Basics", self.member.borrowed_books)
        self.assertEqual(self.book.copies, 2)

    def test_member_return_book(self):
        """Check if a member can return a book."""
        self.member.borrow_book(self.book)
        self.member.return_book(self.book)
        self.assertNotIn("Python Basics", self.member.borrowed_books)
        self.assertEqual(self.book.copies, 3)

    def test_library_add_duplicate_book(self):
        """Ensure duplicate book IDs are not added."""
        duplicate_book = Book(book_id=1, title="Duplicate Book", author="Author", copies=2)
        self.library.add_book(duplicate_book)
        self.assertEqual(len(self.library.books), 2)  # Should still be 2, not 3

if __name__ == "__main__":
    unittest.main()
