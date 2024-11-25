DELIMITER $$

-- Procedure to search all tables for a given term
CREATE PROCEDURE search_all_tables(search_term VARCHAR(255))
BEGIN
    -- Search Patient Table
    SELECT * FROM Patient
    WHERE PatientID LIKE CONCAT('%', search_term, '%')
    OR firstName LIKE CONCAT('%', search_term, '%')
    OR lastName LIKE CONCAT('%', search_term, '%')
    OR DateOfBirth LIKE CONCAT('%', search_term, '%')
    OR Sex LIKE CONCAT('%', search_term, '%')
    OR Height LIKE CONCAT('%', search_term, '%')
    OR Weight LIKE CONCAT('%', search_term, '%')
    OR AddressID LIKE CONCAT('%', search_term, '%')
    OR DNR LIKE CONCAT('%', search_term, '%')
    OR InsuranceCheck LIKE CONCAT('%', search_term, '%');
    
    -- Search PatientAddress Table
    SELECT * FROM PatientAddress
    WHERE AddressID LIKE CONCAT('%', search_term, '%')
    OR StreetNo LIKE CONCAT('%', search_term, '%')
    OR StreetName LIKE CONCAT('%', search_term, '%')
    OR UnitNo LIKE CONCAT('%', search_term, '%')
    OR City LIKE CONCAT('%', search_term, '%')
    OR State LIKE CONCAT('%', search_term, '%')
    OR Country LIKE CONCAT('%', search_term, '%');
    
    -- Search PatientPhone Table
    SELECT * FROM PatientPhone
    WHERE patientID LIKE CONCAT('%', search_term, '%')
    OR phone LIKE CONCAT('%', search_term, '%');
    
    -- Search Staff Table
    SELECT * FROM Staff
    WHERE staffID LIKE CONCAT('%', search_term, '%')
    OR firstName LIKE CONCAT('%', search_term, '%')
    OR lastName LIKE CONCAT('%', search_term, '%')
    OR position LIKE CONCAT('%', search_term, '%')
    OR department LIKE CONCAT('%', search_term, '%');
    
    -- Search PatientCondition Table
    SELECT * FROM PatientCondition
    WHERE patientID LIKE CONCAT('%', search_term, '%')
    OR medicalCondition LIKE CONCAT('%', search_term, '%')
    OR description LIKE CONCAT('%', search_term, '%')
    OR diagnoserID LIKE CONCAT('%', search_term, '%');
    
    -- Search PatientStaffCare Table
    SELECT * FROM PatientStaffCare
    WHERE staffID LIKE CONCAT('%', search_term, '%')
    OR patientID LIKE CONCAT('%', search_term, '%')
    OR staffRoleInCare LIKE CONCAT('%', search_term, '%')
    OR careStartDate LIKE CONCAT('%', search_term, '%')
    OR careEndDate LIKE CONCAT('%', search_term, '%');
    
    -- Search StaffPhone Table
    SELECT * FROM StaffPhone
    WHERE staffID LIKE CONCAT('%', search_term, '%')
    OR phone LIKE CONCAT('%', search_term, '%');
    
    -- Search Insurance Table
    SELECT * FROM Insurance
    WHERE PolicyID LIKE CONCAT('%', search_term, '%')
    OR provider LIKE CONCAT('%', search_term, '%')
    OR patientID LIKE CONCAT('%', search_term, '%')
    OR BillingAddressID LIKE CONCAT('%', search_term, '%');
    
    -- Search BillingAddress Table
    SELECT * FROM BillingAddress
    WHERE BillingAddressID LIKE CONCAT('%', search_term, '%')
    OR streetNo LIKE CONCAT('%', search_term, '%')
    OR streetName LIKE CONCAT('%', search_term, '%')
    OR unitNo LIKE CONCAT('%', search_term, '%')
    OR city LIKE CONCAT('%', search_term, '%')
    OR state LIKE CONCAT('%', search_term, '%')
    OR country LIKE CONCAT('%', search_term, '%');
    
    -- Search InsuranceCoverageDetails Table
    SELECT * FROM InsuranceCoverageDetails
    WHERE PolicyID LIKE CONCAT('%', search_term, '%')
    OR coverageDetails LIKE CONCAT('%', search_term, '%');
    
    -- Search Medication Table
    SELECT * FROM Medication
    WHERE medID LIKE CONCAT('%', search_term, '%')
    OR medName LIKE CONCAT('%', search_term, '%')
    OR drugclass LIKE CONCAT('%', search_term, '%')
    OR adminDetails LIKE CONCAT('%', search_term, '%')
    OR storagedetails LIKE CONCAT('%', search_term, '%');
    
    -- Search PatientMedication Table
    SELECT * FROM PatientMedication
    WHERE PatientID LIKE CONCAT('%', search_term, '%')
    OR medID LIKE CONCAT('%', search_term, '%')
    OR dosage LIKE CONCAT('%', search_term, '%')
    OR AdminSchedule LIKE CONCAT('%', search_term, '%')
    OR prescribingDocID LIKE CONCAT('%', search_term, '%');
    
    -- Search MedicalSideEffects Table
    SELECT * FROM MedicalSideEffects
    WHERE medID LIKE CONCAT('%', search_term, '%')
    OR sideEffects LIKE CONCAT('%', search_term, '%')
    OR Severity LIKE CONCAT('%', search_term, '%');
    
    -- Search Allergy Table
    SELECT * FROM Allergy
    WHERE allergyName LIKE CONCAT('%', search_term, '%')
    OR managementStrategy LIKE CONCAT('%', search_term, '%')
    OR seasonalconsiderations LIKE CONCAT('%', search_term, '%');
    
    -- Search PatientAllergy Table
    SELECT * FROM PatientAllergy
    WHERE allergyName LIKE CONCAT('%', search_term, '%')
    OR patientID LIKE CONCAT('%', search_term, '%')
    OR severity LIKE CONCAT('%', search_term, '%')
    OR description LIKE CONCAT('%', search_term, '%');
    
    -- Search AllergySymptoms Table
    SELECT * FROM AllergySymptoms
    WHERE allergyName LIKE CONCAT('%', search_term, '%')
    OR symptoms LIKE CONCAT('%', search_term, '%')
    OR severity LIKE CONCAT('%', search_term, '%');
    
    -- Search AllergyTreatment Table
    SELECT * FROM AllergyTreatment
    WHERE allergyName LIKE CONCAT('%', search_term, '%')
    OR treatment LIKE CONCAT('%', search_term, '%')
    OR considerations LIKE CONCAT('%', search_term, '%');
    
    -- Search Visitor Table
    SELECT * FROM Visitor
    WHERE visitorID LIKE CONCAT('%', search_term, '%')
    OR firstName LIKE CONCAT('%', search_term, '%')
    OR lastName LIKE CONCAT('%', search_term, '%');
    
    -- Search Visit Table
    SELECT * FROM Visit
    WHERE visitID LIKE CONCAT('%', search_term, '%')
    OR visitorID LIKE CONCAT('%', search_term, '%')
    OR patientID LIKE CONCAT('%', search_term, '%')
    OR VisitDate LIKE CONCAT('%', search_term, '%')
    OR notes LIKE CONCAT('%', search_term, '%');
    
    -- Search VisitorPhone Table
    SELECT * FROM VisitorPhone
    WHERE visitorID LIKE CONCAT('%', search_term, '%')
    OR phone LIKE CONCAT('%', search_term, '%');
    
    -- Search food Table
    SELECT * FROM food
    WHERE foodname LIKE CONCAT('%', search_term, '%')
    OR foodgroup LIKE CONCAT('%', search_term, '%')
    OR calories LIKE CONCAT('%', search_term, '%')
    OR protein LIKE CONCAT('%', search_term, '%')
    OR fats LIKE CONCAT('%', search_term, '%');
    
    -- Search FoodAllergyConflict Table
    SELECT * FROM FoodAllergyConflict
    WHERE foodname LIKE CONCAT('%', search_term, '%')
    OR allergyName LIKE CONCAT('%', search_term, '%')
    OR ConflictCheck LIKE CONCAT('%', search_term, '%');
    
    -- Search MedAllergyConflict Table
    SELECT * FROM MedAllergyConflict
    WHERE allergyName LIKE CONCAT('%', search_term, '%')
    OR medID LIKE CONCAT('%', search_term, '%')
    OR ConflictCheck LIKE CONCAT('%', search_term, '%');
    
    -- Search MedtoMedConflict Table
    SELECT * FROM MedtoMedConflict
    WHERE medicationAID LIKE CONCAT('%', search_term, '%')
    OR medicationBID LIKE CONCAT('%', search_term, '%')
    OR ConflictCheck LIKE CONCAT('%', search_term, '%')
    OR severity LIKE CONCAT('%', search_term, '%');
    
    -- Search MealPlan Table
    SELECT * FROM MealPlan
    WHERE MealPlanID LIKE CONCAT('%', search_term, '%')
    OR schedule LIKE CONCAT('%', search_term, '%')
    OR PatientID LIKE CONCAT('%', search_term, '%');
    
    -- Search Meal Table
    SELECT * FROM Meal
    WHERE MealPlanID LIKE CONCAT('%', search_term, '%')
    OR mealName LIKE CONCAT('%', search_term, '%')
    OR foodName1 LIKE CONCAT('%', search_term, '%')
    OR foodName2 LIKE CONCAT('%', search_term, '%')
    OR type LIKE CONCAT('%', search_term, '%');
    
END$$

-- Dynamic Search Procedure to handle searches for any table
CREATE PROCEDURE search_table(search_term VARCHAR(255), table_name VARCHAR(255))
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE column_name VARCHAR(255);
    DECLARE column_type VARCHAR(255);
    DECLARE where_clause VARCHAR(10000) DEFAULT '';
    
    -- Declare a cursor to get all column names and types for the given table
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME, COLUMN_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = table_name AND TABLE_SCHEMA = DATABASE();
    
    -- Declare the NOT FOUND handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    -- Open the cursor
    OPEN cur;
    
    -- Loop through each column
    read_loop: LOOP
        FETCH cur INTO column_name, column_type;
        
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- If the column type is string-like, use LIKE for search, otherwise handle appropriately
        IF column_type LIKE '%char%' OR column_type LIKE '%text%' OR column_type LIKE '%varchar%' THEN
            SET where_clause = CONCAT(where_clause, ' OR ', column_name, ' LIKE "%', search_term, '%"');
        ELSEIF column_type LIKE '%date%' THEN
            SET where_clause = CONCAT(where_clause, ' OR ', column_name, ' LIKE "%', search_term, '%"');
        ELSEIF column_type LIKE '%int%' OR column_type LIKE '%decimal%' THEN
            SET where_clause = CONCAT(where_clause, ' OR ', column_name, ' = ', search_term);
        ELSEIF column_type LIKE '%boolean%' THEN
            SET where_clause = CONCAT(where_clause, ' OR ', column_name, ' = ', IF(search_term = 'true', 1, 0));
        END IF;
    END LOOP;
    
    -- Close the cursor
    CLOSE cur;
    
    -- Finalize the WHERE clause
    IF LENGTH(where_clause) > 0 THEN
        SET where_clause = SUBSTRING(where_clause, 5); -- Remove the first "OR"
        SET @sql = CONCAT('SELECT * FROM ', table_name, ' WHERE ', where_clause);
    ELSE
        SET @sql = CONCAT('SELECT * FROM ', table_name, ' WHERE 1=0'); -- No matching columns
    END IF;
    
    -- Prepare and execute the dynamic SQL statement
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
    
-- query 1, multi relation
SELECT 
    Patient.firstName,
    Patient.lastName,
    PatientAddress.StreetNo,
    PatientAddress.StreetName,
    PatientAddress.City,
    PatientAddress.State
FROM
    Patient
JOIN
    PatientAddress
ON
    Patient.AddressID = PatientAddress.AddressID;

-- Query 2, using subquery to calculate average height
SELECT
    firstName,
    lastName,
    Height
FROM
    Patient
WHERE
    Height > (SELECT AVG(Height) FROM Patient);

-- Query 3, using DOB to find age under 70
SELECT
    firstName,
    lastName,
    TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE()) AS Age
FROM
    Patient
WHERE
    TIMESTAMPDIFF(YEAR, DateOfBirth, CURDATE()) < 70;

-- Query 4, using exists, checking if a specific patient has insurance
SELECT
    CASE
        WHEN EXISTS (
            SELECT 1
            FROM Patient
            WHERE PatientID = '5037335674' AND InsuranceCheck = 1
        ) THEN 'Yes'
        ELSE 'No'
    END AS HasInsurance;

-- Query 5, prints all patients that have insurance
SELECT
    PatientID,
    firstName,
    lastName,
    CASE
        WHEN InsuranceCheck = 1 THEN 'Yes'
        ELSE 'No'
    END AS HasInsurance
FROM Patient;

-- Query 6, using group and join
SELECT 
    Patient.PatientID, 
    Patient.firstName, 
    Patient.lastName, 
    COUNT(PatientMedication.medID) AS NumberOfMedications 
FROM 
    Patient 
JOIN 
    PatientMedication ON Patient.PatientID = PatientMedication.PatientID 
GROUP BY 
    Patient.PatientID 
ORDER BY 
    NumberOfMedications DESC; 

-- Query 7, using group 
SELECT
    medicalCondition,
    COUNT(DISTINCT patientID) AS NumberOfPatients
FROM
    PatientCondition
GROUP BY
    medicalCondition;


END$$

DELIMITER ;
