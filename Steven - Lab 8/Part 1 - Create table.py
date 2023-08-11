import pyodbc

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

sqlStr = """CREATE TABLE Student (
    StudentID INT NOT NULL,
    FirstName nvarchar(40) NOT NULL,
    Surname nvarchar(30) NULL,
    Course nvarchar(30) NULL,
    City nvarchar(15) NULL)"""

conn = pyodbc.connect(connectionString)
cur = conn.cursor()
cur.execute(sqlStr)

conn.commit() 
conn.close()

sqlStr="""
IF EXISTS(
    SELECT TABLE_NAME, TABLE_SCHEMA
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'Student'
    AND TABLE_SCHEMA = 'dbo')
BEGIN
    DROP TABLE Student
END"""
