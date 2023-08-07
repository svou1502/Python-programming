#Added a while function to ensure input is between 1 and 100 
#otherwise the user needs to re-enter
while True:
    try:
        # Input the exam mark for a student
        mark = int(input("Enter the exam mark: "))
        
        # Check if the mark is within the valid range
        if mark < 1 or mark > 100:
            print("Error: Marks must be between 1 and 100.")
        else:
            # Input the student level
            level = int(input("Enter the student level (1 or 2): "))
            if level != 1 and level != 2:
                print("Invalid level. Please enter either 1 or 2.")
            else:
                # Calculate and display the grade based on the mark and level
                if level == 1:
                    if mark < 50:
                        grade = "The exam grade is Fail"
                    elif mark <= 60:
                        grade = "The exam grade is Pass"
                    elif mark <= 70:
                        grade = "The exam grade is Merit"
                    else:
                        grade = "The exam grade is Distinction"
                else:  # level == 2
                    if mark < 40:
                        grade = "The exam grade is Fail"
                    elif mark <= 50:
                        grade = "The exam grade is Pass"
                    elif mark <= 65:
                        grade = "The exam grade is Merit"
                    else:
                        grade = "The exam grade is Distinction"
                
                print("Grade:", grade)
                break  # Exit the loop after successful input and processing
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

