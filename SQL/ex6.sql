-- Switch to the LongTermCare database
USE LongTermCare;

-- Disable foreign key checks to avoid issues during cleanup
SET FOREIGN_KEY_CHECKS = 0;

-- Clear existing data to avoid duplicate entries or conflicts
DELETE FROM FoodAllergyConflict;
DELETE FROM MedicalSideEffects;
DELETE FROM Medication;
DELETE FROM PatientStaffCare;
DELETE FROM Staff;
DELETE FROM PatientAllergy;
DELETE FROM Allergy;
DELETE FROM Patient;
DELETE FROM Food;

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- Insert required data into the Food table
INSERT INTO Food (foodName, foodGroup, calories, protein, fats)
VALUES 
    ('Peanut Butter', 'Legumes', 588, 25, 50),
    ('Shrimp', 'Seafood', 99, 24, 1);

-- Insert required data into the Allergy table
-- Use numeric values for seasonalconsiderations
INSERT INTO Allergy (allergyName, managementStrategy, seasonalconsiderations)
VALUES 
    ('Peanuts', 'Avoid all peanut products. Carry an epinephrine injector.', 0),
    ('Shellfish', 'Avoid shellfish and carry an epinephrine injector.', 0);

-- Insert test data into Patient
INSERT INTO Patient (PatientID, firstName, lastName, DateOfBirth, Sex, Height, Weight, AddressID, DNR, InsuranceCheck)
VALUES 
    ('P001', 'John', 'Doe', '1980-01-01', 'M', 175, 80, NULL, TRUE, TRUE),
    ('P002', 'Jane', 'Smith', '1990-05-15', 'F', 160, 60, NULL, FALSE, FALSE),
    ('P003', 'Mark', 'Lee', '1985-03-22', 'M', 180, 85, NULL, TRUE, TRUE);

-- Insert test data into Staff
-- Ensure column names match the schema
INSERT INTO Staff (StaffID, firstName, lastName, Position, Department)
VALUES 
    ('S001', 'Alice', 'Brown', 'Nurse', 'General Care'),
    ('S002', 'Bob', 'White', 'Doctor', 'Pediatrics');

-- Insert test data into Medication
INSERT INTO Medication (MedID, MedName, DrugClass, AdminDetails, StorageDetails)
VALUES 
    ('M001', 'Aspirin', 'Analgesic', 'Oral', 'Store at room temperature'),
    ('M002', 'Penicillin', 'Antibiotic', 'Injectable', 'Refrigerated');

-- Insert test data into MedicalSideEffects
INSERT INTO MedicalSideEffects (MedID, SideEffects, Severity)
VALUES 
    ('M001', 'Nausea', 'Mild'),
    ('M002', 'Anaphylaxis', 'Severe');

-- Insert test data into PatientAllergy
-- Ensure Severity matches the allowed values and AllergyName matches the Allergy table
INSERT INTO PatientAllergy (AllergyName, PatientID, Severity, Description)
VALUES 
    ('Peanuts', 'P001', 'Mild', 'Mild allergic reaction'),
    ('Shellfish', 'P002', 'Severe', 'Severe allergic reaction');

-- Insert test data into FoodAllergyConflict
INSERT INTO FoodAllergyConflict (FoodName, AllergyName, ConflictCheck)
VALUES 
    ('Peanut Butter', 'Peanuts', TRUE),
    ('Shrimp', 'Shellfish', TRUE);

-- Insert nurses who are not already assigned to specific patients into the PatientStaffCare table
INSERT INTO PatientStaffCare (StaffID, PatientID, StaffRoleInCare, CareStartDate)
SELECT S.StaffID, P.PatientID, 'Support Care', CURDATE()
FROM Staff S
CROSS JOIN Patient P
WHERE S.Position = 'Nurse'
  AND NOT EXISTS (
      SELECT 1
      FROM PatientStaffCare PSC
      WHERE PSC.StaffID = S.StaffID
        AND PSC.PatientID = P.PatientID
  );

-- Update medications to add "High Priority Storage" note if they have severe side effects
UPDATE Medication M
SET StorageDetails = CONCAT(StorageDetails, ' - High Priority Storage')
WHERE EXISTS (
    SELECT 1
    FROM MedicalSideEffects MS
    WHERE MS.MedID = M.MedID
      AND MS.Severity = 'Severe'
);

-- Delete low-severity patient allergies that are not linked to any food allergies
DELETE FROM PatientAllergy
WHERE Severity = 'Low'
  AND AllergyName NOT IN ( 
      SELECT AllergyName
      FROM FoodAllergyConflict
  );

-- Verify results of the operations
SELECT * FROM PatientStaffCare LIMIT 10; -- Verify nurse-patient assignments
SELECT * FROM Medication WHERE StorageDetails LIKE '%High Priority Storage%'; -- Verify updated medications
SELECT * FROM PatientAllergy; -- Verify remaining allergies
