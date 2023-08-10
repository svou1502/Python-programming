import pyodbc

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

# Using WHERE with = 
sqlStr= " SELECT * FROM company WHERE company_no BETWEEN 0 AND 2000 "


conn = pyodbc.connect(connectionString)
cur = conn.cursor()
result = cur.execute(sqlStr).fetchall()
conn.close()

for row in result:
    print(row)
# Using WHERE with = 
sqlStr= " SELECT * FROM company WHERE company_no BETWEEN 100 and 200"


conn = pyodbc.connect(connectionString)
cur = conn.cursor()
result = cur.execute(sqlStr).fetchall()
conn.close()

for row in result:
    print(row)
