## Example of the parameterized constructor : 

class SwapValue:
    first = 0
    second = 0

	
 # parameterized constructor
    def __init__(self,f,s):
        self.first = f
        self.second = s
        
    def __del__(self):
        print("Deleting Destructor")
    
    def display(self):
        print("First Value = ",str(self.first))
        print("Second Value = ",str(self.second))
        
    def swap(self):
        print("\nSwapping the values")
        temp = self.first + self.second
        self.first = temp - self.first
        self.second = temp - self.second
        
# creating object of the class
# this will invoke parameterized constructor
obj = SwapValue(1000, 2000)

print("\nValues Before Swapping -")
obj.display()

# perform Swapping of numbers
obj.swap()

# display result
print("Values After Swapping -")
obj.display()

# this will invoke parameterized constructor
obj2 = SwapValue(743, 347)

# display result
print("\nValues Before Swapping -")
obj2.display()

# perform Swapping of numbers
obj2.swap()

# display result
print("Values After Swapping -")
obj2.display()
obj.display()
print('Program End...')