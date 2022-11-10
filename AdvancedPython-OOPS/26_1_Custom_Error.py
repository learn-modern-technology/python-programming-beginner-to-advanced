class Book:
    def __init__(self, name, pages_count):
        self.name = name
        self.pages_count = pages_count
        self.pages_read = 0
        
    def read(self, pages_rd):
        self.pages_read += pages_rd
        print(f"You have now read {self.pages_read} pages out of {self.pages_count}")
    
    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.pages_count}>"
        )

bookstat = Book("Think and Grow Rich", 100)
bookstat.read(20)
bookstat.read(40)
bookstat.read(50)       ## This is not possible. We should add an Exception over here

