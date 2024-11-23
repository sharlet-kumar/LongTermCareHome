import random
from faker import Faker
import csv

# Initialize Faker for generating realistic names and data
fake = Faker()

# Define counts for primary entities
num_patients = 50
num_medications = 60
num_meal_plans = 5
num_visitors = 1
num_staff = 40
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
food_allergy_conflicts = []

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
        
def generate_csv_writer(file_name, fieldnames):
    file = open(file_name, 'w', newline='')
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    return writer, file

# Open CSV files
csv_files = {
    "Patients.csv": ['patient_id', 'first_name', 'last_name', 'dob', 'sex', 'height', 'weight', 'insurance', 'dnr_present', 'street_no', 'street_name', 'unit_no', 'city', 'province', 'country'],
    "Medications.csv": ['med_id', 'med_name', 'drug_class', "administration_details", 'storage_details'],
    "PatientPhone.csv": ['patient_id', 'phone_number'],
    "PatientEmail.csv": ['patient_id', 'email'],
    "Staff.csv": ['staff_id', 'first_name', 'last_name', 'position', 'department'],
    "StaffPhone.csv": ['staff_id', 'phone_number'],
    "PatientMedicalConditions.csv": ['patient_id', 'medical_condition', 'description', 'diagnosis_date', 'diagnoser_id'],
    "PatientStaffCare.csv": ['staff_id', 'patient_id', 'staff_role_in_care', 'care_start_date', 'care_end_date'],
    "Insurance.csv": ['policy_id', 'provider', 'street_no', 'street_name', 'unit_no', 'city', 'province', 'country', 'patient_id'],
    "InsuranceCoverageDetails.csv": ['policy_id', 'coverage_details'],
    "MedsTreatCondition.csv": ['med_id', 'condition_name'],
    "MedSideEffects.csv": ['med_id', 'side_effect', 'severity'],
    "Allergy.csv": ['allergy_name', 'type', 'management_strategy', 'seasonal_considerations'],
    "AllergySymptom.csv": ['allergy_name', 'symptom', 'severity'],
    "AllergyTreatment.csv": ['allergy_name', 'treatment', 'considerations'],
    "PatientAllergies.csv": ['allergy_name', 'patient_id', 'severity', 'description'],
    "visitor.csv": ['visitor_id', 'first_name', 'last_name', 'patient_id'],
    "Visits.csv": ['visit_id', 'visitor_id', 'patient_id', 'date', 'time', 'notes'],
    "VisitorPhone.csv": ['visitor_id', 'phone_number'],
    "FoodAndNutrition.csv": ['food_name', 'type', 'calories', 'protein', 'carbs', 'fats'],
    "MedAllergyConflict.csv": ['med_id', 'allergy_name', 'severity'],
    "MedMedConflict.csv": ['med_A', 'med_B', 'severity'],
    "MealPlans.csv": ['meal_plan_id', 'date', 'schedule', 'patient_id'],
    "Meal.csv": ['plan_id', 'food_name', 'portion', 'date', 'time'],
    "FoodAllergyConflict.csv": ['food_name', 'allergy_name'],
    "PatientMedication.csv": ['patient_id', 'med_id', 'dosage', 'admin_schedule', 'prescribing_doc_id']
}

# Open all files and their corresponding writers
file_handles = {}
writers = {}

try:
    # Open files and initialize CSV writers
    for filename, fieldnames in csv_files.items():
        file_handles[filename] = open(filename, 'w', newline='')
        writers[filename] = csv.DictWriter(file_handles[filename], fieldnames=fieldnames)
        writers[filename].writeheader()

    
# Generate Patients
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
        
        patient_writer = writers["Patients.csv"]
        patient_writer.writerow({"patient_id": patient_id, "first_name": first_name, "last_name": last_name, 'dob': dob, 'sex': sex, 'height': height, 'weight': weight, 'insurance': insurance, 'dnr_present': dnr_present, 'street_no': street_no, 'street_name': street_name, 'unit_no': unit_no, 'city': city, 'province' : province, 'country': country })

        # Generate data for PatientPhones table
        for _ in range(random.randint(*num_phones_per_patient)):  # Each patient can have 1-3 phone numbers
            phone_number = generate_unique_phone()

            patient_phone_writer=writers["PatientPhone.csv"]
            patient_phone_writer.writerow({'patient_id':patient_id, 'phone_number': phone_number})
        

        # Generate data for PatientEmails table
        for _ in range(random.randint(*num_emails_per_patient)):  # Each patient can have 1-2 emails
            email = generate_unique_email()

            patient_email_writer=writers["PatientEmail.csv"]
            patient_email_writer.writerow({'patient_id':patient_id, 'email': email})
            
# Generate Staff and only keep Doctor IDs for diagnoserID in PatientMedicalConditions
    for _ in range(num_staff):
        staff_id = generate_unique_staff_id()
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        position = random.choice(["Nurse", "Doctor", "Administrator", "Technician"])
        department = random.choice(["Emergency", "Pediatrics", "Oncology", "Cardiology", "Radiology"])

        staff_writer=writers["Staff.csv"]
        staff_writer.writerow({'staff_id':staff_id, 'first_name':first_name, 'last_name': last_name, 'position':position, 'department':department})
        # Add to doctor_ids list if the position is "Doctor"
        if position == "Doctor":
            doctor_ids.append(staff_id)

        # StaffPhone
        phone_number = generate_unique_phone()

        staff_phone_writer=writers["StaffPhone.csv"]
        staff_phone_writer.writerow({'staff_id':staff_id, 'phone_number': phone_number})

# Generate Patient Medical Conditions, using only doctor IDs as diagnoserID
    for _ in range(num_patients // 2):  # Assign medical conditions to half of the patients
        patient_id = random.choice(patient_ids)
        condition = random.choice(health_conditions)
        description = fake.sentence().replace("'", "''")
        diagnosis_date = fake.date_this_decade()
        diagnoser_id = random.choice(doctor_ids)  # Only doctors can be diagnosers

        # Ensure consistent tracking of conditions for each patient
        if patient_id not in patient_conditions:
            patient_conditions[patient_id] = []
        patient_conditions[patient_id].append(condition)

        # Write to the CSV file
        patient_medical_conditions_writer = writers["PatientMedicalConditions.csv"]
        patient_medical_conditions_writer.writerow({
            'patient_id': patient_id,
            'medical_condition': condition,
            'description': description,
            'diagnosis_date': diagnosis_date,
            'diagnoser_id': diagnoser_id
        })

# Generate PatientStaffCare
    for _ in range(num_patients * 2):  # Assign each patient to at least one staff member
        staff_id = random.choice(staff_ids)
        patient_id = random.choice(patient_ids)
        staff_role = random.choice(["Primary Care", "Specialist", "Technician", "Nurse"])
        care_start_date = fake.date_this_year()
        care_end_date = fake.date_this_year()
        
        # Ensure care_end_date is after care_start_date
        if care_end_date < care_start_date:
            care_start_date, care_end_date = care_end_date, care_start_date

        patient_staff_care_writer=writers["PatientStaffCare.csv"]
        patient_staff_care_writer.writerow({'staff_id':staff_id, 'patient_id' :patient_id, 'staff_role_in_care':staff_role, 'care_start_date':care_start_date, 'care_end_date': care_end_date})

# Generate Insurance for patients with insurance
    for patient_id in patients_with_insurance:
        policy_id = fake.unique.random_int(min=1000, max=9999)
        provider = random.choice(insurance_providers)
        street_no = fake.building_number()
        street_name = fake.street_name().replace("'", "''")
        unit_no = fake.random_int(min=1, max=100)
        city = fake.city().replace("'", "''")
        province = fake.state_abbr()
        country = 'Canada' if random.random() < 0.7 else 'US'

        insurance_writer=writers["Insurance.csv"]
        insurance_writer.writerow({'policy_id':policy_id, 'provider':provider, 'street_no':street_no, 'street_name':street_no, 'unit_no': unit_no, 'city' :city, 'province' :provider, 'country' :country, 'patient_id' :patient_id})

        # InsuranceCoverageDetails
        coverage_details = fake.sentence().replace("'", "''")

        insurance_coverage_details_writer=writers["InsuranceCoverageDetails.csv"]
        insurance_coverage_details_writer.writerow({'policy_id':policy_id, 'coverage_details':coverage_details})
    
    # Generate Medications and their single treatment
    for _ in range(num_medications):
        med_id = generate_unique_med_id()
        med_name = fake.word().capitalize()
        drug_class = random.choice(["Antibiotic", "Analgesic", "Antiviral", "Antidepressant"])
        administration_details = random.choice(["Oral", "Topical", "Injectable"])
        storage_details = random.choice(["Keep refrigerated", "Store at room temperature", "Avoid direct sunlight"])

        # Assign a single treated condition for this medication
        treated_condition = random.choice(health_conditions)
        medication_condition_map[med_id] = treated_condition

        # Write medication details to Medications.csv
        medication_writer = writers["Medications.csv"]
        medication_writer.writerow({
            'med_id': med_id,
            'med_name': med_name,
            'drug_class': drug_class,
            "administration_details": administration_details,
            'storage_details': storage_details
        })

        # Write the single treated condition to MedsTreatCondition.csv
        treat_conditions_writer = writers["MedsTreatCondition.csv"]
        treat_conditions_writer.writerow({'med_id': med_id, 'condition_name': treated_condition})

# Generate Medication Side Effects
    for med_id in med_ids:
        for _ in range(random.randint(1, 3)):  # Each medication can have 1-3 side effects
            side_effect = random.choice(side_effects_list)
            severity = random.choice(["Mild", "Moderate", "Severe"])

            med_side_effects_write=writers["MedSideEffects.csv"]
            med_side_effects_write.writerow({'med_id':med_id, 'side_effect':side_effect, 'severity':severity})

# Generate Allergies, Allergy Symptoms, and Allergy Treatments
    for allergy_name in allergy_names:
        # Generate Allergy information
        type = random.choice(["Food", "Environmental", "Drug"])
        management_strategy = fake.sentence().replace("'", "''")
        seasonal_considerations = random.choice(["Yes", "No"])

        allergy_write = writers["Allergy.csv"]
        allergy_write.writerow({ 'allergy_name': allergy_name,
            'type': type,
            'management_strategy': management_strategy,
            'seasonal_considerations': seasonal_considerations
        })

        # Generate Symptoms for each Allergy
        for _ in range(random.randint(1, 3)):
            symptom = random.choice(["Sneezing", "Itchy eyes", "Swelling", "Hives", "Shortness of breath"])
            severity = random.choice(["Mild", "Moderate", "Severe"])

            allergy_symptom_write = writers["AllergySymptom.csv"]
            allergy_symptom_write.writerow({
                'allergy_name': allergy_name,
                'symptom': symptom,
                'severity': severity
            })

        # Generate Treatment for each Allergy
        treatment = fake.sentence().replace("'", "''")
        considerations = fake.sentence().replace("'", "''")

        allergy_treatment_write = writers["AllergyTreatment.csv"]
        allergy_treatment_write.writerow({
            'allergy_name': allergy_name,
            'treatment': treatment,
            'considerations': considerations
        })

    # Generate Patient Allergies
    for patient_id in patient_ids[:len(patient_ids) // 2]:  # Assign allergies to roughly half the patients
        # Ensure no duplicate allergies for a patient
        patient_allergies = random.sample(allergy_names, random.randint(1, 3))
        patient_allergy_map[patient_id] = patient_allergies

        for allergy_name in patient_allergies:
            severity = random.choice(["Mild", "Moderate", "Severe"])
            description = fake.sentence()

            patient_allergies_write = writers["PatientAllergies.csv"]
            patient_allergies_write.writerow({
                'allergy_name': allergy_name,
                'patient_id': patient_id,
                'severity': severity,
                'description': description
            })

# Generate Visitor
    for _ in range(num_visitors):
        visitor_id = generate_unique_visitor_id()
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        patient_id = random.choice(patient_ids)

        visitor_write=writers["visitor.csv"]
        visitor_write.writerow({'visitor_id':visitor_id, 'first_name':first_name, 'last_name':last_name, 'patient_id':patient_id})

# Generate Visits
    for _ in range(num_visitors):
        visit_id = fake.unique.random_int(min=1000, max=9999)
        visitor_id = random.choice(visitor_ids)
        patient_id = random.choice(patient_ids)
        date = fake.date_this_year()
        time = fake.time()
        notes = fake.sentence().replace("'", "''")

        visits_write=writers["Visits.csv"]
        visits_write.writerow({'visit_id':visit_id, 'visitor_id':visitor_id, 'patient_id':patient_id, 'date':date, 'time':time, 'notes':notes})

# Generate VisitorPhone
    for visitor_id in visitor_ids:
        phone_number = generate_unique_phone()

        visitor_phone_writer=writers["VisitorPhone.csv"]
        visitor_phone_writer.writerow({'visitor_id':visitor_id, 'phone_number':phone_number})

 # Generate Foods and Nutritional Values
    for _ in range(num_food_items):
        food_name = generate_unique_food_name()
        food_type = random.choice(food_types)
        calories = random.randint(50, 300)
        protein = random.randint(0, 20)
        carbs = random.randint(0, 50)
        fats = random.randint(0, 20)

        food_nutrition_writer=writers["FoodAndNutrition.csv"]
        food_nutrition_writer.writerow({'food_name':food_name, 'type':type, 'calories':calories, 'protein':protein, 'carbs':carbs, 'fats':fats})

# Generate MedAllergyConflict (conflicts between medications and allergies)
    for _ in range(num_medications // 2):
        med_id = random.choice(med_ids)
        allergy_name = random.choice(allergy_names)
        severity = random.choice(["Low", "Medium", "High"])
        
        med_allergy_conflict_writer=writers["MedAllergyConflict.csv"]
        med_allergy_conflict_writer.writerow({'med_id':med_id, 'allergy_name':allergy_name, 'severity':severity})


# Medication Conflicts
    med_ids_list = list(medication_condition_map.keys())
    for _ in range(len(med_ids_list) // 3):  # About 1/3 of meds have conflicts
        med_a = random.choice(med_ids_list)
        med_b = random.choice(med_ids_list)
        while med_b == med_a:
            med_b = random.choice(med_ids_list)  # Ensure unique pairs
        med_med_conflicts.append((med_a, med_b))

        med_med_conflict_writer = writers["MedMedConflict.csv"]
        med_med_conflict_writer.writerow({'med_A': med_a, 'med_B': med_b, 'severity': random.choice(["Low", "Medium", "High"])})


## Generate FoodAllergyConflict
    for _ in range(num_food_items * 2):  # Randomly create conflicts for some food items
        food_name = random.choice(food_names)
        allergy_name = random.choice(allergy_names)

        # Write the conflict to the CSV file
        food_allergy_conflict_writer = writers["FoodAllergyConflict.csv"]
        food_allergy_conflict_writer.writerow({
            'food_name': food_name,
            'allergy_name': allergy_name,
    })

# Generate MealPlans for each patient
    for patient_id in patient_ids:
        meal_plan_id = generate_unique_meal_plan_id()
        date = fake.date_this_year()
        schedule = random.choice(["Breakfast", "Lunch", "Dinner"])

        meal_plans_writer = writers["MealPlans.csv"]
        meal_plans_writer.writerow({
            'meal_plan_id': meal_plan_id,
            'date': date,
            'schedule': schedule,
            'patient_id': patient_id
        })

        # Add the meal plan ID to the meal_plan_ids list
        meal_plan_ids.append(meal_plan_id)

    # Optionally generate additional random meal plans
    for _ in range(num_meal_plans):  # num_meal_plans is additional meal plans
        meal_plan_id = generate_unique_meal_plan_id()
        patient_id = random.choice(patient_ids)
        date = fake.date_this_year()
        schedule = random.choice(["Breakfast", "Lunch", "Dinner"])

        meal_plans_writer = writers["MealPlans.csv"]
        meal_plans_writer.writerow({
            'meal_plan_id': meal_plan_id,
            'date': date,
            'schedule': schedule,
            'patient_id': patient_id
        })

        # Add the meal plan ID to the meal_plan_ids list
        meal_plan_ids.append(meal_plan_id)

    # Generate Meals for all meal plans
    for meal_plan_id in meal_plan_ids:
        for _ in range(random.randint(1, 3)):  # Each plan can have 1-3 meals
            food_name = random.choice(food_names)
            portion = random.randint(1, 3)
            date = fake.date_this_year()
            time = fake.time()

            meal_writer = writers["Meal.csv"]
            meal_writer.writerow({
                'plan_id': meal_plan_id,
                'food_name': food_name,
                'portion': portion,
                'date': date,
                'time': time
            })

# Generate PatientMedication
    for patient_id, conditions in patient_conditions.items():
        assigned_medications = set()  # Track medications already assigned to this patient

        for condition in conditions:
            # Find medications that treat this condition
            meds_for_condition = [
                med_id for med_id, treated_condition in medication_condition_map.items()
                if treated_condition == condition
            ]

            # Filter medications to avoid conflicts
            suitable_meds = []
            for med_id in meds_for_condition:
                # Check for allergy conflicts
                patient_allergies = patient_allergy_map.get(patient_id, [])
                med_allergies = medication_allergy_map.get(med_id, [])
                if any(allergy in med_allergies for allergy in patient_allergies):
                    continue  # Skip this medication due to allergy conflict

                # Check for medication conflicts
                conflicting_meds = [
                    med_b for med_a, med_b in med_med_conflicts if med_a == med_id or med_b == med_id
                ]
                if any(assigned_med in assigned_medications for assigned_med in conflicting_meds):
                    continue  # Skip this medication due to medication conflict

                # Add to suitable medications if no conflicts
                suitable_meds.append(med_id)

            # Assign a suitable medication if available
            if suitable_meds:
                medication = random.choice(suitable_meds)
                prescribing_doc = random.choice(doctor_ids) if doctor_ids else None
                dosage = random.randint(1, 3) * 10  # e.g., 10mg, 20mg, 30mg
                admin_schedule = random.choice(["Morning", "Evening", "Twice a Day"])

                patient_medication_writer = writers["PatientMedication.csv"]
                patient_medication_writer.writerow({
                    'patient_id': patient_id,
                    'med_id': medication,
                    'dosage': dosage,
                    'admin_schedule': admin_schedule,
                    'prescribing_doc_id': prescribing_doc
                })

                # Track assigned medication
                assigned_medications.add(medication)

finally:
    # Ensure all file handles are closed
    for handle in file_handles.values():
        handle.close()

print("Data generation complete. CSV files are ready.")