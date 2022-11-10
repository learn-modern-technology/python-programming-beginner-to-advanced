class Student:
    def __init__(self):
        self.name = "Mohan Kandasamy"
        self.grades = (88,73,92,96,97)
    
    def average(self):
        return sum(self.grades)/ len(self.grades)
    
    def display(self):
        print(f"name - {self.name}")
        print(f"grades - {self.grades}")
    

student = Student()
student.display()
avg = student.average()
print(f"Average is {avg}")
print(student.name)
print(student.grades)