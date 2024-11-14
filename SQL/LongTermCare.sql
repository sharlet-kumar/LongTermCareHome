use LongTermCare;

create table Patient 
(
PatientID varchar (10) not null, 
firstName varchar (15),
lastName varchar (15), 
DateOfBirth date,
Sex char (1) check(Sex in ('M','F')), 
Height smallint,
Weight smallint, 
InsuranceID int (10), 
AddressID int (10),
DNR boolean,
MealPlanID int (10),
 PRIMARY KEY(PatientID)
 ##DO FOREIGN KEYS
 );
create table PatientAddress
(
AddressID int (10),
StreetNo int,
StreetName varchar (30),
 UnitNo smallint,
 City varchar (30),
 State varchar (30),
 Country varchar (30),
 primary key (AddressID),
 foreign key PatientAddress(AddressID) references Patient(AddressID)
	ON DELETE CASCADE
    ON UPDATE CASCADE
);
create table PatientMedications
(
patientID int (10),
 medicalCondition varchar (30),
 description varchar (150), 
 diagnosisDate date, 
 diagnoserID varchar (10),
 primary key (patientID, medicalCondition),
 foreign key PatientMedications(patientID) references Patient(patientID)
);
create table PatientPhone
(
patientID int(10),
phone varchar (15),
primary key (patientID),
foreign key PatientPhone(patientID) references Patient(patientID)
);

create table Staff
(
staffID varchar (10),
firstName varchar (15),
lasttime varchar (15),
position varchar (20),
department varchar (30),
primary key (staffID)
);

create table PatientStaffCare
(
staffID varchar(10),
patientID varchar (10),
staffRoleInCare varchar(30),
careStartDate date,
careEndDate date,
primary key (staffID, patientID),
foreign key PatientStaffCare(staffID) references Staff(staffID),
foreign key PatientStaffCare(patientID) references Patient(patientID)
);

create table StaffPhone
(
staffID varchar (10),
phone varchar (15),
primary key (staffID),
foreign key StaffPhone(staffID) references Staff(staffID));

create table Insurance(

);
##ENSURE INSURANCE RELATIONS ARE CORRECT##

create table Medication (
medID varchar (10),
medName varchar (30),
drugclass varchar (20),
adminDetails varchar (50),
storagedetails varchar (50),
primary key (medID));

create table PatientMedication( ##Determine what are PK's and if PDocID needs to renamed to StaffID
PatientID varchar (10),
medID varchar (10),
dosage smallint,
AdminSchedule varchar (40),
prescribingDocID varchar (10),
primary key (patientID, ???)
foreign key Medication(patientID) references Patient(patientID)
foreign key PatientMedication(prescribingDocID) references StaffID(staffID)
);

create table MedicalSideEffects(
medID varchar(10) not null,
sideEffects varchar (50),
Severity varbinary (10),
primary key (medID),
foreign key MedicalSideEffects(medID) references Medication(medID) 
);

create table Allergy(
allergyName varchar (20) not null,
managementStrategy varchar (100),
seasonalconsiderations varchar (50),
primary key (allergyName)
);


create table PatientAllergy(
allergyName varchar (20) not null,
patientID varchar (10) not null,
severity varchar (6) Check(severity in ('Low', 'Medium', 'High')),
description varchar (50),
primary key (allergyName, patientID),
foreign key PatientAllergy(patientID) references Patient(patientID),
foreign key PatientAllergy(allergyName) references PatientAllergy(allergyName)
);

create table AllergySymptoms(
allergyName varchar (20) not null,
symptoms varchar (160),
severity varchar (6) Check(severity in ('Low', 'Medium', 'High')))
;

create table AllergyTreatment ##DO WE NEED THIS???

create table MealPlan ##CAN THIS COMBINE INTO PLAN AND FOOD THING??

create table Visitor(
vistorID varchar (10) not null,
firstName varchar (15),
lastName varchar (15)
primary key (vistorID));

create table Visit(
visitID varchar (10) not null,
vistorID varchar (10) not null,
patientID varchar (10) not null,
VisitDate date,
notes varchar (100));

create table VisitorPhone(
visitorID varchar (10), 
phone varchar (15)
);

create table 

create table 
create table Food;
create table MealPlan;