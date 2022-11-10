## Classmethods are often used as factories.
## In a class as well as methods, we can put variables and these become class properties.

class Book:
    TYPES = ("hardcover","paperback")

    def __init__(self, name, book_type, weight):
        self.name=name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self):
        return f"<Book Details: {self.name}, {self.book_type}, weight {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, paper_weight):
        return cls(name, Book.TYPES[0], paper_weight + 100)        ## These inititates object using __init__ method of the same class
    
    @classmethod
    def paperback(cls, name, paper_weight):
        return cls(name, Book.TYPES[1], paper_weight)              ## These inititates object using __init__ method of the same class

print(Book.TYPES)
book = Book("The Alchemist","paperback", 1400)      ## We are using the __reper__ method to print it 
print(f"Without Classmethod - {book}")

###How to use factories ?? 
###Eg- We have 2 book types and we want to allow only these 2 book_types to take in name and page weight and 
###will return book as name , book type and paper weight
hardcoverbook = Book.hardcover("Harry Potter ",1500)        ## To initialize the object using classmethods 
print(f"With Classmethod - {hardcoverbook}")                ##

paperbackbook = Book.paperback("Harry Potter ",1500)        ## To initialize the object using classmethods 
print(f"With Classmethod - {paperbackbook}")                ##
