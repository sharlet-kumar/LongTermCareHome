DROP VIEW IF EXISTS PatientView;
DROP VIEW IF EXISTS MedicationView;
-- View 1: PatientView
CREATE VIEW PatientView AS
SELECT 
    PatientID,
    firstName,
    lastName,
    DateOfBirth,
    Sex,
    Height,
    Weight, 
    AddressID,    
    DNR
FROM 
    Patient;

-- Query on PatientView
SELECT * FROM PatientView WHERE Sex = 'M' AND DateOfBirth = '1980-01-01';


-- View 2: MedicationView
CREATE VIEW MedicationView AS
SELECT 
    medID,
    medName,
    drugClass,
    adminDetails,
    storageDetails
FROM 
    Medication;

-- Query on MedicationView
SELECT * FROM MedicationView WHERE medName = 'aspirin';

-- Testing views with insert

-- Insert into PatientView
INSERT INTO Patient (PatientID, firstName, lastName, DateOfBirth, Sex, Height, Weight, AddressID, DNR, InsuranceCheck)
VALUES 
    ('P001', 'John', 'Doe', '1980-01-01', 'M', 175, 80, NULL, TRUE, TRUE),
    ('P002', 'Jane', 'Smith', '1990-05-15', 'F', 160, 60, NULL, FALSE, FALSE),
    ('P003', 'Mark', 'Lee', '1985-03-22', 'M', 180, 85, NULL, TRUE, TRUE);

-- Insert into MedicationView
INSERT INTO Medication (MedID, MedName, DrugClass, AdminDetails, StorageDetails)
VALUES 
    ('M001', 'Aspirin', 'Analgesic', 'Oral', 'Store at room temperature'),
    ('M002', 'Penicillin', 'Antibiotic', 'Injectable', 'Refrigerated');
