# Basic Dictionaries
friend_ages = {"Rohit": 29, "Rosberry": 30, "Anjali": 27}
friend_ages["Mahesh"] = 30

print("friend_ages",friend_ages)

print(friend_ages["Rosberry"])

# -- List of dictionaries --
friends = [
    {"name": "Ronnie Singh", "age": 24},
    {"name": "Adam Zampa", "age": 30},
    {"name": "Anant Singh", "age": 27},
    {"name": "Anjali Pandey", "age": 29},
]

print("friends", friends)

#print("friends", friends[0])
#print("friends", friends[1])
#print("friends", friends[2])
#print("friends", friends[3])

print("friends", friends[0]["name"],friends[0]["age"])
print("friends", friends[1]["name"],friends[1]["age"])
print("friends", friends[2]["name"],friends[2]["age"])
print("friends", friends[3]["name"],friends[3]["age"])

# -- Iteration --
student_attendance = {"Rohit": 85, "Rosberry": 90, "Anjali": 95, "Ronnie": 100}

#for student in student_attendance:
#    print(f"{student}: {student_attendance[student]}")

#for x in student_attendance:
#    print(x)
#for x in student_attendance:
#    print(f"{x} : {student_attendance[x]}")

# Better
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

studentf="Anjali"
# -- Using the `in` keyword --
if studentf in student_attendance:
    print(f"{studentf}: {student_attendance[studentf]}")
else:
    print("f {studentf} isn't a student in this class!")

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print("Average Attendance in %",sum(attendace_values)/len(attendace_values))