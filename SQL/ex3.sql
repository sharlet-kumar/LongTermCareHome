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
 

##Select Statements for each insertion

Select * from food;
Select * from PatientPhone;
Select * from Visit

 