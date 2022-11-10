import os
import sys

num_list4 = [(x,y) for x in range(2,6) for y in ["python", "is", "interesting"]]
print('num_list4',num_list4)

look_up =[1, 2, 3, 4, 5]
num_list5 = [(a,b) for a in range(5) for b in look_up]
print('num_list5-',num_list5)

num_list6 = [(a,b) for a in range(5) for b in look_up if a==b]
print('num_list6-',num_list6)

num_list7 = [(a,b) for a in range(5) for b in look_up if a<b]
print('num_list7-',num_list7)

num_list8 = [1,2,3,4,5,6,7,8,9,10]
even_list = [x for x in num_list8 if x%2==0]
print('even_list', even_list)

odd_list = [x for x in num_list8 if x%2!=0]
print('odd_list', odd_list)

sqr_odd_list = [x**2 for x in num_list8 if x%2!=0]
print('sqr_odd_list',sqr_odd_list)

cube_odd_list = [x**3 for x in num_list8 if x%2!=0]
print('cube_odd_list',cube_odd_list)

a = 50
b = 20
# checking only if statement
if b > a:
 print("b is greater than a")

#checking if else statement
a = 20
b = 30
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")

a = 30
b = 30
#checking if elif else statement
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
