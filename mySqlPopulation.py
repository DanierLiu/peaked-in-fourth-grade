import csv
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="elementaryschool"
)

# Create a cursor object
cursor = db.cursor()

# Insert Cafeteria data
with open('cafeteria_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        sql = "INSERT INTO Cafeteria (CafeteriaNum, NumOfTables, NumOfSeats, NumOfStaff) VALUES (%s, %s, %s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)

# Insert Elementary School data
with open('elementaryschool_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        sql = "INSERT INTO ElementarySchool (School_ID, SchoolName, NumOfStudents, CafeteriaNum) VALUES (%s, %s, %s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)

# Insert Classroom data
with open('classroom_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        sql = "INSERT INTO Classroom (ClassroomNum, School_ID, NumOfSeats, NumOfTables) VALUES (%s, %s, %s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)


# Insert Food Served data
with open('foodserved_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        cafeteria_num, food_served = row
        # Check if the combination of CafeteriaNum and FoodServed already exists in the table
        cursor.execute("SELECT * FROM FoodServed WHERE CafeteriaNum=%s AND FoodServed=%s", (cafeteria_num, food_served))
        result = cursor.fetchone()
        if result is not None:
            print(f"Skipping duplicate entry: {row}")
            continue
        # Insert new row
        sql = "INSERT INTO FoodServed (CafeteriaNum, FoodServed) VALUES (%s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)


# Insert Staff data
with open('staff_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        # Check for empty values and replace with None
        row = [None if x == '' else x for x in row]
        sql = "INSERT INTO Staff (StaffID, StaffName, age, CafeteriaNum, School_ID, CourseSubject, SecLiceNum, NumYearAsPrincipal, NurseLiceNum, CounsLiceNum, Job_Res, SchoolAcc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)

# Insert Student data
with open('student_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        sql = "INSERT INTO Student (StudentID, StudentName, year, age, CafeteriaNum, School_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)

db.commit() # Commit the changes to the database

cursor.close()
db.close()