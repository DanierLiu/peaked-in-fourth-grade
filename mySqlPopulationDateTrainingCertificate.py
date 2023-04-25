import mysql.connector
import random

# Connect to the SQL server and create a cursor
cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='elementaryschool')
cursor = cnx.cursor()

# Retrieve the list of security staff members from the Staff table
cursor.execute("SELECT StaffID, SecLiceNum FROM Staff WHERE SecLiceNum IS NOT NULL")
security_staff = cursor.fetchall()

# Generate a random date in MM/DD/YYYY format
def random_date():
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2)
    year = random.randint(1970, 2022)
    return f"{month}/{day}/{year}"

# Insert a new record into the DateTrainingCertificate table for each security staff member
for staff in security_staff:
    sql = "INSERT INTO DateTrainingCertificate (StaffID, CertificateID, DateReceived) VALUES (%s, %s, %s)"
    certificate_id = staff[1]
    date_received = random_date()
    val = (staff[0], certificate_id, date_received)
    cursor.execute(sql, val)

# Commit the changes and close the connection
cnx.commit()
cnx.close()
