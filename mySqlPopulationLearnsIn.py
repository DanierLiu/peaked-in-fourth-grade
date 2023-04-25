import mysql.connector
import random

# Connect to the SQL server and create a cursor
cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='elementaryschool')
cursor = cnx.cursor()

# Retrieve the list of existing classroom numbers and their corresponding max number of seats from the Classroom table
cursor.execute("SELECT ClassroomNum, NumOfSeats FROM Classroom")
classrooms = [(row[0], row[1]) for row in cursor.fetchall()]

# Retrieve the list of existing student IDs from the Student table
cursor.execute("SELECT StudentID FROM Student")
student_ids = [row[0] for row in cursor.fetchall()]

# Initialize a dictionary to keep track of the number of students in each classroom
classroom_counts = {}
for classroom in classrooms:
    classroom_counts[classroom[0]] = 0

# Loop through each student and assign them to a random classroom
for student_id in student_ids:
    # Get a random classroom that still has available seats
    valid_classrooms = [classroom for classroom in classrooms if classroom_counts[classroom[0]] < classroom[1]]
    if len(valid_classrooms) == 0:
        break  # Stop looping if there are no more available classrooms
    classroom_num = random.choice(valid_classrooms)[0]
    
    # Insert the new record into the LearnsIn table
    sql = "INSERT INTO LearnsIn (StudentID, ClassroomNum) VALUES (%s, %s)"
    val = (student_id, classroom_num)
    cursor.execute(sql, val)
    
    # Update the number of students in the assigned classroom
    classroom_counts[classroom_num] += 1

# Commit the changes and close the connection
cnx.commit()
cnx.close()
