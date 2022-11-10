import os
import sys
os.path.dirname(sys.executable)

print(os.path.dirname(sys.executable))
print(sys.executable)

raj_marks = [88,92,95,96,73]
ram_marks = [92,92,95,95,80]
subject_list =["Computer Science",'Physics','Maths','Science','English']

print("1. Marks of Raj is -",raj_marks)
print("2. Marks of Raj is -",raj_marks[:2],'and',raj_marks[2:])
print("1. Marks of Ram is -",ram_marks)
print("2. Marks of Ram is -",ram_marks[:])
##print("3. Marks of Ram is -",ram_marks[]) ##SyntaxError: invalid syntax. Perhaps you forgot a comma?

print("List of Subjects is-",subject_list)
print('Science Marks of Raj is',raj_marks[3],'and Ram is',ram_marks[3])
print('English Marks of Raj is',raj_marks[-1],'and Ram is',ram_marks[-1])

##ram_sumofmarks = + ram_marks ##TypeError: bad operand type for unary +: 'list'
##ram_sumofmarks = + ram_marks[:] ##TypeError: bad operand type for unary +: 'list'
##print("Sum of Marks for Ram is-",ram_sumofmarks)

# for x in ram_marks:
#     print('Marks for Ram is-',x)

total_ram_marks = 0
for i in range(0, len(ram_marks)):
    total_ram_marks = total_ram_marks + ram_marks[i]

print("Sum of Marks for Ram is- ",total_ram_marks)
print("Average of Marks for Ram is- ",total_ram_marks/len(ram_marks))

total_raj_marks = 0
for j in range(0, len(raj_marks)):
    total_raj_marks = total_raj_marks + raj_marks[j]

print("Sum of Marks for Raj is- ",total_raj_marks)
print("Average of Marks for Raj is- ",total_raj_marks/len(raj_marks))

##dummy_marks = [92,92,95,95,,]       ##SyntaxError: invalid syntax
dummy_marks = [92,92,95,95,]
print("Dummy Marks is- ",dummy_marks)
## print("Dummy Marks is- ",dummy_marks[4])  ##IndexError: list index out of range
print("Dummy Marks is- ",dummy_marks[3])

dummy_marks = ram_marks
print("Dummy Marks is- ",dummy_marks)

dummy_marks2 = ram_marks[:2]
print("Dummy Marks2 is- ",dummy_marks2)

dummy_subject= subject_list[:]
print("Dummy Subject is- ",dummy_subject)

dummy3_marks = ram_marks + raj_marks
print("Dummy Marks3 is- ",dummy3_marks)

dummy_marks4 = ram_marks[1:3] + raj_marks
print("Dummy Marks4 is- ",dummy_marks4)

ram_marks[1:3] += raj_marks
print("Ram Marks is- ",ram_marks)

