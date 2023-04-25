import mysql.connector
import random
from datetime import datetime, timedelta

# Connect to the SQL server and create a cursor
cnx = mysql.connector.connect(user='root', password='password', host='localhost', database='elementaryschool')
cursor = cnx.cursor()

# Retrieve the list of existing staff IDs from the Staff table
cursor.execute("SELECT StaffID FROM Staff")
staff_ids = [row[0] for row in cursor.fetchall()]

# Generate a random ExpirationDate that is within the next year
expiration_date = datetime.now() + timedelta(days=random.randint(1, 365))

# Generate a random DateReceived that is within the past year
date_received = datetime.now() - timedelta(days=random.randint(1, 365))

# Generate a new ID badge entry for each staff member
for staff_id in staff_ids:
    # Insert the new record into the IDBadge table
    sql = "INSERT INTO IDBadge (StaffID, ExpirationDate, DateReceived) VALUES (%s, %s, %s)"
    val = (staff_id, expiration_date.strftime('%m/%d/%Y'), date_received.strftime('%m/%d/%Y'))
    cursor.execute(sql, val)

# Commit the changes and close the connection
cnx.commit()
cnx.close()
