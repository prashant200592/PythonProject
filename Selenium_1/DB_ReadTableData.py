# Install mysql-connector-python
import mysql.connector

search_query = "SELECT * FROM calfd;"

try:
    con = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="cde3$RFV", database="mydb")
    curs = con.cursor()
    curs.execute(search_query)
    for row in curs:
        print(row[0], row[1], row[2], row[3], row[4], row[5])
    #con.commit()
    con.close()
except:
    print("Connection Unsuccessful :(")

print("Finished...")