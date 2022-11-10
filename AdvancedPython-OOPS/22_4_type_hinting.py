## Use 19_2_ClassMethods using type hinting
class Book:
    TYPES = ("Hardcover", "Paperback")
    
    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name: str, weight: int) -> "Book":
        return cls(name, cls.TYPES[0], weight + 100)
    
    @classmethod
    def paperback(cls, name: str, weight: int) -> "Book":
        return cls(name, cls.TYPES[1], weight)
    

hardcoverbook = Book.hardcover("Harry Potter ",1500)        ## To initialize the object using classmethods 
print(f"With Classmethod - {hardcoverbook}")                ##

paperbackbook = Book.paperback("The Alchemist ",1500)        ## To initialize the object using classmethods 
print(f"With Classmethod - {paperbackbook}")  