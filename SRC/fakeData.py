import random
from faker import Faker

# Initialize Faker for generating realistic names and data
fake = Faker()

# Define counts for primary entities
num_patients = 5
num_medications = 6
num_meal_plans = 5
num_visitors = 1
num_staff = 4
num_food_items = 3

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

patient_conditions = {}  # {patient_id: [condition1, condition2, ...]}
medication_condition_map = {}  # {med_id: [condition1, condition2, ...]}
med_med_conflicts = []  # [(med_a, med_b)]
patient_allergy_map = {}  # {patient_id: [allergy1, allergy2, ...]}
medication_allergy_map = {}  # {med_id: [allergy1, allergy2, ...]}

# Helper functions for unique data generation
def generate_unique_id():
    while True:
        patient_id = ''.join(random.choices('0123456789', k=10))
        if patient_id not in patient_ids:
            patient_ids.append(patient_id)
            return patient_id

def generate_unique_med_id():
    while True:
        med_id = ''.join(random.choices('0123456789', k=8))
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
        dob = fake.date_of_birth(minimum_age=50, maximum_age=100)
        height = fake.random_int(min=120, max=220)  # in cm
        weight = fake.random_int(min=40, max=150)   # in kg
        insurance = random.choice(['Y', 'N'])
        sex = random.choice(['M', 'F'])
        dnr_present = 'Y' if random.random() < 0.8 else 'N'  # 80% chance of Y

        if insurance == 'Y':
            patients_with_insurance.append(patient_id)

        # Composite address attribute with Canada more likely than US
        street_no = fake.building_number()
        street_name = fake.street_name().replace("'", "''")
        unit_no = fake.random_int(min=1, max=100)
        city = fake.city().replace("'", "''")
        province = fake.state_abbr()
        country = 'Canada' if random.random() < 0.7 else 'US'  # 70% Canada, 30% US
        
        # Generate SQL INSERT statement for Patients table
        patient_sql = f"""
        INSERT INTO Patients (patient_id, first_name, last_name, dob, sex, height, weight, insurance, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('{patient_id}', '{first_name}', '{last_name}', '{dob}','{sex}', {height}, {weight}, '{insurance}', '{dnr_present}', '{street_no}', '{street_name}', {unit_no}, '{city}', '{province}', '{country}');
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

# Generate Patient Medical Conditions, using only doctor IDs as diagnoserID
    file.write("\n-- PatientMedicalConditions Table\n")
    for _ in range(num_patients // 2):  # Half of the patients have medical conditions
        patient_id = random.choice(patient_ids)
        condition = random.choice(health_conditions)
        description = fake.sentence().replace("'", "''")
        diagnosis_date = fake.date_this_decade()
        diagnoser_id = random.choice(doctor_ids)  # Only doctors as diagnosers

        patient_conditions[patient_id] = random.sample(health_conditions, random.randint(*num_conditions_per_patient))

        patient_medical_condition_sql = f"""
        INSERT INTO PatientMedicalConditions (patientID, medicalCondition, description, diagnosisDate, diagnoserID)
        VALUES ('{patient_id}', '{condition}', '{description}', '{diagnosis_date}', '{diagnoser_id}');
        """
        file.write(patient_medical_condition_sql + '\n')

# Generate PatientStaffCare
    file.write("\n-- PatientStaffCare Table\n")
    for _ in range(num_patients * 2):  # Assign each patient to at least one staff member
        staff_id = random.choice(staff_ids)
        patient_id = random.choice(patient_ids)
        staff_role = random.choice(["Primary Care", "Specialist", "Technician", "Nurse"])
        care_start_date = fake.date_this_year()
        care_end_date = fake.date_this_year()
        
        # Ensure care_end_date is after care_start_date
        if care_end_date < care_start_date:
            care_start_date, care_end_date = care_end_date, care_start_date

        patient_staff_care_sql = f"""
        INSERT INTO PatientStaffCare (staffID, patientID, staffRoleInCare, careStartDate, careEndDate)
        VALUES ('{staff_id}', '{patient_id}', '{staff_role}', '{care_start_date}', '{care_end_date}');
        """
        file.write(patient_staff_care_sql)

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

# Generate Medications
    file.write("-- Medications Table\n")
    
    # Generate Medications
    for _ in range(num_medications):
        med_id = generate_unique_med_id()
        med_name = fake.word().capitalize()
        drug_class = random.choice(["Antibiotic", "Analgesic", "Antiviral", "Antidepressant"])
        administration_details = random.choice(["Oral", "Topical", "Injectable"])
        storage_details = random.choice(["Keep refrigerated", "Store at room temperature", "Avoid direct sunlight"])

        # Generate treated conditions for this medication
        treated_conditions = random.sample(health_conditions, random.randint(1, 3))
        medication_condition_map[med_id] = treated_conditions

        # Insert into Medication table
        medication_sql = f"""
        INSERT INTO Medication (medID, medName, drugClass, administrationDetails, storageDetails)
        VALUES ('{med_id}', '{med_name}', '{drug_class}', '{administration_details}', '{storage_details}');
        """
        file.write(medication_sql + '\n')

# Generate entries for MedsTreatCondition table
    for condition in treated_conditions:
        meds_treat_condition_sql = f"""
        INSERT INTO MedsTreatCondition (medID, conditionName)
        VALUES ('{med_id}', '{condition}');
        """
        file.write(meds_treat_condition_sql + '\n')


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

 # Generate Patient Allergies
    file.write("\n-- PatientAllergies Table\n")
    for _ in range(num_patients // 2):  # Roughly half the patients have allergies
        patient_id = random.choice(patient_ids)
        allergy_name = random.choice(allergy_names)
        severity = random.choice(["Mild", "Moderate", "Severe"])
        description = fake.sentence()

        patient_allergy_map[patient_id] = random.sample(allergy_names, random.randint(0, 3))

        
        patient_allergy_sql = f"""
        INSERT INTO PatientAllergies (allergyName, patientID, severity, description)
        VALUES ('{allergy_name}', '{patient_id}', '{severity}', '{description}');
        """
        file.write(patient_allergy_sql + '\n')

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

# Generate VisitorPhone
    file.write("\n-- VisitorPhone Table\n")
    for visitor_id in visitor_ids:
        phone_number = generate_unique_phone()
        visitor_phone_sql = f"INSERT INTO VisitorPhone (visitor_ID, phone) VALUES ('{visitor_id}', '{phone_number}');"
        file.write(visitor_phone_sql + '\n')

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


# Generate MedMedConflict (conflicts between medications)
    file.write("-- MedMedConflict Table\n")
    med_ids_list = list(medication_condition_map.keys())
    for _ in range(len(med_ids_list) // 3):  # About 1/3 of meds have conflicts
        med_a = random.choice(med_ids_list)
        med_b = random.choice(med_ids_list)
        while med_b == med_a:
            med_b = random.choice(med_ids_list)
        severity = random.choice(["Low", "Medium", "High"])
        
        med_med_conflicts.append((med_a, med_b))
    file.write(f"INSERT INTO MedMedConflict (medicationA, medicationB, severity) VALUES ('{med_a}', '{med_b}', 'High');\n")

#Generate MealPlans
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

# Generate Meal
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

# Generate PatientMedication
    file.write("-- PatientMedication Table\n")
    for patient_id, conditions in patient_conditions.items():
        assigned_medications = set()  # Track medications already assigned to this patient

        for condition in conditions:
            # Find medications that treat this condition
            meds_for_condition = [
                med_id for med_id, treated_conditions in medication_condition_map.items()
                if condition in treated_conditions
            ]

            # Filter medications to avoid conflicts
            suitable_meds = []
            for med_id in meds_for_condition:
                # Check for allergy conflicts
                patient_allergies = patient_allergy_map.get(patient_id, [])
                if any(allergy in medication_allergy_map.get(med_id, []) for allergy in patient_allergies):
                    continue  # Skip this medication due to allergy conflict

                # Check for medication conflicts
                conflicting_meds = [
                    med_b for med_a, med_b in med_med_conflicts if med_a == med_id or med_b == med_id
                ]
                if any(med in assigned_medications for med in conflicting_meds):
                    continue  # Skip this medication due to medication conflict

                # Add to suitable medications if no conflicts
                suitable_meds.append(med_id)

            # Assign a suitable medication if available
            if suitable_meds:
                medication = random.choice(suitable_meds)
                prescribing_doc = random.choice(doctor_ids) if doctor_ids else None
                dosage = random.randint(1, 3) * 10  # e.g., 10mg, 20mg, 30mg
                admin_schedule = random.choice(["Morning", "Evening", "Twice a Day"])

                patient_medication_sql = f"""
                INSERT INTO PatientMedication (PatientID, medID, dosage, AdminSchedule, prescribingDocID)
                VALUES ('{patient_id}', '{medication}', {dosage}, '{admin_schedule}', '{prescribing_doc}');
                """
                file.write(patient_medication_sql + '\n')

                # Track assigned medication
                assigned_medications.add(medication)

print("Data generation complete. SQL file saved as 'insert_data.sql'.")
