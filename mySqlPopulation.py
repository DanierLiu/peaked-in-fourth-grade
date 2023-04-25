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

# # Insert Cafeteria data
# with open('cafeteria_data.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     next(reader)  # Skip the first row (header)
#     for row in reader:
#         sql = "INSERT INTO Cafeteria (CafeteriaNum, NumOfTables, NumOfSeats, NumOfStaff) VALUES (%s, %s, %s, %s)"
#         val = tuple(row)
#         cursor.execute(sql, val)

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
        sql = "INSERT INTO FoodServed (CafeteriaNum, FoodServed) VALUES (%s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)

# Insert Staff data
with open('staff_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        sql = "INSERT INTO Staff (StaffID, StaffName, age, CafeteriaNum, School_ID, CourseSubject, SecLiceNum, NumYearAsPrincipal, NurseLiceNum, CounsLiceNum, Job_Res, SchoolAcc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)

# Insert Student data
with open('student_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the first row (header)
    for row in reader:
        sql = "INSERT INTO Student (StudentID, StudentName, Grade, age, CafeteriaNum, School_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        val = tuple(row)
        cursor.execute(sql, val)

db.commit() # Commit the changes to the database

cursor.close()
db.close()