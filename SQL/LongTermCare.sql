-- Active: 1732140614617@@localhost@3306@longtermcare
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
InsuranceCheck boolean,
PRIMARY KEY(PatientID)
 );
create table PatientAddress
(
AddressID varchar (10) not null,
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

create table PatientPhone
(
patientID varchar(10) not null,
phone varchar (15),
primary key (patientID),
foreign key PatientPhone(patientID) references Patient(patientID)
	ON DELETE cascade
    ON UPDATE cascade
);

create table Staff
(
staffID varchar (10) not null,
firstName varchar (15),
lasttime varchar (15),
position varchar (20),
department varchar (30),
primary key (staffID)
);

create table PatientCondition
(
 patientID varchar (10) not null,
 medicalCondition varchar (30) not null,
 description varchar (150), 
 diagnosisDate date, 
 diagnoserID varchar (10)
 ,primary key (patientID, medicalCondition),
 foreign key PatientCondition(diagnoserID) references Staff(staffID)
	ON DELETE NO ACTION
    ON UPDATE CASCADE,
 foreign key PatientCondition(patientID) references Patient(patientID)
	ON DELETE cascade
    ON UPDATE cascade
);

create table PatientStaffCare
(
staffID varchar(10) not null,
patientID varchar (10) not null,
staffRoleInCare varchar(30),
careStartDate date,
careEndDate date,
primary key (staffID, patientID),
foreign key PatientStaffCare(staffID) references Staff(staffID)
	ON DELETE cascade
    ON UPDATE cascade,
foreign key PatientStaffCare(patientID) references Patient(patientID)
	ON DELETE cascade
    ON UPDATE cascade
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
	ON DELETE cascade
    ON UPDATE cascade
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
	ON DELETE cascade
    ON UPDATE cascade
);

create table InsuranceCoverageDetails (
PolicyID varchar (10) not null,
coverageDetails varchar (60), 
primary key (PolicyID),
foreign key InsuranceCoverageDetails(PolicyID) references Insurance(PolicyID)
	ON DELETE cascade
    ON UPDATE cascade
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
prescribingDocID varchar (10) not null,
primary key (patientID, prescribingDocID),
foreign key PatientMedication(patientID) references Patient(patientID)
	ON DELETE CASCADE
    ON UPDATE cascade,
foreign key PatientMedication(prescribingDocID) references Staff(staffID)
	ON DELETE no action
    ON UPDATE cascade
);

create table MedicalSideEffects(
medID varchar(10) not null,
sideEffects varchar (50),
Severity varbinary (10),
primary key (medID),
foreign key MedicalSideEffects(medID) references Medication(medID)
	ON DELETE CASCADE
    ON update cascade
);

create table Allergy(
allergyName varchar (20) not null unique,
managementStrategy varchar (100),
seasonalconsiderations varchar (100),
primary key (allergyName)
);


create table PatientAllergy(
allergyName varchar (20) not null unique,
patientID varchar (10) not null,
severity varchar (6) Check(severity in ('Low', 'Medium', 'High')),
description varchar (300),
primary key (allergyName, patientID),
foreign key PatientAllergy(patientID) references Patient(patientID)
	ON delete cascade
    ON UPDATE cascade,
foreign key PatientAllergy(allergyName) references Allergy(allergyName)
);

create table AllergySymptoms(
allergyName varchar (20) not null,
symptoms varchar (160),
severity varchar (6) Check(severity in ('Low', 'Medium', 'High')),
primary key (allergyName),
foreign key AllergySymptoms(allergyName) references Allergy(allergyName)
	ON DELETE cascade
    ON UPDATE cascade);

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
foreign key Visit(visitorID) references Visitor(visitorID)
	ON delete cascade
    ON update cascade,
foreign key PIDVisit(patientID) references Patient(patientID)
	ON delete cascade
    ON update cascade);

create table VisitorPhone(
visitorID varchar (10) not null, 
phone varchar (15),
primary key (visitorID),
foreign key VisitorPhone(visitorID) references Visitor(visitorID)
	ON delete cascade
    on update cascade
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
foreign key FoodAllergyConflict(foodname) references food(foodname)
	ON delete cascade
    ON update cascade,
foreign key FoodAllergyConflict(allergyName) references Allergy(allergyName)
	ON delete cascade
    ON update cascade);

create table MedAllergyConflict(
allergyName varchar (20) not null,
medID varchar (10) not null, 
ConflictCheck boolean,
primary key (allergyName, medID),
foreign key MedAllergyConflict(medID) references Medication(medID)
	ON delete cascade
    ON update cascade,
foreign key MedAllergyConflict(allergyName) references Allergy(allergyName)
	ON delete cascade
    ON update cascade);

create table MedtoMedConflict(
medicationAID varchar (10) not null,
medicationBID varchar (10) not null,
ConflictCheck boolean,
primary key (medicationAID, medicationBID),
foreign key MedtoMedConflict(medicationAID) references Medication(medID)
	ON delete cascade
    ON update cascade,
foreign key MedtoMedConflict(medicationBID) references Medication(medID)
	ON delete cascade
    ON update cascade);

create table MealPlan(
MealPlanID varchar (10) not null,
schedule varchar (200),
PatientID varchar (10),
primary key (MealPlanID),
foreign key MealPlan(PatientID) references Patient(PatientID)
	ON DELETE NO ACTION
    ON UPDATE cascade);

create table Meal(
MealPlanID varchar (10) not null,
mealName varchar (50) not null,
foodName1 varchar (50) not null,
foodName2 varchar (50),
type varchar (20),
primary key (MealPlanID, mealName, foodName1),
foreign key Meal(MealPlanID) references MealPlan(MealPlanID)
	ON delete cascade
    ON update cascade,
foreign key Meal(foodName1) references food(foodName)
	ON delete cascade
    ON update cascade);


##INSERT STATEMENTS
#Statement Number 1#
insert into food (foodname, foodgroup, calories, protein, fats)
values ('Bowl of Scrambled Eggs', 'Protein', 326, 22, 24);

#Statement Number 2# 
#(It has multiple inserts as it uses the first one to step up the more complex/"interesting" second one)#

insert into Patient (PatientID, firstName, lastName, Sex, Weight, DNR) values 
('2516544', 'William', 'Burgers', 'M', 165, 0);

insert into PatientPhone (PatientID,phone)
(
Select PatientID, 6478880121
from Patient
where patientID= '2516544'
);

#Statement Number 3# 
#(It has multiple as it uses the first one to step up the more complex/"interesting" second one)#

insert into Visitor(visitorID, firstName, lastName) values ('6578080002', 'Paul', 'Burgers');

insert into Visit(visitID, visitorID, patientID)
(
Select '9809123456', visitorID, patientID
from visitor, Patient
);
 
