import csv
import random
import mysql.connector
from datetime import datetime, timedelta

# Connect to MySQL server
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="elementaryschool"
)

mycursor = db.cursor()

# Get list of nurses with non-null NurseLiceNum
mycursor.execute("SELECT StaffID FROM Staff WHERE NurseLiceNum IS NOT NULL")
nurse_ids = [row[0] for row in mycursor.fetchall()]

num_rows = len(nurse_ids)

diploma_id_range = range(1000, 10000)
date_format = "%m/%d/%Y"

data = []
for i in range(num_rows):
    staff_id = nurse_ids[i]
    date_received = (datetime.today() - timedelta(days=random.randint(365, 1825))).strftime(date_format)  # Random date in the past 5 years
    diploma_id = random.choice(diploma_id_range)
    row = [
        staff_id,
        diploma_id,
        date_received
    ]
    data.append(row)

    # Insert new NursingSchoolDiploma record into database
    sql = "INSERT INTO nursingschooldiploma (StaffID, DiplomaID, DateReceived) VALUES (%s, %s, %s)"
    val = (staff_id, diploma_id, date_received)
    mycursor.execute(sql, val)
    db.commit()

with open('nursing_school_diploma_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['StaffID', 'DiplomaID', 'DateReceived'])
    writer.writerows(data)

csvfile.close()