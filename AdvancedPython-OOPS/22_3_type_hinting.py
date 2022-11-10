## Type hinting is available in python 3.5 and above
### Hinting will help us identify the errors before running the python interpretor 
from typing import List  ## can also import Tupple, Set

class Book:
    def __init__(self, name:str):
        self.name = name
    def __str__(self):
        return f"Book - {self.name}"

class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books
    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."



# Key benefit is now you'll get told if you pass in the wrong thing...
## Suggests this is incorrect if you have a tool that will analyse your code (e.g. PyCharm or Pylint)
##book = Book("Harry Potter", "352")  
books1 = Book("Harry Potter")
books2 = Book("The Alchemist")
books3 = Book("Think and grow Rich")
print(books1)
print(books2)
print(books3)
shelf = BookShelf([books1, books2, books3])
## Suggests this is incorrect too
##Type hinting is that: hints. It doesn't stop your code from working... although it can save you at times!
## -- Hinting the current object --
print(shelf)