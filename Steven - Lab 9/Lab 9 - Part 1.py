class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances of the Student class
student1 = Student("Costi", 25)
student2 = Student("Eloise", 26)

# Getting the age of one of the students
age_of_student1 = student1.age
print(f"{student1.name}'s age is {age_of_student1} years.")

