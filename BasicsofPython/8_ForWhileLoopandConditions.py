import os
import sys
import secrets
os.path.dirname(sys.executable)

print(os.path.dirname(sys.executable))
print(sys.executable)

num_list1 = []
for x in range(10):
    num_list1.append(secrets.randbelow(100))

print('Value of x -',x)
print('NumList1 -',num_list1)
print('Length of NumList1 -',len(num_list1))

num_list2 = [secrets.randbelow(300) for y in range(10)]
##print('Value of y-',y) ##NameError: name 'y' is not defined
print('num_list2 -',num_list2)
print('Length of num_list2 -',len(num_list2))

for index, elements in enumerate(num_list1):
    print(index,elements)

num_list3 = list(range(15))
print('num_list3-', num_list3)

num_list4 = list(range(10,20))
print('num_list4-', num_list4)

# Prints all letters except 'e' and 's'
# Python Continue Statement returns the control to the beginning of the loop
i = 0
a = 'geeksforgeeks'

while i < len(a):
	if a[i] == 'e' or a[i] == 's':
		i += 1
		continue
	print('Current Letter :', a[i])
	i += 1


# Python program to demonstrate while-else loop
# Python Break Statement brings control out of the loop.
# while loop executes the block until a condition is satisfied. 
# When the condition becomes false, the statement immediately after the loop is executed. 
# The else clause is only executed when your while condition becomes false. 
# If you break out of the loop, or if an exception is raised, it won’t be executed
i = 0
while i < 4:
	i += 1
	print(i)
else: # Executed because no break in for
	print("No Break\n")

i = 0
while i < 4:
	i += 1
	print(i)
	break
else: # Not executed as there is a break
	print("No Break")

# loop break statement example in python
print("break statement example")
colors = ["red", "green", "blue"]
for x in colors:
    if(x == "green"):
        break
    print(x)

#loop continue statement example in python
print("continue statemet example")
colors = ["red", "green", "blue"]
for x in colors:
    if(x == "green"):
        continue
    print(x)

# else block loop example in python
print("else block example")
colors = ["red", "green", "blue"]
for x in colors:
    if(x == "green"):
      continue
else:
    print("All Items processed")
    
print("\nelse block example")
colors = ["red", "green", "blue"]
for x in colors:
    print(x)
else:
    print("All Items processed")
    
