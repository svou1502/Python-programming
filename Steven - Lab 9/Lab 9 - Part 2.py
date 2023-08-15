import statistics # Importing the statistics module

class Student:
    def __init__(self, name, age, current_class):
        self.name = name
        self.age = age
        self.current_class = current_class # Modified to except the students current class
        self.test_scores = [] # Created attribute to work out test scores

    def add_test_scores(self, score1, score2, score3):
        self.test_scores = [score1, score2, score3]

    def calculate_average_score(self):
        average_score = statistics.mean(self.test_scores)
        return average_score

# Creating instances of the Student's info
student1 = Student("Costi", 20, "Computer Science")
student2 = Student("Eloise", 22, "Advanced Computer Science")

# Adding test scores and calculating average for student1
student1.add_test_scores(85, 90, 78)
average_score_student1 = student1.calculate_average_score()

# Adding test scores and calculating average for student2
student2.add_test_scores(55, 58, 45)
average_score_student2 = student2.calculate_average_score()

# Displaying results
print(f"{student1.name}'s average test score: {average_score_student1:.2f}")
print(f"{student2.name}'s average test score: {average_score_student2:.2f}")

