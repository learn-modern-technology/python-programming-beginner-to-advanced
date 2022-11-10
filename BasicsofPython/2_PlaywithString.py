from operator import length_hint
import os
import sys
os.path.dirname(sys.executable)

print(os.path.dirname(sys.executable))
print(sys.executable)

str1 ='My name is Turam Viswas'
str2 ="I love to be invovled in Gossips"
str3 = str1 + str2
print('Type of str1 -',type(str1),'str1 is-',str1)
print('Type of str2 -',type(str2),'str2 is-',str2)
print('Type of str3 -',type(str3),'str3 is-',str3)
str4 = str1 + ' '+ str2
print('Type of str4 -',type(str4),'str4 is-',str4)

## str1 ="My name is Turam Viswas"
## str2 ="I love to be invovled in Gossips"
## str3 = str1 + str2
## print('Type of str1 -',type(str1),'str1 is-',str1)
## print('Type of str2 -',type(str2),'str2 is-',str2)
## print('Type of str3 -',type(str3),'str3 is-',str3)
## str4 = str1 + " " + str2
## print('Type of str4 -',type(str4),'str4 is-',str4)

##str5 = str1 + 2  ##TypeError: can only concatenate str (not "int") to str
str5 = str1 * 2
print('Type of str5 -',type(str5),'str5 is-',str5)

str6 = 2 * str1
print('Type of str6 -',type(str6),'str6 is-',str6)

##str7 = str2 * str1  ##TypeError: can't multiply sequence by non-int of type 'str'
##print('Type of str7 -',type(str7),'str7 is-',str7)

print("Length of String1 is",length_hint(str1))
print("Length of String2 is",length_hint(str2))
print("Length of String3 is",length_hint(str3))
print("Length of String4 is",length_hint(str4))
print("Length of String5 is",length_hint(str5))
print("Length of String6 is",length_hint(str6))

## print("5th Character in String1",str1[4])
## print("Modified String1",str1[:4])
## print("Modified String1",str1[:3])
## print("Modified String1",str1[3:])
## print("Modified String1",str1[3:6])

print("Modified String1",str1[3:7])
print("Modified String1",str1[-1:])
print("Modified String1",str1[-12:])
print("Modified String1",str1[:12])
print("Modified String1",str1[:-12])

name = 'Sudharshan Chakraborty'
str7 ='My name is Hemant Badani'
print('str7 is - ', str7)

str7 =f"My name is {name}"
print('str7 is - ', str7)
name = 'Sudhakar Prasad'
print('str7 is - ', str7)
print('str7 is - ', f"My name is {name}")

str8 = "My name is {}"
with_name= str8.format(name)
print("with_name - ",with_name)

str9 = "My name is {}"
with_name_two= str8.format("Ankita Kumari")
print("with_name_two- ",with_name)

long_phrase = "Hello, {}!! Today is {}"
with_input=long_phrase.format("Mohit Kumar", "Sunday")
print("With input-", with_input)