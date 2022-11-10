# python3 code to understand the difference between == and is operator
import os
import sys

list1 = []
list2 = []
list3=list1

print(id(list1))
print(id(list2))
print(id(list3))

if (list1 == list2):
	print("True")
else:
	print("False")

if (list1 is list2):
	print("True")
else:
	print("False")

if (list1 is list3):
	print("True")
else:	
	print("False")

list3 = list3 + list2

if (list1 is list3):
	print("True")
else:	
	print("False")

# -- Comparisons --

print(100 == 10)
print (100 != 10)
print(5 >= 5)  # False
print(10 == 10)  # False

# Comparisons: ==, !=, >, <, >=, <=

# -- is --
# Python also has the `is` keyword. It's a confusing keyword for now, so I don't recommend using it.

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

foreign = abroad

print(friends == abroad)  # True
print(friends is abroad)  # False
print(foreign is abroad)  # True