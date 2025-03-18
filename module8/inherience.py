# parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# child class inheriting from parent class
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def __str__(self):
        return self.title + " by " + self.author

class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size # in MB

    def get_file_size(self):
        return f"{self.file_size} MB"

if __name__ == "__main__":
    my_book = Ebook("The Great Gatsby", "F. Scott Fitzgerald", 10)
    print(my_book.get_title())
    print(my_book.get_author())
    print(my_book.get_file_size())
    print(my_book)