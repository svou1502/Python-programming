import pyodbc
import csv

# Connection string
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

# Student record
student_data = [
    (1, 'Steven', 'V', 'Coding Fundamentals', 'London'),
    (2, 'Caleb', 'NA', 'Coding Fundamentals', 'NA'),
    (3, 'Eloise', 'NA', 'Coding Fundamentals', 'NA'),
    (4, 'Costi', 'NA', 'Coding Fundamentals', 'NA'),
    (5, 'Eoin', 'Davies', 'Coding Fundamentals', '?'),
    (6, 'Jack', 'Taylor', 'Coding Fundamentals', '?'),
    (7, 'Nancy', '?', 'Coding Fundamentals', '?')
]

# Insert records into CSV file
csv_filename = 'students.csv'
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['StudentID', 'FirstName', 'Surname', 'Course', 'City'])
    writer.writerows(student_data)

# Connect to the database
conn = pyodbc.connect(connectionString)
cur = conn.cursor()

# Read data from CSV file and insert into the database
with open(csv_filename, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cur.execute(
            "INSERT INTO Student (StudentID, FirstName, Surname, Course, City) "
            "VALUES (?, ?, ?, ?, ?)",
            row['StudentID'], row['FirstName'], row['Surname'], row['Course'], row['City']
        )

# Commit and close connection
conn.commit()
conn.close()

print("Data inserted into the database.")

# Now you can check the records using your Database Management Studio.

