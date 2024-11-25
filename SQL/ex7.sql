use longtermcare;
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
SELECT * FROM PatientView WHERE Sex = 'M' AND DateOfBirth = '1974-03-31';


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
SELECT * FROM MedicationView WHERE medName = 'Wonder';

-- Testing views with insert
-- Insert into MedicationView
INSERT INTO Medication (MedID, MedName, DrugClass, AdminDetails, StorageDetails)
VALUES 
    ('M999', 'Wonder', 'Analgesic', 'Oral', 'Store at room temperature');
