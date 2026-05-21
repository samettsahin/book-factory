import random


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


def generate_random_book():
    titles = ["1984", "Dune", "Foundation", "The Hobbit"]
    authors = ["George Orwell", "Frank Herbert", "Isaac Asimov", "J.R.R. Tolkien"]

    return Book(
        random.choice(titles),
        random.choice(authors),
        random.randint(1950, 2025)
    )


book = generate_random_book()
print(book)