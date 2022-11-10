class TooManyPagesReadError(ValueError):  ## We need to inherit from the exception class
    pass

class Book:
    def __init__(self, name, pages_count):
        self.name = name
        self.pages_count = pages_count
        self.pages_read = 0
        
    def read(self, pages_rd):
        if self.pages_read + pages_rd > self.pages_count:
            raise TooManyPagesReadError(
                f"You have tried to read {self.pages_read + pages_rd} pages. But this book has only {self.pages_count} pages"
            )
        self.pages_read += pages_rd
        print(f"You have now read {self.pages_read} pages out of {self.pages_count}")
    
    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.pages_count}>"
        )

print("Welcome to the Book Read Tracker App")
bookstat = Book("Think and Grow Rich", 100)
try:
    bookstat.read(20)
    bookstat.read(40)
    bookstat.read(50)
except TooManyPagesReadError as e:
    print(e)
finally:
    print("Happy Reading ahead")
