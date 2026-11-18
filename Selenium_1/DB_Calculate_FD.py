# Install mysql-connector-python
import mysql.connector

search_query = "SELECT * FROM calfd;"

try:
    con = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="cde3$RFV", database="mydb")
    curs = con.cursor()
    curs.execute(search_query)
    for row in curs:
        principal = row[0]
        #print(principal, end=" ")
        rateOfInterest = row[1]
        per1 = row[2]
        per2 = row[3]
        frequency = row[4]
        cal_mvalue = row[5]



    con.close()
except:
    print("Connection Unsuccessful :(")

print("Finished...")