import random
from faker import Faker

# Initialize Faker for generating realistic names and data
fake = Faker()

# Define counts for primary entities
num_patients = 10
num_medications = 5
num_allergies = 22
num_meal_plans = 5
num_visitors = 10
num_staff = 5
num_food_items = 10

# Multi-value counts
num_phones_per_patient = (1, 3)
num_emails_per_patient = (1, 2)
num_conditions_per_patient = (0, 5)

# Predeffined lists
allergy_names = ["Peanuts", "Shellfish", "Pollen", "Dust", "Mold", "Latex"]
food_types = ["Fruit", "Vegetable", "Grain", "Protein", "Dairy"]
health_conditions = ['Hypertension', 'Diabetes', 'Asthma', 'Heart Disease', 'Alzheimers', 'Dementia', 'Depression',
    'Heart Failure', 'Arthritis', 'Obesity', 'High Cholesterol', 'Cancer', 'Hearing loss',
    'Cataracts', "Stroke", 'Delirium', "Osteoporosis", 'Gout', 'Allergies', 'Anemia', 'Epilepsy', 'Migraine']
insurance_providers= ["Manulife", 'Sun Life', "Empire Life", "RBC Insurance Agency", 'Beneva', "Desjardins", 
                "wawanesa Insurance", "Canada Lifey"]
side_effects_list = ["Nausea", "Headache", "Dizziness", "Fatigue", "Dry mouth"]

# Store unique IDs and data to use across related tables
patient_ids = []
patients_with_insurance = []
med_ids = []
staff_ids = []
doctor_ids = []
meal_plan_ids = []
visitor_ids = []
food_names = []
all_phone_numbers = set()
all_emails = set()

# Helper functions for unique data generation
def generate_unique_id():
    while True:
        patient_id = ''.join(random.choices('0123456789', k=12))
        if patient_id not in patient_ids:
            patient_ids.append(patient_id)
            return patient_id

def generate_unique_med_id():
    while True:
        med_id = ''.join(random.choices('0123456789', k=6))
        if med_id not in med_ids:
            med_ids.append(med_id)
            return med_id

def generate_unique_staff_id():
    while True:
        staff_id = ''.join(random.choices('0123456789', k=6))
        if staff_id not in staff_ids:
            staff_ids.append(staff_id)
            return staff_id

def generate_unique_meal_plan_id():
    while True:
        meal_plan_id = ''.join(random.choices('0123456789', k=6))
        if meal_plan_id not in meal_plan_ids:
            meal_plan_ids.append(meal_plan_id)
            return meal_plan_id

def generate_unique_visitor_id():
    while True:
        visitor_id = ''.join(random.choices('0123456789', k=6))
        if visitor_id not in visitor_ids:
            visitor_ids.append(visitor_id)
            return visitor_id

def generate_unique_food_name():
    while True:
        food_name = fake.word().capitalize()
        if food_name not in food_names:
            food_names.append(food_name)
            return food_name

def generate_unique_phone():
    while True:
        phone_number = fake.phone_number().replace("'", "''")
        if phone_number not in all_phone_numbers:
            all_phone_numbers.add(phone_number)
            return phone_number

def generate_unique_email():
    while True:
        email = fake.email().replace("'", "''")
        if email not in all_emails:
            all_emails.add(email)
            return email

# File to store SQL insert statements
with open('insert_data.sql', 'w') as file:
    
    # Generate Patients
    file.write("-- Patients Table\n")
    for _ in range(num_patients):
        # Generate unique ID for the patient
        patient_id = generate_unique_id()
        
        # Composite attributes
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        
        # Simple attributes
        dob = fake.date_of_birth(minimum_age=0, maximum_age=100)
        height = fake.random_int(min=120, max=220)  # in cm
        weight = fake.random_int(min=40, max=150)   # in kg
        insurance = random.choice(['Y', 'N'])
        sex = random.choice(['M', 'F'])
        dnr_present = 'Y' if random.random() < 0.8 else 'N'  # 80% chance of Y
        
        # Composite address attribute with Canada more likely than US
        street_no = fake.building_number()
        street_name = fake.street_name().replace("'", "''")
        unit_no = fake.random_int(min=1, max=100)
        city = fake.city().replace("'", "''")
        province = fake.state_abbr()
        country = 'Canada' if random.random() < 0.7 else 'US'  # 70% Canada, 30% US
        
        # Generate SQL INSERT statement for Patients table
        patient_sql = f"""
        INSERT INTO Patients (patient_id, first_name, last_name, dob, height, weight, insurance, sex, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('{patient_id}', '{first_name}', '{last_name}', '{dob}', {height}, {weight}, '{insurance}', '{sex}', '{dnr_present}', '{street_no}', '{street_name}', {unit_no}, '{city}', '{province}', '{country}');
        """
        file.write(patient_sql + '\n')

        # Generate data for PatientPhones table
        for _ in range(random.randint(*num_phones_per_patient)):  # Each patient can have 1-3 phone numbers
            phone_number = generate_unique_phone()
            phone_sql = f"INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('{patient_id}', '{phone_number}');"
            file.write(phone_sql + '\n')

        # Generate data for PatientEmails table
        for _ in range(random.randint(*num_emails_per_patient)):  # Each patient can have 1-2 emails
            email = generate_unique_email()
            email_sql = f"INSERT INTO PatientEmails (patient_id, email) VALUES ('{patient_id}', '{email}');"
            file.write(email_sql + '\n')
            
    # Generate Staff and only keep Doctor IDs for diagnoserID in PatientMedicalConditions
    file.write("\n-- Staff Table\n")
    for _ in range(num_staff):
        staff_id = generate_unique_staff_id()
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        position = random.choice(["Nurse", "Doctor", "Administrator", "Technician"])
        department = random.choice(["Emergency", "Pediatrics", "Oncology", "Cardiology", "Radiology"])

        staff_sql = f"""
        INSERT INTO Staff (Staff_ID, firstName, lastName, Position, Department)
        VALUES ('{staff_id}', '{first_name}', '{last_name}', '{position}', '{department}');
        """
        file.write(staff_sql + '\n')

        # Add to doctor_ids list if the position is "Doctor"
        if position == "Doctor":
            doctor_ids.append(staff_id)

        # StaffPhone
        phone_number = generate_unique_phone()
        phone_sql = f"INSERT INTO StaffPhone (Staff_ID, phone) VALUES ('{staff_id}', '{phone_number}');"
        file.write(phone_sql + '\n')

    # Generate Medications
    file.write("\n-- Medications Table\n")
    for _ in range(num_medications):
        med_id = generate_unique_med_id()
        med_name = fake.word().capitalize()
        drug_class = random.choice(["Antibiotic", "Analgesic", "Antiviral", "Antidepressant"])
        administration_details = random.choice(["Oral", "Topical", "Injectable"])
        storage_details = random.choice(["Keep refrigerated", "Store at room temperature", "Avoid direct sunlight"])
        
        medication_sql = f"""
        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ({med_id}, '{med_name}', '{drug_class}', '{administration_details}', '{storage_details}');
        """
        file.write(medication_sql + '\n')
        # Generate Patient Allergies
    file.write("\n-- PatientAllergies Table\n")
    for _ in range(num_patients // 2):  # Roughly half the patients have allergies
        patient_id = random.choice(patient_ids)
        allergy_name = random.choice(allergy_names)
        severity = random.choice(["Mild", "Moderate", "Severe"])
        description = fake.sentence()
        
        patient_allergy_sql = f"""
        INSERT INTO PatientAllergies (allergyName, patientID, severity, description)
        VALUES ('{allergy_name}', '{patient_id}', '{severity}', '{description}');
        """
        file.write(patient_allergy_sql + '\n')

    # Generate MedAllergyConflict (conflicts between medications and allergies)
    file.write("\n-- MedAllergyConflict Table\n")
    for _ in range(num_medications // 2):
        med_id = random.choice(med_ids)
        allergy_name = random.choice(allergy_names)
        severity = random.choice(["Low", "Medium", "High"])
        
        med_allergy_conflict_sql = f"""
        INSERT INTO MedAllergyConflict (medID, allergyName, severity)
        VALUES ('{med_id}', '{allergy_name}', '{severity}');
        """
        file.write(med_allergy_conflict_sql + '\n')

    # Generate Patient Medical Conditions, using only doctor IDs as diagnoserID
    file.write("\n-- PatientMedicalConditions Table\n")
    for _ in range(num_patients // 2):  # Half of the patients have medical conditions
        patient_id = random.choice(patient_ids)
        condition = random.choice(health_conditions)
        description = fake.sentence().replace("'", "''")
        diagnosis_date = fake.date_this_decade()
        diagnoser_id = random.choice(doctor_ids)  # Only doctors as diagnosers

        patient_medical_condition_sql = f"""
        INSERT INTO PatientMedicalConditions (patientID, medicalCondition, description, diagnosisDate, diagnoserID)
        VALUES ('{patient_id}', '{condition}', '{description}', '{diagnosis_date}', '{diagnoser_id}');
        """
        file.write(patient_medical_condition_sql + '\n')

    # Generate MedMedConflict (conflicts between medications)
    file.write("\n-- MedMedConflict Table\n")
    for _ in range(num_medications // 3):  # Some medications conflict with others
        medication_a = random.choice(med_ids)
        medication_b = random.choice(med_ids)
        while medication_b == medication_a:
            medication_b = random.choice(med_ids)  # Ensure unique pairs
        severity = random.choice(["Low", "Medium", "High"])
        
        med_med_conflict_sql = f"""
        INSERT INTO MedMedConflict (medicationA, medicationB, severity)
        VALUES ('{medication_a}', '{medication_b}', '{severity}');
        """
        file.write(med_med_conflict_sql + '\n')

     # Generate Insurance for patients with insurance
    file.write("\n-- Insurance Table\n")
    for patient_id in patients_with_insurance:
        policy_id = fake.unique.random_int(min=1000, max=9999)
        provider = random.choice(insurance_providers)
        street_no = fake.building_number()
        street_name = fake.street_name().replace("'", "''")
        unit_no = fake.random_int(min=1, max=100)
        city = fake.city().replace("'", "''")
        province = fake.state_abbr()
        country = 'Canada' if random.random() < 0.7 else 'US'

        insurance_sql = f"""
        INSERT INTO Insurance (policyID, provider, streetNo, streetName, unitNo, city, province, country, patientID)
        VALUES ('{policy_id}', '{provider}', '{street_no}', '{street_name}', {unit_no}, '{city}', '{province}', '{country}', '{patient_id}');
        """
        file.write(insurance_sql + '\n')

        # InsuranceCoverageDetails
        coverage_details = fake.sentence().replace("'", "''")
        coverage_sql = f"INSERT INTO InsuranceCoverageDetails (policyID, coverageDetails) VALUES ('{policy_id}', '{coverage_details}');"
        file.write(coverage_sql + '\n')

    # Generate Medication Side Effects
    file.write("\n-- MedicationSideEffects Table\n")
    for med_id in med_ids:
        for _ in range(random.randint(1, 3)):  # Each medication can have 1-3 side effects
            side_effect = random.choice(side_effects_list)
            severity = random.choice(["Mild", "Moderate", "Severe"])

            side_effect_sql = f"""
            INSERT INTO MedicationSideEffects (medID, sideEffect, severity)
            VALUES ('{med_id}', '{side_effect}', '{severity}');
            """
            file.write(side_effect_sql + '\n')

    # Generate Allergies, Allergy Symptoms, and Allergy Treatments
    file.write("\n-- Allergy Table\n")
    for allergy_name in allergy_names:
        type_ = random.choice(["Food", "Environmental", "Drug"])
        management_strategy = fake.sentence().replace("'", "''")
        seasonal_considerations = random.choice(["Yes", "No"])

        allergy_sql = f"""
        INSERT INTO Allergy (allergyName, type, managementStrategy, seasonalConsiderations)
        VALUES ('{allergy_name}', '{type_}', '{management_strategy}', '{seasonal_considerations}');
        """
        file.write(allergy_sql + '\n')

        # AllergySymptoms
        for _ in range(random.randint(1, 3)):
            symptom = random.choice(["Sneezing", "Itchy eyes", "Swelling", "Hives", "Shortness of breath"])
            severity = random.choice(["Mild", "Moderate", "Severe"])
            symptom_sql = f"INSERT INTO AllergySymptoms (allergyName, symptom, severity) VALUES ('{allergy_name}', '{symptom}', '{severity}');"
            file.write(symptom_sql + '\n')

        # AllergyTreatment
        treatment = fake.sentence().replace("'", "''")
        considerations = fake.sentence().replace("'", "''")
        treatment_sql = f"INSERT INTO AllergyTreatment (allergyName, treatment, considerations) VALUES ('{allergy_name}', '{treatment}', '{considerations}');"
        file.write(treatment_sql + '\n')

    # Generate VisitorPhone
    file.write("\n-- VisitorPhone Table\n")
    for visitor_id in visitor_ids:
        phone_number = generate_unique_phone()
        visitor_phone_sql = f"INSERT INTO VisitorPhone (visitor_ID, phone) VALUES ('{visitor_id}', '{phone_number}');"
        file.write(visitor_phone_sql + '\n')

    # Generate PlanMeals
    file.write("\n-- PlanMeals Table\n")
    for meal_plan_id in meal_plan_ids:
        for _ in range(random.randint(1, 3)):  # Each plan can have 1-3 meals
            food_name = random.choice(food_names)
            portion = random.randint(1, 3)
            date = fake.date_this_year()
            time = fake.time()

            plan_meals_sql = f"""
            INSERT INTO PlanMeals (planID, foodName, portion, date, time)
            VALUES ('{meal_plan_id}', '{food_name}', {portion}, '{date}', '{time}');
            """
            file.write(plan_meals_sql + '\n')

    # Generate MealPlans
    file.write("\n-- MealPlan Table\n")
    for _ in range(num_meal_plans):
        meal_plan_id = generate_unique_meal_plan_id()
        patient_id = random.choice(patient_ids)
        date = fake.date_this_year()
        schedule = random.choice(["Breakfast", "Lunch", "Dinner"])

        meal_plan_sql = f"""
        INSERT INTO MealPlan (mealPlanID, date, schedule, patientID)
        VALUES ('{meal_plan_id}', '{date}', '{schedule}', '{patient_id}');
        """
        file.write(meal_plan_sql + '\n')

    # Generate Visitor
    file.write("\n-- Visitor Table\n")
    for _ in range(num_visitors):
        visitor_id = generate_unique_visitor_id()
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        patient_id = random.choice(patient_ids)

        visitor_sql = f"""
        INSERT INTO Visitor (visitor_ID, firstName, lastName, patient_ID)
        VALUES ('{visitor_id}', '{first_name}', '{last_name}', '{patient_id}');
        """
        file.write(visitor_sql + '\n')

    # Generate Visits
    file.write("\n-- Visit Table\n")
    for _ in range(num_visitors):
        visit_id = fake.unique.random_int(min=1000, max=9999)
        visitor_id = random.choice(visitor_ids)
        patient_id = random.choice(patient_ids)
        date = fake.date_this_year()
        time = fake.time()
        notes = fake.sentence().replace("'", "''")

        visit_sql = f"""
        INSERT INTO Visit (visitID, visitorID, patientID, date, time, notes)
        VALUES ('{visit_id}', '{visitor_id}', '{patient_id}', '{date}', '{time}', '{notes}');
        """
        file.write(visit_sql + '\n')

    # Generate Foods and Nutritional Values
    file.write("\n-- Food and FoodNutritionalVal Tables\n")
    for _ in range(num_food_items):
        food_name = generate_unique_food_name()
        food_type = random.choice(food_types)
        calories = random.randint(50, 300)
        protein = random.randint(0, 20)
        carbs = random.randint(0, 50)
        fats = random.randint(0, 20)

        food_sql = f"""
        INSERT INTO Food (foodName, type, calories, protein, carbs, fats)
        VALUES ('{food_name}', '{food_type}', {calories}, {protein}, {carbs}, {fats});
        """
        file.write(food_sql + '\n')

print("Data generation complete. SQL file saved as 'insert_data.sql'.")
