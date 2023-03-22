CREATE TABLE Cafeteria(
    CafeteriaNum int NOT NULL,
    NumOfTables int NOT NULL,
    NumOfSeats int NOT NULL,
    NumOfStaff int NOT NULL,
    PRIMARY KEY(CafeteriaNum)
);

CREATE TABLE Classes Taught(
    ClassroomNum int,
    C_Taught Varchar(80),
    PRIMARY KEY(C_Taught, ClassroomNum),
    FOREIGN KEY(ClassroomNum) REFERENCES Classroom(ClassroomNum)
);

CREATE TABLE Classroom(
    ClassroomNum int,
    School_ID int,
    NumOfSeats int,
    NumOfTables int,
    PRIMARY KEY(ClassroomNum)
);

CREATE TABLE DateTrainingCertificate(
    StaffID int,
    CertificateID int,
    DateReceived VARCHAR(4),
    PRIMARY KEY(StaffID, CertificateID)
);

CREATE TABLE ElementarySchool(
    School_ID int,
    SchoolName varchar(80),
    NumOfStudents int,
    CafeteriaNum int,
    PRIMARY KEY(School_ID)
);

CREATE TABLE FoodServed(
    CafeteriaNum int,
    FoodServed int,
    PRIMARY KEY(CafeteriaNum, FoodServed)
);

CREATE TABLE IDBadge(
    StaffID int,
    ExpirationDate VARCHAR(4),
    DateReceived VARCHAR(4),
    PRIMARY KEY(StaffID)
);

CREATE TABLE LearnsIn(
    StudentID int,
    ClassroomNum int,
    PRIMARY KEY(StudentID, ClassroomNum)
);

CREATE TABLE NursingSchoolDiploma(
    StaffID int,
    DiplomaID int,
    DateReceived VARCHAR(10),
    PRIMARY KEY(StaffID, DiplomaID)
);

CREATE TABLE Staff(
    StaffID INT,
    StaffName VARCHAR(80),
    age int,
    CafeteriaNum int,
    School_ID int,
    CourseSubject VARCHAR(80),
    SecLiceNum VARCHAR(20),
    NumYearAsPrincipal int,
    NurseLiceNum int,
    CounsLiceNum int,
    Job_Res VARCHAR(80),
    SchoolAcc VARCHAR(20),
    PRIMARY(StaffID)
);

CREATE TABLE Student(
    StudentID int,
    StudentName varchar(80),
    year varchar(10),
    age int,
    CafeteriaNum int,
    School_ID int,
    PRIMARY KEY(StudentID)
);

