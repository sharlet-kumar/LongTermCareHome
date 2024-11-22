DELIMITER $$

CREATE PROCEDURE SearchPatientData(
    IN searchDietaryRestrictions VARCHAR(255),
    IN searchAllergy VARCHAR(255),
    IN searchCondition VARCHAR(255),
    IN searchDrugName VARCHAR(255),
    IN searchPatientName VARCHAR(255),
    IN minDOB DATE, 
    IN maxDOB DATE,
    IN insuranceProvider VARCHAR(255)
)
BEGIN
    SELECT 
        p.PatientID,
        CONCAT(p.firstName, ' ', p.lastName) AS PatientName,
        p.DateOfBirth,
        p.Sex,
        p.Weight,
        pa.streetNo, pa.streetName, pa.unitNo, pa.city, pa.state, pa.country AS Address,
        pi.provider AS InsuranceProvider,
        pc.medicalCondition AS MedicalCondition,
        a.allergyName AS Allergy,
        pm.medID AS MedicationID,
        m.medName AS MedicationName,
        mp.schedule AS MealPlanSchedule,
        f.foodname AS DietaryRestriction
    FROM 
        Patient p
    LEFT JOIN 
        PatientAddress pa ON p.AddressID = pa.AddressID
    LEFT JOIN 
        Insurance pi ON p.PatientID = pi.PatientID
    LEFT JOIN 
        PatientCondition pc ON p.PatientID = pc.patientID
    LEFT JOIN 
        PatientAllergy paa ON p.PatientID = paa.patientID
    LEFT JOIN 
        Allergy a ON paa.allergyName = a.allergyName
    LEFT JOIN 
        PatientMedication pm ON p.PatientID = pm.patientID
    LEFT JOIN 
        Medication m ON pm.medID = m.medID
    LEFT JOIN 
        MealPlan mp ON p.MealPlanID = mp.MealPlanID
    LEFT JOIN 
        Meal ml ON mp.MealPlanID = ml.MealPlanID
    LEFT JOIN 
        food f ON ml.foodName1 = f.foodname
    WHERE 
        (searchDietaryRestrictions IS NULL OR f.foodname LIKE CONCAT('%', searchDietaryRestrictions, '%'))
        AND (searchAllergy IS NULL OR a.allergyName LIKE CONCAT('%', searchAllergy, '%'))
        AND (searchCondition IS NULL OR pc.medicalCondition LIKE CONCAT('%', searchCondition, '%'))
        AND (searchDrugName IS NULL OR m.medName LIKE CONCAT('%', searchDrugName, '%'))
        AND (searchPatientName IS NULL OR CONCAT(p.firstName, ' ', p.lastName) LIKE CONCAT('%', searchPatientName, '%'))
        AND (minDOB IS NULL OR p.DateOfBirth >= minDOB)
        AND (maxDOB IS NULL OR p.DateOfBirth <= maxDOB)
        AND (insuranceProvider IS NULL OR pi.provider LIKE CONCAT('%', insuranceProvider, '%'))
    ORDER BY 
        p.PatientID;
END $$

DELIMITER ;
