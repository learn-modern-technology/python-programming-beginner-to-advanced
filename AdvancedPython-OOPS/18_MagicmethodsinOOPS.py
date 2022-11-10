# class Student:
#     def __init__(self,name, age):           
#         self.name = name
#         self.age = age
#     
#     
# student = Student("Mahak", 26)
# print(student)      

## Output will be object 
#<__main__.Student object at 0x00000251D0B17D60>



# class Student:
#     def __init__(self,name, age):           ### -- Remember *args ? --
#         self.name = name
#         self.age = age
#     
#     #def __str__(self):
#     #    pass            # ypeError: __str__ returned non-string (type NoneType)
# -- __str__ --
###The goal of __str__ is to return a nice, easy to read string for end users.
## 
#     def __str__(self):
#         #return "Hello"      # return Hello
#         #return self         #TypeError: __str__ returned non-string (type Student)
#         return f"Student {self.name}, is {self.age} years old"
#     
#     def __repr__(self) -> str:
#         return f"<Student({self.name}, {self.age})>"
#         
# student = Student("Mahak", 28)
# print(student)      ## Prints output of __str__ methods

###The goal of __repr__ is to be unambiguous, and if possible what it outputs should allow us to re-create an identical object.
class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
#
## Adding the < > just so it's clear that this is an object we're printing out!    
    def __repr__(self):
        return f"<Student('{self.name}', {self.age})>"
        
student = Student("Mahak", 28)
print(student)      ## Prints output of repr methods