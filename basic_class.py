# Description: Define a class Book with attributes year_published
# like title, author, and Include a method display_info() that prints the book details.

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def display_info(self):
        print(f"Title: {self.title}, written by: {self.author}, year: {self.year_published}")

if __name__ == "__main__":
    book1 = Book("Animal Farm", "George Orwell", "1930")
    book2 = Book("The Road to Bar Beach", "Sam Eyo", "1986")

    book1.display_info()
    book2.display_info()