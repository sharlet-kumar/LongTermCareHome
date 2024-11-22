-- Clear existing data to avoid duplicate entries or foreign key conflicts
DELETE FROM FoodAllergyConflict;
DELETE FROM MedicalSideEffects;
DELETE FROM Medication;
DELETE FROM PatientStaffCare;
DELETE FROM Staff;
DELETE FROM PatientAllergy;
DELETE FROM Allergy;
DELETE FROM Patient;
DELETE FROM Food;

-- Insert required data into the Food table
INSERT INTO Food (foodName, foodGroup, calories, protein, fats)
VALUES 
    ('Peanut Butter', 'Legumes', 588, 25, 50),
    ('Shrimp', 'Seafood', 99, 24, 1);

-- Insert required data into the Allergy table
INSERT INTO Allergy (allergyName, managementStrategy, seasonalconsiderations)
VALUES 
    ('Peanuts', 'Avoid all peanut products. Carry an epinephrine injector.', 'No seasonal considerations'),
    ('Shellfish', 'Avoid shellfish and carry an epinephrine injector.', 'No seasonal considerations');

-- Insert test data into Patient
INSERT INTO Patient (PatientID, firstName, lastName, DateOfBirth, Sex, Height, Weight, AddressID, DNR, InsuranceCheck)
VALUES 
    ('P001', 'John', 'Doe', '1980-01-01', 'M', 175, 80, NULL, TRUE, TRUE),
    ('P002', 'Jane', 'Smith', '1990-05-15', 'F', 160, 60, NULL, FALSE, FALSE),
    ('P003', 'Mark', 'Lee', '1985-03-22', 'M', 180, 85, NULL, TRUE, TRUE);

-- Insert test data into Staff
-- Use 'lasttime' instead of 'lastName' to match the original schema
INSERT INTO Staff (StaffID, firstName, lasttime, Position, Department)
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
-- AllergyName must match the Allergy table
INSERT INTO PatientAllergy (AllergyName, PatientID, Severity, Description)
VALUES 
    ('Peanuts', 'P001', 'Low', 'Mild allergic reaction'),
    ('Shellfish', 'P002', 'High', 'Severe allergic reaction');

-- Insert test data into FoodAllergyConflict
INSERT INTO FoodAllergyConflict (FoodName, AllergyName, ConflictCheck)
VALUES 
    ('Peanut Butter', 'Peanuts', TRUE),
    ('Shrimp', 'Shellfish', TRUE);

-- Insert nurses who are not already assigned to specific patients into the PatientStaffCare table
INSERT INTO PatientStaffCare (StaffID, PatientID, StaffRoleInCare, CareStartDate)
SELECT S.StaffID, P.PatientID, 'Support Care', CURDATE()
FROM Staff S, Patient P
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
