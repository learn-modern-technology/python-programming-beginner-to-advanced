## All methods that use "self" inside a class are called Instance Methods
## It is called instance methods because we call it on Class instance
class Test:
    def instance_method(self):
        print(f"Called instance_method of {self}")
    
test = Test()   ## Prints nothing
test.instance_method()
Test.instance_method(test)
### Output of above instance_method calls
### Called instance_method of <__main__.Test object at 0x000001C9105BACE0>
### Called instance_method of <__main__.Test object at 0x000001C9105BACE0>

class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
        
    @classmethod        ## You want a method that uses class for something then we can use classmethod.
    def class_method(clss):
        print(f"Called class_method of {clss}")
        
    @staticmethod       ## A function inside the class that do not use it for anything. We can use statcimethod
    def static_method():
        print("Called Static Methods")
    
classtest = ClassTest()              
##ClassTest.instance_method()      ## TypeError: ClassTest.instance_method() missing 1 required positional argument: 'self'
ClassTest.instance_method(classtest)
ClassTest.class_method()         ## Python implicitly passes the self argument
ClassTest.static_method()
## Staticmethods are used to just place a method inside the class for code organizations.
## Classmethods are often used as factories.

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
        return Book(name, Book.TYPES[0], paper_weight + 100)        ## These inititates object using __init__ method of the same class
    
    @classmethod
    def paperback(cls, name, paper_weight):
        return Book(name, Book.TYPES[1], paper_weight)              ## These inititates object using __init__ method of the same class

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
