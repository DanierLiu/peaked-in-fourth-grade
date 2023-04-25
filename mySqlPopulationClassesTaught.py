import mysql.connector
import random

# Connect to the SQL server and create a cursor
cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='elementaryschool')
cursor = cnx.cursor()

# Retrieve the list of existing classroom numbers from the Classroom table
cursor.execute("SELECT ClassroomNum FROM Classroom")
classroom_numbers = [row[0] for row in cursor.fetchall()]

# Loop until every classroom has an entry in ClassesTaught
while len(classroom_numbers) > 0:
    # Generate a random ClassroomNum from the list of existing classroom numbers
    classroom_number = random.choice(classroom_numbers)

    # Insert the new record into the ClassesTaught table
    sql = "INSERT INTO ClassesTaught (ClassroomNum, C_Taught) VALUES (%s, %s)"
    val = (classroom_number, random.choice(['Math', 'Science', 'History', 'English', 'Art']))
    cursor.execute(sql, val)

    # Remove the ClassroomNum from the list of existing classroom numbers
    classroom_numbers.remove(classroom_number)

# Commit the changes and close the connection
cnx.commit()
cnx.close()
