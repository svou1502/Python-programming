import pyodbc

connectionString= r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=northwind;Trusted_Connection=yes'

# Read rows with a filter

sqlStr= " SELECT * FROM customers"

conn = pyodbc.connect(connectionString)
cur = conn.cursor()
result = cur.execute(sqlStr).fetchall()
conn.close()

for row in result:
    print(row)
