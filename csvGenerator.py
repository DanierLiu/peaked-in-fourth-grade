import csv
import random
import mysql.connector

# Cafeteria Table
num_rows = 5
num_of_tables_range = range(5, 21)
num_of_seats_range = range(30, 101)
num_of_staff_range = range(1, 6)

data = []
for i in range(num_rows):
    row = [
        (i+1),
        random.choice(num_of_tables_range),
        random.choice(num_of_seats_range),
        random.choice(num_of_staff_range),
    ]
    data.append(row)

with open('cafeteria_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['CafeteriaNum', 'NumOfTables', 'NumOfSeats', 'NumOfStaff'])
    writer.writerows(data)

csvfile.close()

# Classroom Table
num_rows = 100
school_ids = 1
num_of_seats_range = range(25, 31)
num_of_tables_range = range(2, 6)

data = []
for i in range(num_rows):
    row = [
        (i+1),
        school_ids,
        random.choice(num_of_seats_range),
        random.choice(num_of_tables_range),
    ]
    data.append(row)

with open('classroom_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ClassroomNum', 'School_ID', 'NumOfSeats', 'NumOfTables'])
    writer.writerows(data)

csvfile.close()

# Elementary School
num_rows = 1
school_names = ['Big Yikes Elementary']
num_of_students_range = range(100, 501)
cafeteria_nums = 5

data = []
for i in range(num_rows):
    row = [
        num_rows,
        school_names,
        random.choice(num_of_students_range),
        cafeteria_nums,
    ]
    data.append(row)

with open('elementaryschool_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['School_ID', 'SchoolName', 'NumOfStudents', 'CafeteriaNum'])
    writer.writerows(data)

csvfile.close()

# Food Served
num_rows = 25
cafeteria_nums = range(1, 5)
foods_served = ['Pizza', 'Burgers', 'Hot dogs', 'Tacos', 'Sandwiches']

data = []
for i in range(num_rows):
    row = [
        random.choice(cafeteria_nums),
        random.choice(foods_served)
    ]
    data.append(row)

with open('foodserved_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['CafeteriaNum', 'FoodServed'])
    writer.writerows(data)

csvfile.close()

Staff
# Load first and last names from CSV file
with open('names.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    first_names = [row[0] for row in reader]
with open('names.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    last_names = [row[1] for row in reader]

num_rows = 500

ages_range = range(20, 71)
course_subjects = ['Math', 'Science', 'History', 'English', 'Art']
job_res = ['Teacher', 'Nurse', 'Counselor', 'Security', 'Lunch Member', 'Janitor']
school_id = 1
used_ids = []

data = []
for i in range(num_rows):
    while True:
        new_id = random.randint(1, 1000)  # Generate a new ID
        if new_id not in used_ids:  # Check if it's already been used
            used_ids.append(new_id)  # Add to the list of used IDs
        break  # Break out of the loop if the ID is unique
    if(i == 1):
        job = 'Principal'
    else:
        job = random.choice(job_res)
    cafeteria_num = random.randint(1, 5)
    nursing_license_num = None
    num_years_as_principal = None
    security_license_num = None
    counselor_license_num = None
    course_subject = None
    job_res_val = None
    school_acc_val = 'No'  # Set SchoolAcc to 'No' by default
    
    if job == 'Nurse':
        nursing_license_num = str(random.randint(1000000, 9999999))
    elif job == 'Principal':
        num_years_as_principal = random.randint(0, 30)
    elif job == 'Security':
        security_license_num = str(random.randint(1000000, 9999999))
    elif job == 'Counselor':
        counselor_license_num = str(random.randint(1000000, 9999999))
    elif job == 'Teacher':
        course_subject = random.choice(course_subjects)
        job_res_val = None
    elif job == 'Janitor':  # Set SchoolAcc to 'Yes' if job is 'Janitor'
        school_acc_val = 'Yes'
    else:  # Lunch Member
        job_res_val = random.choice(['Cook', 'Dishes', 'Lunch Line'])

    row = [
        new_id,
        random.choice(first_names) + ' ' + random.choice(last_names),
        random.choice(ages_range),
        cafeteria_num,
        school_id,
        course_subject,
        security_license_num,
        num_years_as_principal,
        nursing_license_num,
        counselor_license_num,
        job_res_val,
        school_acc_val  # Set SchoolAcc value
    ]
    data.append(row)

with open('staff_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['StaffID', 'StaffName', 'age', 'CafeteriaNum', 'School_ID', 'CourseSubject', 'SecLiceNum', 'NumYearAsPrincipal', 'NurseLiceNum', 'CounsLiceNum', 'Job_Res', 'SchoolAcc'])
    writer.writerows(data)

csvfile.close()

# Student
# Load first and last names from CSV file
with open('names.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    first_names = [row[0] for row in reader]
with open('names.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    last_names = [row[1] for row in reader]

num_rows = 500

ages_range = range(5, 14)
school_id = 1

data = []
for i in range(num_rows):
    grade = random.choice(['Kg', '1st', '2nd', '3rd', '4th', '5th'])
    row = [
        (i+1),
        random.choice(first_names) + ' ' + random.choice(last_names),
        grade,
        random.choice(ages_range),
        random.randint(1, 5), # CafeteriaNum
        school_id,
    ]
    data.append(row)

with open('student_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['StudentID', 'StudentName', 'Grade', 'age', 'CafeteriaNum', 'School_ID'])
    writer.writerows(data)

csvfile.close()
