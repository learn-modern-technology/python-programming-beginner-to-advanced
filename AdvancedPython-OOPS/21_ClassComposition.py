### Class Composition is a conterpart to inheritance that build out classes to use other classes
### We will be using very little Class Inheritance. But we will be using more of Class Composition.
### Composition allows your classes to be simpler and reduces the complexity of the code overall
class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity
    def __str__(self):
        return f"Bookshelf with {self.quantity} books"
shelf = Bookshelf(500)
print(shelf)

class Book(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name
    def __str__(self):
        ##super().__str__(self)
        return f"{self.name}"
        
book = Book("The Alchemist", 200)
print(book)

### why the above code breaks down is that we have a Book class which inherits from bookshelf
### but actually we are not using inside it anything about bookshelf, but just overwriting the bookshelf objects
### There is no reason to inherit if we are not going to use it any way.
### This is where a Composition come in.
### Composition is for - "A BookShelf has many Books"
### Instead of defining our book and bookshelf like this, we will define it little differently.
### Instead of defining a number of book in Bookshelf, we will allow a constructor to take in a number of books.

## This is an example of Class that composes of another classes
class Bookshelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"Bookshelf with {len(self.books)} books"

class Book:         ## No need to inherit Bookshelf or call super() class/method to invoke parent class
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"
    
book1 = Book("The Alchemist")
book2 = Book("Harry Potter")
shelf = Bookshelf(book1, book2)

print(shelf)