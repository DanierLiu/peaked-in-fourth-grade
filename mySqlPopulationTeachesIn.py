import mysql.connector
import csv
import random

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="elementaryschool"
)

# Create a cursor
cursor = db.cursor()

# Get a list of all staff IDs
staff_ids = []
cursor.execute("SELECT StaffID FROM Staff")
for staff_id in cursor.fetchall():
    staff_ids.append(staff_id[0])

# Get a list of all classroom numbers
classroom_nums = []
cursor.execute("SELECT ClassroomNum FROM Classroom")
for classroom_num in cursor.fetchall():
    classroom_nums.append(classroom_num[0])

# Generate data for the TeachesIn table
data = []
for staff_id in staff_ids:
    classroom_num = random.choice(classroom_nums)
    data.append((staff_id, classroom_num))

# Insert data into the TeachesIn table
sql = "INSERT INTO TeachesIn (StaffID, ClassroomNum) VALUES (%s, %s)"
cursor.executemany(sql, data)

# Ensure every staff member has at least one TeachesIn record
for staff_id in staff_ids:
    cursor.execute("SELECT COUNT(*) FROM TeachesIn WHERE StaffID=%s", (staff_id,))
    num_records = cursor.fetchone()[0]
    if num_records == 0:
        classroom_num = random.choice(classroom_nums)
        cursor.execute("INSERT INTO TeachesIn (StaffID, ClassroomNum) VALUES (%s, %s)", (staff_id, classroom_num))

# Commit changes and close the connection
db.commit()
cursor.close()
db.close()
