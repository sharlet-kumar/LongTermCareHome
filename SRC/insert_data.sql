-- Patients Table

        INSERT INTO Patients (patient_id, first_name, last_name, dob, sex, height, weight, insurance, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('1946382308', 'Gerald', 'Guzman', '1952-10-14','M', 166, 84, 'Y', 'Y', '4476', 'Macias Road', 17, 'West Frankburgh', 'CA', 'Canada');
        
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('1946382308', '+1-539-353-1081x0643');
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('1946382308', '(631)740-1172x13910');
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('1946382308', '623.963.8439x692');
INSERT INTO PatientEmails (patient_id, email) VALUES ('1946382308', 'sandra73@example.com');
INSERT INTO PatientEmails (patient_id, email) VALUES ('1946382308', 'andersonamber@example.net');

        INSERT INTO Patients (patient_id, first_name, last_name, dob, sex, height, weight, insurance, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('9848953975', 'Heather', 'Williams', '1960-11-15','F', 127, 150, 'Y', 'Y', '0927', 'Patterson Loaf', 33, 'Jillbury', 'ND', 'US');
        
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('9848953975', '455-699-8264x020');
INSERT INTO PatientEmails (patient_id, email) VALUES ('9848953975', 'donald36@example.org');
INSERT INTO PatientEmails (patient_id, email) VALUES ('9848953975', 'austinpeters@example.com');

        INSERT INTO Patients (patient_id, first_name, last_name, dob, sex, height, weight, insurance, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('3874295759', 'Nathan', 'Schmitt', '1961-04-28','M', 123, 92, 'Y', 'N', '0005', 'Lindsay Junctions', 4, 'Colleenberg', 'LA', 'Canada');
        
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('3874295759', '(331)576-6560x4313');
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('3874295759', '+1-571-661-0761');
INSERT INTO PatientEmails (patient_id, email) VALUES ('3874295759', 'ycox@example.com');
INSERT INTO PatientEmails (patient_id, email) VALUES ('3874295759', 'elucero@example.com');

        INSERT INTO Patients (patient_id, first_name, last_name, dob, sex, height, weight, insurance, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('8104261653', 'Elizabeth', 'Combs', '1931-06-02','M', 177, 55, 'Y', 'N', '73881', 'Brent Unions', 61, 'Watersview', 'VA', 'Canada');
        
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('8104261653', '747-380-1748x37830');
INSERT INTO PatientEmails (patient_id, email) VALUES ('8104261653', 'mary41@example.org');

        INSERT INTO Patients (patient_id, first_name, last_name, dob, sex, height, weight, insurance, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('0170420117', 'Amanda', 'Gonzalez', '1973-08-03','F', 180, 48, 'N', 'Y', '20237', 'Durham Mall', 64, 'Lake Rogerstad', 'NY', 'Canada');
        
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('0170420117', '(637)240-4951x2658');
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('0170420117', '001-387-939-1960');
INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('0170420117', '+1-493-654-8135x8874');
INSERT INTO PatientEmails (patient_id, email) VALUES ('0170420117', 'vmora@example.org');

-- Staff Table

        INSERT INTO Staff (Staff_ID, firstName, lastName, Position, Department)
        VALUES ('847151', 'Jonathan', 'Robinson', 'Administrator', 'Cardiology');
        
INSERT INTO StaffPhone (Staff_ID, phone) VALUES ('847151', '278-690-8784');

        INSERT INTO Staff (Staff_ID, firstName, lastName, Position, Department)
        VALUES ('733871', 'Shelley', 'Ware', 'Nurse', 'Cardiology');
        
INSERT INTO StaffPhone (Staff_ID, phone) VALUES ('733871', '+1-224-200-2495x2022');

        INSERT INTO Staff (Staff_ID, firstName, lastName, Position, Department)
        VALUES ('132244', 'Traci', 'Simmons', 'Doctor', 'Cardiology');
        
INSERT INTO StaffPhone (Staff_ID, phone) VALUES ('132244', '(284)321-7255');

        INSERT INTO Staff (Staff_ID, firstName, lastName, Position, Department)
        VALUES ('850415', 'Paul', 'Brandt', 'Nurse', 'Cardiology');
        
INSERT INTO StaffPhone (Staff_ID, phone) VALUES ('850415', '+1-330-681-4164');

-- PatientMedicalConditions Table

        INSERT INTO PatientMedicalConditions (patientID, medicalCondition, description, diagnosisDate, diagnoserID)
        VALUES ('3874295759', 'Cataracts', 'Feel piece matter sell want garden candidate.', '2023-08-22', '132244');
        

        INSERT INTO PatientMedicalConditions (patientID, medicalCondition, description, diagnosisDate, diagnoserID)
        VALUES ('3874295759', 'High Cholesterol', 'Air head toward others stock close book pass.', '2024-09-20', '132244');
        

-- PatientStaffCare Table

        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('850415', '0170420117', 'Technician', '2024-04-21', '2024-08-31');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('132244', '9848953975', 'Primary Care', '2024-02-06', '2024-06-24');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('847151', '0170420117', 'Specialist', '2024-01-12', '2024-06-03');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('733871', '3874295759', 'Technician', '2024-07-21', '2024-08-16');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('847151', '1946382308', 'Specialist', '2024-04-11', '2024-07-19');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('733871', '3874295759', 'Technician', '2024-07-10', '2024-11-02');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('850415', '9848953975', 'Specialist', '2024-04-11', '2024-07-17');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('850415', '3874295759', 'Technician', '2024-01-19', '2024-10-31');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('847151', '1946382308', 'Specialist', '2024-01-21', '2024-02-24');
        
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('733871', '1946382308', 'Primary Care', '2024-03-29', '2024-08-24');
        
-- Insurance Table

        INSERT INTO Insurance (policyID, provider, streetNo, streetName, unitNo, city, province, country, patientID)
        VALUES ('6839', 'RBC Insurance Agency', '2541', 'Scott Ville', 79, 'Waynefort', 'MD', 'Canada', '1946382308');
        
INSERT INTO InsuranceCoverageDetails (policyID, coverageDetails) VALUES ('6839', 'Nor record program about.');

        INSERT INTO Insurance (policyID, provider, streetNo, streetName, unitNo, city, province, country, patientID)
        VALUES ('5833', 'Sun Life', '2826', 'Jonathan Bridge', 3, 'East Robert', 'OR', 'Canada', '9848953975');
        
INSERT INTO InsuranceCoverageDetails (policyID, coverageDetails) VALUES ('5833', 'Full wide information Democrat.');

        INSERT INTO Insurance (policyID, provider, streetNo, streetName, unitNo, city, province, country, patientID)
        VALUES ('3036', 'Sun Life', '3498', 'Saunders Causeway', 93, 'Kleinberg', 'GA', 'Canada', '3874295759');
        
INSERT INTO InsuranceCoverageDetails (policyID, coverageDetails) VALUES ('3036', 'Property approach art paper as continue on.');

        INSERT INTO Insurance (policyID, provider, streetNo, streetName, unitNo, city, province, country, patientID)
        VALUES ('1658', 'Desjardins', '241', 'Callahan Gateway', 79, 'Port Jamesstad', 'VA', 'Canada', '8104261653');
        
INSERT INTO InsuranceCoverageDetails (policyID, coverageDetails) VALUES ('1658', 'Suddenly teacher people investment theory.');
-- Medications Table

        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ('74867845', 'Upon', 'Antidepressant', 'Oral', 'Avoid direct sunlight');
        

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('74867845', 'Dementia');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('74867845', 'Allergies');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('74867845', 'Hypertension');
            

        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ('02828446', 'Reduce', 'Analgesic', 'Injectable', 'Store at room temperature');
        

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('02828446', 'Cataracts');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('02828446', 'Arthritis');
            

        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ('55165356', 'Car', 'Antiviral', 'Topical', 'Keep refrigerated');
        

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('55165356', 'Cancer');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('55165356', 'Hypertension');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('55165356', 'Anemia');
            

        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ('81674331', 'About', 'Analgesic', 'Topical', 'Keep refrigerated');
        

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('81674331', 'Arthritis');
            

        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ('81942911', 'Foreign', 'Analgesic', 'Oral', 'Avoid direct sunlight');
        

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('81942911', 'Anemia');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('81942911', 'Migraine');
            

        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ('77131128', 'Area', 'Antibiotic', 'Topical', 'Avoid direct sunlight');
        

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('77131128', 'Gout');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('77131128', 'Alzheimers');
            

            INSERT INTO MedicationConditions (medID, conditionName)
            VALUES ('77131128', 'Osteoporosis');
            

-- MedicationSideEffects Table

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('74867845', 'Nausea', 'Mild');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('74867845', 'Fatigue', 'Mild');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('74867845', 'Headache', 'Mild');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('02828446', 'Nausea', 'Mild');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('02828446', 'Dizziness', 'Moderate');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('55165356', 'Dizziness', 'Mild');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('55165356', 'Nausea', 'Moderate');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('81674331', 'Nausea', 'Mild');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('81674331', 'Dizziness', 'Moderate');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('81674331', 'Fatigue', 'Moderate');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('81942911', 'Dizziness', 'Mild');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('77131128', 'Headache', 'Moderate');
            

            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('77131128', 'Nausea', 'Mild');
            

-- Allergy Table

        INSERT INTO Allergy (allergyName, type, managementStrategy, seasonalConsiderations)
        VALUES ('Peanuts', 'Drug', 'American form already meeting.', 'No');
        
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Peanuts', 'Sneezing', 'Severe');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Peanuts', 'Sneezing', 'Mild');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Peanuts', 'Itchy eyes', 'Moderate');
INSERT INTO AllergyTreatment (allergyName, treatment, considerations) VALUES ('Peanuts', 'True break most green which dream will.', 'Whether other at leave.');

        INSERT INTO Allergy (allergyName, type, managementStrategy, seasonalConsiderations)
        VALUES ('Shellfish', 'Food', 'Choose great computer.', 'No');
        
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Shellfish', 'Hives', 'Severe');
INSERT INTO AllergyTreatment (allergyName, treatment, considerations) VALUES ('Shellfish', 'Exist near care others catch keep world pull.', 'Commercial say develop room trial.');

        INSERT INTO Allergy (allergyName, type, managementStrategy, seasonalConsiderations)
        VALUES ('Pollen', 'Food', 'Hand great significant sport firm quite.', 'Yes');
        
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Pollen', 'Sneezing', 'Moderate');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Pollen', 'Itchy eyes', 'Moderate');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Pollen', 'Hives', 'Severe');
INSERT INTO AllergyTreatment (allergyName, treatment, considerations) VALUES ('Pollen', 'Thought miss impact country outside research.', 'None government near get hear game.');

        INSERT INTO Allergy (allergyName, type, managementStrategy, seasonalConsiderations)
        VALUES ('Dust', 'Drug', 'American hour someone card.', 'No');
        
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Dust', 'Swelling', 'Mild');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Dust', 'Shortness of breath', 'Moderate');
INSERT INTO AllergyTreatment (allergyName, treatment, considerations) VALUES ('Dust', 'Mother political shoulder detail sort.', 'Race common finish reduce.');

        INSERT INTO Allergy (allergyName, type, managementStrategy, seasonalConsiderations)
        VALUES ('Mold', 'Food', 'Professional new politics ask research and list.', 'No');
        
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Mold', 'Swelling', 'Mild');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Mold', 'Sneezing', 'Moderate');
INSERT INTO AllergyTreatment (allergyName, treatment, considerations) VALUES ('Mold', 'Try nothing course force.', 'Matter TV perform baby hand.');

        INSERT INTO Allergy (allergyName, type, managementStrategy, seasonalConsiderations)
        VALUES ('Latex', 'Drug', 'Unit above some direction government game admit.', 'Yes');
        
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Latex', 'Swelling', 'Moderate');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Latex', 'Swelling', 'Moderate');
INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('Latex', 'Shortness of breath', 'Mild');
INSERT INTO AllergyTreatment (allergyName, treatment, considerations) VALUES ('Latex', 'Market husband treatment follow.', 'Hotel physical author then.');

-- PatientAllergies Table

        INSERT INTO PatientAllergies (allergyName, patientID, severity, description)
        VALUES ('Shellfish', '9848953975', 'Mild', 'Involve shake with example box.');
        

        INSERT INTO PatientAllergies (allergyName, patientID, severity, description)
        VALUES ('Mold', '1946382308', 'Severe', 'Ten man look maybe.');
        

-- Visitor Table

        INSERT INTO Visitor (visitor_ID, firstName, lastName, patient_ID)
        VALUES ('898428', 'Benjamin', 'Cooke', '3874295759');
        

-- Visit Table

        INSERT INTO Visit (visitID, visitorID, patientID, date, time, notes)
        VALUES ('7318', '898428', '9848953975', '2024-04-03', '14:09:21', 'Indicate note might fear peace light.');
        

-- VisitorPhone Table
INSERT INTO VisitorPhone (visitor_ID, phone) VALUES ('898428', '539.453.0406');

-- Food and FoodNutritionalVal Tables

        INSERT INTO Food (foodName, type, calories, protein, carbs, fats)
        VALUES ('Else', 'Vegetable', 225, 17, 46, 11);
        

        INSERT INTO Food (foodName, type, calories, protein, carbs, fats)
        VALUES ('Beautiful', 'Grain', 247, 11, 28, 11);
        

        INSERT INTO Food (foodName, type, calories, protein, carbs, fats)
        VALUES ('Seem', 'Dairy', 71, 17, 16, 17);
        

-- MedAllergyConflict Table

        INSERT INTO MedAllergyConflict (medID, allergyName, severity)
        VALUES ('74867845', 'Latex', 'High');
        

        INSERT INTO MedAllergyConflict (medID, allergyName, severity)
        VALUES ('74867845', 'Mold', 'Low');
        

        INSERT INTO MedAllergyConflict (medID, allergyName, severity)
        VALUES ('02828446', 'Peanuts', 'High');
        
-- MedMedConflict Table
INSERT INTO MedMedConflict (medicationA, medicationB, severity) VALUES ('74867845', '81942911', 'High');

-- MealPlan Table

        INSERT INTO MealPlan (mealPlanID, date, schedule, patientID)
        VALUES ('115854', '2024-10-15', 'Breakfast', '0170420117');
        

        INSERT INTO MealPlan (mealPlanID, date, schedule, patientID)
        VALUES ('236298', '2024-08-02', 'Dinner', '0170420117');
        

        INSERT INTO MealPlan (mealPlanID, date, schedule, patientID)
        VALUES ('764761', '2024-07-03', 'Dinner', '3874295759');
        

        INSERT INTO MealPlan (mealPlanID, date, schedule, patientID)
        VALUES ('706054', '2024-03-21', 'Dinner', '3874295759');
        

        INSERT INTO MealPlan (mealPlanID, date, schedule, patientID)
        VALUES ('348493', '2024-10-17', 'Lunch', '9848953975');
        

-- PlanMeals Table

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('115854', 'Else', 2, '2024-10-18', '22:44:05');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('115854', 'Seem', 1, '2024-09-23', '21:34:06');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('115854', 'Beautiful', 2, '2024-08-24', '02:14:20');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('236298', 'Seem', 2, '2024-03-10', '12:56:04');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('236298', 'Seem', 2, '2024-07-11', '16:58:55');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('236298', 'Seem', 3, '2024-11-10', '17:59:16');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('764761', 'Beautiful', 1, '2024-06-18', '12:12:22');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('706054', 'Seem', 3, '2024-08-08', '09:38:44');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('706054', 'Seem', 1, '2024-09-15', '19:14:45');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('706054', 'Else', 3, '2024-08-21', '11:40:33');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('348493', 'Seem', 2, '2024-01-16', '14:36:55');
            

            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('348493', 'Else', 1, '2024-01-18', '16:50:49');
            
-- PatientMedication Table

                INSERT INTO PatientMedication (PatientID, medID, dosage, AdminSchedule, prescribingDocID)
                VALUES ('3874295759', '02828446', 10, 'Twice a Day', '132244');
                

                INSERT INTO PatientMedication (PatientID, medID, dosage, AdminSchedule, prescribingDocID)
                VALUES ('3874295759', '77131128', 30, 'Evening', '132244');
                
