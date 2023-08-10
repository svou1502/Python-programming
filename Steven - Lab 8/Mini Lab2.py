import pyodbc

def dbfunctionquery(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    result = cur.execute(statement).fetchall()
    conn.close()
    return result

def dbinsert(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
        cur.execute(statement)
        conn.commit()  # Commit changes after successful execution
        print("Company inserted successfully.")
    except:
        conn.rollback()  # Rollback changes if there's an error
        print('Error: Cannot insert the company for some reason')
    conn.close()

def dbupdate(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
        cur.execute(statement)
        conn.commit()  # Commit changes after successful execution
        print("Update executed successfully.")
    except:
        conn.rollback()  # Rollback changes if there's an error
        print('Error: Cannot execute update for some reason')
    conn.close()

def dbdelete(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
        cur.execute(statement)
        conn.commit()  # Commit changes after successful execution
        print("Delete executed successfully.")
    except:
        conn.rollback()  # Rollback changes if there's an error
        print('Error: Cannot execute delete for some reason')
    conn.close()

#Insert a new company
insert_query = """
INSERT INTO company (company_no, company_name, tel, county, post_code)
VALUES (5555, 'QA', '01234 567890', 'London', 'W1 1AA')
"""

dbinsert(insert_query)



#Update companies in 'London' to 'West London'

update_query = """
UPDATE company
SET county = 'West London'
WHERE county = 'London'
"""

dbupdate(update_query)


# Delete 'Inge' from the salesperson table

delete_query = """
DELETE FROM salesperson
WHERE salesperson = 'Inge'
"""

dbdelete(delete_query)

select_query = "SELECT * FROM company"
rows = dbfunctionquery(select_query)
for row in rows:
    print(row)


