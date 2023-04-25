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
    PRIMARY KEY(C_Taught, ClassroomNum)
);

CREATE TABLE Classroom(
    ClassroomNum INT NOT NULL,
    School_ID INT NOT NULL,
    NumOfSeats INT NOT NULL,
    NumOfTables INT NOT NULL,
    PRIMARY KEY(ClassroomNum)
);

CREATE TABLE DateTrainingCertificate(
    StaffID INT NOT NULL,
    CertificateID INT NOT NULL,
    DateReceived VARCHAR(4) NOT NULL,
    PRIMARY KEY(StaffID, CertificateID)
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
    FoodServed VARCHAR(60) NOT NULL,
    PRIMARY KEY(CafeteriaNum, FoodServed)
);

CREATE TABLE IDBadge(
    StaffID INT NOT NULL,
    ExpirationDate VARCHAR(4) NOT NULL,
    DateReceived VARCHAR(4) NOT NULL,
    PRIMARY KEY(StaffID)
);

CREATE TABLE LearnsIn(
    StudentID INT NOT NULL,
    ClassroomNum INT NOT NULL,
    PRIMARY KEY(StudentID, ClassroomNum)
);

CREATE TABLE NursingSchoolDiploma(
    StaffID INT NOT NULL,
    DiplomaID INT NOT NULL,
    DateReceived VARCHAR(10) NOT NULL,
    PRIMARY KEY(StaffID, DiplomaID)
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
    PRIMARY KEY(StaffID)
);

CREATE TABLE Student(
    StudentID INT NOT NULL,
    StudentName VARCHAR(80) NOT NULL,
    year VARCHAR(10) NOT NULL,
    age INT NOT NULL,
    CafeteriaNum INT NOT NULL,
    School_ID INT NOT NULL,
    PRIMARY KEY(StudentID)
);

CREATE TABLE TeachesIn(
    StaffID INT NOT NULL,
    ClassroomNum INT NOT NULL,
    PRIMARY KEY(StaffID, ClassroomNum)
);

CREATE TABLE UniversityDiploma(
    DateReceived VARCHAR(10) NOT NULL,
    DiplomaID INT,
    StaffID INT,
    PRIMARY KEY(StaffID, DiplomaID)
);

ALTER TABLE ClassesTaught
ADD CONSTRAINT fk_ClassesTaught_ClassroomNum
FOREIGN KEY (ClassroomNum) REFERENCES Classroom(ClassroomNum);

ALTER TABLE Classroom
ADD CONSTRAINT fk_Classroom_School_ID
FOREIGN KEY (School_ID) REFERENCES ElementarySchool(School_ID);

ALTER TABLE DateTrainingCertificate
ADD CONSTRAINT fk_DateTrainingCertificate_StaffID
FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);

ALTER TABLE FoodServed
ADD CONSTRAINT fk_FoodServed_CafeteriaNum
FOREIGN KEY (CafeteriaNum) REFERENCES Cafeteria(CafeteriaNum);

ALTER TABLE IDBadge
ADD CONSTRAINT fk_IDBadge_StaffID
FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);

ALTER TABLE LearnsIn
ADD CONSTRAINT fk_LearnsIn_StudentID
FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
ADD CONSTRAINT fk_LearnsIn_ClassroomNum
FOREIGN KEY (ClassroomNum) REFERENCES Classroom(ClassroomNum);

ALTER TABLE NursingSchoolDiploma
ADD CONSTRAINT fk_NursingSchoolDiploma_StaffID
FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);

ALTER TABLE Staff
ADD CONSTRAINT fk_Staff_CafeteriaNum
FOREIGN KEY (CafeteriaNum) REFERENCES Cafeteria(CafeteriaNum),
ADD CONSTRAINT fk_Staff_School_ID
FOREIGN KEY (School_ID) REFERENCES ElementarySchool(School_ID);

ALTER TABLE Student
ADD CONSTRAINT fk_Student_CafeteriaNum
FOREIGN KEY (CafeteriaNum) REFERENCES Cafeteria(CafeteriaNum),
ADD CONSTRAINT fk_Student_School_ID
FOREIGN KEY (School_ID) REFERENCES ElementarySchool(School_ID);

ALTER TABLE TeachesIn
ADD CONSTRAINT fk_TeachesIn_StaffID
FOREIGN KEY (StaffID) REFERENCES Staff(StaffID),
ADD CONSTRAINT fk_TeachesIn_ClassroomNum
FOREIGN KEY (ClassroomNum) REFERENCES Classroom(ClassroomNum);

ALTER TABLE UniversityDiploma
ADD CONSTRAINT fk_UniversityDiploma_StaffID
FOREIGN KEY (StaffID) REFERENCES Staff(StaffID);
