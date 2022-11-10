import os
import sys
os.path.dirname(sys.executable)

print(os.path.dirname(sys.executable))
print(sys.executable)

# var1, var2, var3, var4, var5, var6 = "There ", "is ", "no ", "substitute ", "for ", "hardwork "
# 
# print('var1-',var1)
# print('var2-',var2)
# print('var3-',var3)
# print('var4-',var4)
# print('var5-',var5)
# print('var6-',var6)
# 
# user_name=input('Please enter your name:')
# print(var1 + var2 + var3+ var4 + var5+ var6, user_name +'!!!')
# 
# user_input1 = float(input("Please enter a number: "))
# print('user_input1 is',user_input1)
# 
# user_input2 = int(input("Please enter a number: "))
# print('user_input2 is',user_input2)
# 
# user_input3 = int(input("Please enter a number: "))
# print('user_input3 is',user_input3)
# 
# total = user_input1 + user_input2 + user_input3
# print("Total is -",total)
# 
# print(f"user_input1 is {user_input1}, user_input2 is {user_input2} and user_input3 is {user_input3}")
# print(f"user_input1 is {user_input1:.2f}, user_input2 is {user_input2} and user_input3 is {user_input3}")

name = input("Enter your name")
print(f'Hello, {name}')

user_age = input("Enter your Age in years")
years = int(user_age)
months = years * 12
print(f"Your age, {years} years, is equal to {months} months")