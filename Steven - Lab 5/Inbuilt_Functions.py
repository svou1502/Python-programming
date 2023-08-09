import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
grades = data.split(',')

# Calculate and display minimum and maximum values
min_grade = min(grades)
max_grade = max(grades)

print("Grades:", grades)
print("Minimum grade:", min_grade)
print("Maximum grade:", max_grade)

# Min is 100 (?), max is 99?  The data is being read as strings
# Use map function to convert strings to integer

# Part 2

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
grades = data.split(',')

# Use map() to convert strings to integers
grades = list(map(int, grades))

# Calculate and display minimum and maximum values
min_grade = min(grades)
max_grade = max(grades)

print("Grades:", grades)
print("Minimum grade:", min_grade)
print("Maximum grade:", max_grade)

# Display the average of grades to two decimal points
average_grade = sum(grades) / len(grades)  # Calculate the average
average_grade = round(average_grade, 2)     # Round to two decimal points

print("The average grade is: ", average_grade)

# Using the statistics function, needs to be placed at the first line of code

average = statistics.mean(grades)

print("The average grade using the statistics library is: ", round(statistics.mean(grades), 2))

median = statistics.median(grades)

print("The median grade using the statistics library is: ", median)

