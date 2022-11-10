import os
import sys
import operator
os.path.dirname(sys.executable)
print(os.path.dirname(sys.executable))
print(sys.executable)
x = 20
y = 5
s = x + y
print('Sum of',x,'and',y,'is',s)
d = x-y
print ('Difference between',x,'and',y,'is',d)
p = x*y 
print ('Product of',x,'and',y,'is',p)
q = p/y
#print ('Quotient when ',p,'is divided by',y,'is',q)
print(f"Quotient when {p} is divided by {y} is {d}")
r = p%d
print ('Remainder when',p,'is divided by',d,'is',r)

print('Type of Variable r is',type(r))
print('Type of variable q is',type(q))
print('Type of variable p is',type(p))
print('Type of variable d is',type(d))
print('Type of variable s is',type(s))

# Python code to demonstrate working of
# add(), sub(), mul()

# Initializing variables
a = 4
b = 3

# using add() to add two numbers
print ("The addition of numbers is :",end="");
print (operator.add(a, b))

# using sub() to subtract two numbers
print ("The difference of numbers is :",end="");
print (operator.sub(a, b))

# using mul() to multiply two numbers
print ("The product of numbers is :",end="");
print (operator.mul(a, b))

# Python code to demonstrate working of
# truediv(), floordiv(), pow(), mod()
# Initializing variables
a = 5
b = 2

# using truediv() to divide two numbers
print ("The true division of numbers is : ",end="");
print (operator.truediv(a,b))

# using floordiv() to divide two numbers
print ("The floor division of numbers is : ",end="");
print (operator.floordiv(a,b))

# using pow() to exponentiate two numbers
print ("The exponentiation of numbers is : ",end="");
print (operator.pow(a,b))

# using mod() to take modulus of two numbers
print ("The modulus of numbers is : ",end="");
print (operator.mod(a,b))

# Python code to demonstrate working of
# gt(), ge() and ne()
# Initializing variables
a = 4
b = 3

# using gt() to check if a is greater than b
if (operator.gt(a,b)):
	print ("4 is greater than 3")
else : print ("4 is not greater than 3")

# using ge() to check if a is greater than or equal to b
if (operator.ge(a,b)):
	print ("4 is greater than or equal to 3")
else : print ("4 is not greater than or equal to 3")

# using ne() to check if a is not equal to b
if (operator.ne(a,b)):
	print ("4 is not equal to 3")
else : print ("4 is equal to 3")


# Python code to demonstrate working of
# lt(), le() and eq()
# Initializing variables
a = 3
b = 3

# using lt() to check if a is less than b
if(operator.lt(a,b)):
	print ("3 is less than 3")
else : print ("3 is not less than 3")

# using le() to check if a is less than or equal to b
if(operator.le(a,b)):
	print ("3 is less than or equal to 3")
else : print ("3 is not less than or equal to 3")

# using eq() to check if a is equal to b
if (operator.eq(a,b)):
	print ("3 is equal to 3")
else : print ("3 is not equal to 3")

user_input1 = float(input("Please enter a number: "))
print('user_input1 is',user_input1)

user_input2 = int(input("Please enter a number: "))
print('user_input2 is',user_input2)

user_input3 = int(input("Please enter a number: "))
print('user_input3 is',user_input3)

total = user_input1 + user_input2 + user_input3
print(f"Total is -{total:.3f}")

print(f"user_input1 is {user_input1:.2f}, user_input2 is {user_input2} and user_input3 is {user_input3}")