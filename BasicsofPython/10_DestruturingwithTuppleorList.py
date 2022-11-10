# Destruturing is where we take collections like List or Tuple and break it into individual values
a = (5,11)  # Tupple
b = 5, 11  # Tuple
c = 5, "Arun", 12, "Vishnu"   # Tuple
x, y = (5, 11)
z = [(1,2), (3,4), (5,6)]      # Tuple inside a list
print(f"a = {type(a)}")
print(f"b = {type(b)}")
print(f"c = {type(c)}")
print(f"x= {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")
print(f"z[0] = {type(z[0])}")

student_attendance = {"Rohit": 85, "Rosberry": 90, "Anjali": 95, "Ronnie": 100}

print(f"student_attendance -> {list(student_attendance)}")
print(f"student_attendance -> {list(student_attendance.items())}")  # List of Tupples

## This is the programm for destruturing the List of Tupples
for student, attendance in list(student_attendance.items()):
    print(f"{student}: {attendance}")

people = [("Maheshwar", "Mechanic", 29), ("Vigneshwar", "Artist", 35), ("Rajkumar", "SoftwareEngineer", 38)]

for name, profession, age in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


## Not a good way to do it
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")
    
person = ("Mike",28,"Engineer")
name, _, profession = person        ## we use _ as variable if we want to ignore that value
print(name,profession);

head, *tail = [1,2,3,4,5,6,7]
print(f"head- {head}")
print(f"tail- {tail}")

*head, tail = [1,2,3,4,5,6,7]
print(f"head- {head}")
print(f"tail- {tail}")