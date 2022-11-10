class Student:
    def __init__(self,name, *grades):           ### -- Remember *args ? --
        self.name = name
        self.grades = grades
    
    def average_grades(self):
        return sum(self.grades)/ len(self.grades)
    
    def display(self):
        print(f"name - {self.name}")
        print(f"grades - {self.grades}")
    

student = Student("Mahak", 100,97,92,95,95)
student.display()
avg = student.average_grades()
print(f"Average is {avg}")
print(student.name)
print(student.grades)

student2 = Student("Rameshwar",88,73,92,96,97)
student2.display()
avg = student2.average_grades()
print(f"Average is {avg}")
print(student2.name)
print(student2.grades)

