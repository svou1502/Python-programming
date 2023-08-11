from sqlite3 import Row
import pyodbc

def showCompany():
    connectionString= r'DRIVER={ODBC Driver 13 for SQL Server}; SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'

    try:
        conn = pyodbc.connect(connectionString)
        cur = conn.cursor()
        result = cur.execute('SELECT * FROM companys').fetchall()
        conn.close()
        return result
    except:
        return None

    #----Main----

    rows = showCompany()
    if rows != None:
        for row in rows:
            print(row)
        else:
            print('Error reading data.')


