## Example of the parameterized constructor : 

class SwapValue:
    first = 0
    second = 0

	
 # parameterized constructor
    def __init__(self,f,s):
        self.first = f
        self.second = s
    
    def display(self):
        print("First Value = ",str(self.first))
        print("Second Value = ",str(self.second))
        
    def swap(self):
        print("Swapping the values")
        temp = self.first + self.second
        self.first = temp - self.first
        self.second = temp - self.second
        
# creating object of the class
# this will invoke parameterized constructor
obj = SwapValue(1000, 2000)

# display result
print("Values Before Swapping -\n",)
obj.display()

# perform Swapping of numbers
obj.swap()

# display result
print("Values After Swapping -\n")
obj.display()

# this will invoke parameterized constructor
obj2 = SwapValue(743, 347)

# display result
print("Values Before Swapping -\n")
obj2.display()

# perform Swapping of numbers
obj2.swap()

# display result
print("Values After Swapping -\n")
obj.display()
obj2.display()
print('Program End...')