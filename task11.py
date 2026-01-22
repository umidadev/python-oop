class Book:
    def __init__(self, title, author, is_read = False):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True
        print("Kitob o\'qilgan deb belgilandi")

    def status(self):
        if self.is_read:
            print("O\'qilgan")
        else:
            print("O\'qilmagan")


book1 = Book("Python Basics", "John Doe")
book2 = Book("Clean Code", "Robert Martin")

print(book1.title, end=": ")
book1.status()

book1.mark_as_read()

print(book1.title, end=": ")
book1.status()

print(book2.title, end=": ")
book2.status()
