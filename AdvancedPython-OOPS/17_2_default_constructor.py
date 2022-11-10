#In Python the __init__() method is called the constructor and is always called when an object is created

#Example of default constructor:

class GeekforGeeks:
	
 # default constructor
	def __init__(self):
		self.name = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.name)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()
