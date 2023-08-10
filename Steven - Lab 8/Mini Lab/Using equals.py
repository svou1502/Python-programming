import pyodbc

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

# Using WHERE with = 
sqlStr= " SELECT * FROM company WHERE county='London'"


conn = pyodbc.connect(connectionString)
cur = conn.cursor()
result = cur.execute(sqlStr).fetchall()
conn.close()

for row in result:
    print(row)
