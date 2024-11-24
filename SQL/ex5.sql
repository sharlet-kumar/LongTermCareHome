DELIMITER //

CREATE PROCEDURE Search_All(
    IN search_term VARCHAR(255)
)
BEGIN
    -- Search the Patient table
    SELECT * FROM Patient 
    WHERE PatientID LIKE CONCAT('%', search_term, '%') 
    OR firstName LIKE CONCAT('%', search_term, '%') 
    OR lastName LIKE CONCAT('%', search_term, '%')
    OR Sex LIKE CONCAT('%', search_term, '%') 
    OR DateOfBirth LIKE CONCAT('%', search_term, '%')
    OR Height LIKE CONCAT('%', search_term, '%')
    OR Weight LIKE CONCAT('%', search_term, '%');
    
    -- Search the PatientAddress table
    SELECT * FROM PatientAddress
    WHERE AddressID LIKE CONCAT('%', search_term, '%') 
    OR StreetNo LIKE CONCAT('%', search_term, '%') 
    OR StreetName LIKE CONCAT('%', search_term, '%')
    OR UnitNo LIKE CONCAT('%', search_term, '%') 
    OR City LIKE CONCAT('%', search_term, '%')
    OR State LIKE CONCAT('%', search_term, '%')
    OR Country LIKE CONCAT('%', search_term, '%');
    
    -- Search the Staff table
    SELECT * FROM Staff
    WHERE staffID LIKE CONCAT('%', search_term, '%')
    OR firstName LIKE CONCAT('%', search_term, '%')
    OR lastName LIKE CONCAT('%', search_term, '%') 
    OR position LIKE CONCAT('%', search_term, '%') 
    OR department LIKE CONCAT('%', search_term, '%');
    
    -- Search the Medication table
    SELECT * FROM Medication
    WHERE medID LIKE CONCAT('%', search_term, '%') 
    OR medName LIKE CONCAT('%', search_term, '%') 
    OR drugclass LIKE CONCAT('%', search_term, '%')
    OR adminDetails LIKE CONCAT('%', search_term, '%') 
    OR storagedetails LIKE CONCAT('%', search_term, '%');
    
    -- Search the PatientCondition table
    SELECT * FROM PatientCondition
    WHERE patientID LIKE CONCAT('%', search_term, '%')
    OR medicalCondition LIKE CONCAT('%', search_term, '%') 
    OR description LIKE CONCAT('%', search_term, '%')
    OR diagnoserID LIKE CONCAT('%', search_term, '%');
    
    -- Search the Allergy table
    SELECT * FROM Allergy
    WHERE allergyName LIKE CONCAT('%', search_term, '%')
    OR managementStrategy LIKE CONCAT('%', search_term, '%')
    OR seasonalconsiderations LIKE CONCAT('%', search_term, '%');
    
    -- Search the Visit table
    SELECT * FROM Visit
    WHERE visitID LIKE CONCAT('%', search_term, '%')
    OR visitorID LIKE CONCAT('%', search_term, '%')
    OR patientID LIKE CONCAT('%', search_term, '%') 
    OR VisitDate LIKE CONCAT('%', search_term, '%') 
    OR notes LIKE CONCAT('%', search_term, '%');
    
    -- Add additional SELECT queries for any other tables as needed
    -- For example, if you want to search the food table:
    SELECT * FROM food
    WHERE foodname LIKE CONCAT('%', search_term, '%')
    OR foodgroup LIKE CONCAT('%', search_term, '%')
    OR calories LIKE CONCAT('%', search_term, '%')
    OR protein LIKE CONCAT('%', search_term, '%')
    OR fats LIKE CONCAT('%', search_term, '%');
    
END //

DELIMITER ;
