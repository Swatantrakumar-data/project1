from Catalog import Catalog
from Book import Book
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Member(User):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    # assume name is unique
    def issueBook(self, name, isbn, days=10):
        book = Catalog.searchByName(name)
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)


    # assume name is unique
    def returnBook(self, name, isbn, rack):
        book = Catalog.searchByName(name)
        book.addBookItem(isbn,rack)

class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name + self.location + self.emp_id
    def addBook(self, name, author, publish_date, pages):
        b=Book(name,author,publish_date,pages)
        Catalog.books.append(b)
        Catalog.different_book_count += 1
        return b


    def removeBook(self, name):
        book = Catalog.searchByName(name)
        book.removeBookItem(book)

    def removeBookItemFromCatalog(self, book, isbn):
        book_item = book.searchBookItem(isbn)
        book.removeBookItem(book_item)