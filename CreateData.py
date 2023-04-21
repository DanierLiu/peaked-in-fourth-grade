import mysql.connector
import random

# Create a connection to the MySQL server
cnx = mysql.connector.connect(host='localhost', password='CHANGE_ME', user='CHANGE_ME', database='CHANGE_ME')

  # Create a cursor to execute SQL statements
cursor = cnx.cursor()

cafeNum = 1000001

for i in range(1,200):
  numOfTables = random.randint(20,50)
  numOfSeats = random.randint(50,1000)
  numOfStaff = random.randint(5,20)
  query = f"INSERT INTO cafeteria (CafeteriaNum, NumOfTables, NumOfSeats, NumOfStaff) VALUES ({cafeNum}, {numOfTables}, {numOfSeats}, {numOfStaff});"
  cursor.execute(query)
  cafeNum += 1

cnx.commit()

cnx.close()