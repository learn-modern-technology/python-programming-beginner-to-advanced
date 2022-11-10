from collections import namedtuple
import collections
simpleList = ("red", "green", "blue", 4, 5, 6)  # This is a tupple
print(simpleList)
print(type(simpleList))

simpleList = ["red", "green", "blue", 4, 5, 6]
print(simpleList)
print(type(simpleList))

# Python code to demonstrate namedtuple()
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Tapas', '30', '21121991')

print("Type of variable S is",type(S))

# Access using index
print("The Student info using index is : ", end="")
print(S[0],S[1],S[2])

# Access using name
print("The Student info using keyname is : ", end="")
print(S.name, S.age, S.DOB)

# Access using getattr()
print("The Student info using getattr() is : ", end="")
print(getattr(S,'name'),getattr(S, 'age'),getattr(S, 'DOB'))

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)
  
# ._replace returns a new namedtuple, it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Somil Saxena'))
S1 = S._replace(name='Somil Saxena')
# original namedtuple
print("The Student S info-",S)
print("The Student S1 info-",S1)