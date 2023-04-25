import mysql.connector
import random

# Connect to the SQL server and create a cursor
cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='elementaryschool')
cursor = cnx.cursor()

# Retrieve a list of distinct course subjects from the Staff table
cursor.execute("SELECT DISTINCT CourseSubject FROM Staff WHERE CourseSubject IN ('Math', 'Science', 'History', 'English', 'Art')")
course_subjects = [row[0] for row in cursor.fetchall()]

# Generate a unique DiplomaID for each teacher based on their CourseSubject
diploma_ids = {}
for subject in course_subjects:
    diploma_ids[subject] = random.randint(1000000, 9999999)

# Retrieve the list of StaffIDs from the Staff table
cursor.execute("SELECT StaffID FROM Staff WHERE CourseSubject IN ('Math', 'Science', 'History', 'English', 'Art')")
staff_ids = [row[0] for row in cursor.fetchall()]

# Generate a random DateReceived for each diploma in the past
date_receiveds = [f"{random.randint(1,12)}/{random.randint(1,28)}/{random.randint(1980,2022)}" for i in range(len(staff_ids))]

# Insert the new records into the UniversityDiploma table
for i in range(len(staff_ids)):
    staff_id = staff_ids[i]
    cursor.execute(f"SELECT CourseSubject FROM Staff WHERE StaffID={staff_id}")
    course_subject = cursor.fetchone()[0]
    diploma_id = diploma_ids[course_subject]
    date_received = date_receiveds[i]
    sql = "INSERT INTO UniversityDiploma (DateReceived, DiplomaID, StaffID) VALUES (%s, %s, %s)"
    val = (date_received, diploma_id, staff_id)
    cursor.execute(sql, val)

# Commit the changes and close the connection
cnx.commit()
cnx.close()
