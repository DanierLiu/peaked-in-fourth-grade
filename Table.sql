CREATE TABLE Cafeteria(
    CafeteriaNum INT NOT NULL,
    NumOfTables INT NOT NULL,
    NumOfSeats INT NOT NULL,
    NumOfStaff INT NOT NULL,
    PRIMARY KEY(CafeteriaNum)
);

CREATE TABLE ClassesTaught(
    ClassroomNum INT NOT NULL,
    C_Taught VARCHAR(80) NOT NULL,
    PRIMARY KEY(C_Taught, ClassroomNum),
    FOREIGN KEY(ClassroomNum) REFERENCES Classroom(ClassroomNum)
);

CREATE TABLE Classroom(
    ClassroomNum INT NOT NULL,
    School_ID INT NOT NULL,
    NumOfSeats INT NOT NULL,
    NumOfTables INT NOT NULL,
    PRIMARY KEY(ClassroomNum),
    FOREIGN KEY(School_ID) REFERENCES ElementarySchool(School_ID)
);

CREATE TABLE DateTrainingCertificate(
    StaffID INT NOT NULL,
    CertificateID INT NOT NULL,
    DateReceived VARCHAR(4) NOT NULL,
    PRIMARY KEY(StaffID, CertificateID),
    FOREIGN KEY(StaffID) REFERENCES Staff(StaffID)
);

CREATE TABLE ElementarySchool(
    School_ID INT NOT NULL,
    SchoolName VARCHAR(80) NOT NULL,
    NumOfStudents INT NOT NULL,
    CafeteriaNum INT NOT NULL,
    PRIMARY KEY(School_ID)
);

CREATE TABLE FoodServed(
    CafeteriaNum INT NOT NULL,
    FoodServed INT NOT NULL,
    PRIMARY KEY(CafeteriaNum, FoodServed)
    FOREIGN KEY(CafeteriaNum) REFERENCES Cafeteria(CafeteriaNum)
);

CREATE TABLE IDBadge(
    StaffID INT NOT NULL,
    ExpirationDate VARCHAR(4) NOT NULL,
    DateReceived VARCHAR(4) NOT NULL,
    PRIMARY KEY(StaffID),
    FOREIGN KEY(StaffID) REFERENCES Staff(StaffID)
);

CREATE TABLE LearnsIn(
    StudentID INT NOT NULL,
    ClassroomNum INT NOT NULL,
    PRIMARY KEY(StudentID, ClassroomNum),
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY(ClassroomNum) REFERENCES Classroom(ClassroomNum)
);

CREATE TABLE NursingSchoolDiploma(
    StaffID INT NOT NULL,
    DiplomaID INT NOT NULL,
    DateReceived VARCHAR(10) NOT NULL,
    PRIMARY KEY(StaffID, DiplomaID),
    FOREIGN KEY(StaffID) REFERENCES Staff(StaffID)
);

CREATE TABLE Staff(
    StaffID INT NOT NULL,
    StaffName VARCHAR(80) NOT NULL,
    age INT NOT NULL,
    CafeteriaNum INT,
    School_ID INT NOT NULL,
    CourseSubject VARCHAR(80),
    SecLiceNum VARCHAR(20),
    NumYearAsPrincipal INT,
    NurseLiceNum INT,
    CounsLiceNum INT,
    Job_Res VARCHAR(80),
    SchoolAcc VARCHAR(20),
    PRIMARY KEY(StaffID),
    FOREIGN KEY(CafeteriaNum) REFERENCES Cafeteria(CafeteriaNum),
    FOREIGN KEY(School_ID) REFERENCES ElementarySchool(School_ID)
);

CREATE TABLE Student(
    StudentID INT NOT NULL,
    StudentName VARCHAR(80) NOT NULL,
    year VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    CafeteriaNum INT NOT NULL,
    School_ID INT NOT NULL,
    PRIMARY KEY(StudentID),
    FOREIGN KEY(CafeteriaNum) REFERENCES Cafeteria(CafeteriaNum),
    FOREIGN KEY(School_ID) REFERENCES ElementarySchool(School_ID)
);

CREATE TABLE TeachesIn(
    StaffID INT NOT NULL,
    ClassroomNum INT NOT NULL,
    PRIMARY KEY(StaffID, ClassroomNum),
    FOREIGN KEY(StaffID) REFERENCES Staff(StaffID),
    FOREIGN KEY(ClassroomNum) REFERENCES Classroom(ClassroomNum)
);

CREATE TABLE UniversityDiploma(
    DateReceived VARCHAR(10) NOT NULL,
    DiplomaID INT,
    StaffID INT,
    PRIMARY KEY(StaffID, DiplomaID),
    FOREIGN KEY(StaffID) REFERENCES STAFF(StaffID)
);