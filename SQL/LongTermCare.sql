drop database longtermcare;
create database longtermcare;
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
AddressID varchar (10) unique,
DNR boolean,
MealPlanID varchar (10),
PRIMARY KEY(PatientID)
 );
create table PatientAddress
(
AddressID varchar (10),
StreetNo int,
StreetName varchar (30),
 UnitNo smallint,
 City varchar (30),
 State varchar (30),
 Country varchar (30),
 PRIMARY KEY (AddressID),
 foreign key PatientAddress(AddressID) references Patient(AddressID)
	ON DELETE CASCADE
    ON UPDATE CASCADE
);
create table PatientMedications
(
 patientID varchar (10),
 medicalCondition varchar (30),
 description varchar (150), 
 diagnosisDate date, 
 diagnoserID varchar (10) ##Is this a FK???###
 ,primary key (patientID, medicalCondition),
 foreign key PatientMedications(patientID) references Patient(patientID)
);
create table PatientPhone
(
patientID varchar(10),
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
staffID varchar (10) not null,
phone varchar (15),
primary key (staffID),
foreign key StaffPhone(staffID) references Staff(staffID));

create table Insurance(
PolicyID varchar (10) not null,
provider varchar (20),
patientID varchar (10),
BillingAddressID varchar (10) unique,
primary key (PolicyID),
foreign key Insurance(patientID) references Patient(patientID)
);

create table BillingAddress(
BillingAddressID varchar (10) not null, 
streetNo int,
streetName varchar (20),
unitNo smallint,
city varchar (25),
state varchar (20),
country varchar (30),
primary key (BillingAddressID),
foreign key BillingAddress(BillingAddressID) references Insurance(BillingAddressID)
);

create table InsuranceCoverageDetails (
PolicyID varchar (10) not null,
coverageDetails varchar (60), 
primary key (PolicyID),
foreign key InsuranceCoverageDetails(PolicyID) references Insurance(PolicyID)
)
;


create table Medication (
medID varchar (10) not null,
medName varchar (30),
drugclass varchar (20),
adminDetails varchar (50),
storagedetails varchar (50),
primary key (medID));

create table PatientMedication( 
PatientID varchar (10) not null,
medID varchar (10) not null,
dosage smallint,
AdminSchedule varchar (40),
prescribingDocID varchar (10),
primary key (patientID, prescribingDocID),
foreign key Medication(patientID) references Patient(patientID),
foreign key PatientMedication(prescribingDocID) references Staff(staffID)
);

create table MedicalSideEffects(
medID varchar(10) not null,
sideEffects varchar (50),
Severity varbinary (10),
primary key (medID),
foreign key MedicalSideEffects(medID) references Medication(medID) 
);

create table Allergy(
allergyName varchar (20) not null unique,
managementStrategy varchar (100),
seasonalconsiderations varchar (50),
primary key (allergyName)
);


create table PatientAllergy(
allergyName varchar (20) not null unique,
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
severity varchar (6) Check(severity in ('Low', 'Medium', 'High')),
primary key (allergyName));


#create table AllergyTreatment ##DO WE NEED THIS???

#create table MealPlan ##CAN THIS COMBINE INTO PLAN AND FOOD THING??

create table Visitor(
visitorID varchar (10) not null,
firstName varchar (15),
lastName varchar (15),
primary key (visitorID));

create table Visit(
visitID varchar (10) not null,
visitorID varchar (10) not null,
patientID varchar (10) not null,
VisitDate date,
notes varchar (100),
primary key (visitID),
foreign key Visit(visitorID) references Visitor(visitorID),
foreign key PIDVisit(patientID) references Patient(patientID));

create table VisitorPhone(
visitorID varchar (10) not null, 
phone varchar (15),
primary key (visitorID),
foreign key VisitorPhone(visitorID) references Visitor(visitorID)
);

create table food(
foodname varchar (50) not null,
foodgroup varchar (20),
calories int,
protein int,
fats int,
primary key (foodname)
);

create table FoodAllergyConflict(
foodname varchar (50) not null,
allergyName varchar (20) not null,
ConflictCheck boolean,
primary key (foodname, allergyName),
foreign key FoodAllergyConflict(foodname) references food(foodname),
foreign key FoodAllergyConflict(allergyName) references Allergy(allergyName));

create table MedAllergyConflict(
allergyName varchar (20) not null,
medID varchar (10) not null, 
ConflictCheck boolean,
primary key (allergyName, medID),
foreign key MedAllergyConflict(medID) references Medication(medID),
foreign key MedAllergyConflict(allergyName) references Allergy(allergyName));

create table MedtoMedConflict(
medicationAID varchar (10) not null,
medicationBID varchar (10) not null,
ConflictCheck boolean,
primary key (medicationAID, medicationBID),
foreign key MedtoMedConflict(medicationAID) references Medication(medID),
foreign key MedtoMedConflict(medicationBID) references Medication(medID));

##INSERT STATEMENTS

insert into food (foodname, foodgroup, calories, protein, fats)
values ('Bowl of Scrambled Eggs', 'Protein', 326, 22, 24);

insert into Patient (PatientID, firstName, lastName, Sex, Weight, DNR) values 
('2516544', 'William', 'Burgers', 'M', 165, 0);

insert into PatientPhone (PatientID,phone)
(
Select PatientID, 6478880121
from Patient
);



 
