# Input the exam mark for a student
mark = int(input("Enter the exam mark for the student: "))

# Check if the mark is within the valid range
if mark < 1 or mark > 100:
    print("Error: Marks must be between 1 and 100.")
else:
    # Calculate and display the grade based on the mark
    if mark < 50:
        grade = "The exam grade is a Fail"
    elif mark <= 60:
        grade = "The exam grade is a Pass"
    elif mark <= 70:
        grade = "The exam grade is a Merit"
    else:
        grade = "The exam grade is a Distinction"
    
    print("Grade:", grade)
    
