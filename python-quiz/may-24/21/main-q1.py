"""
What will be the output?
a) 'Python 101' by Michael Driscoll
b) Book object
c) Python 101
d) Error

"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("Python 101", "Michael Driscoll")
print(book)
