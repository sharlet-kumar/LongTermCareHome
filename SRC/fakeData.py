import random
from faker import Faker
import csv

# Initialize Faker for generating realistic names and data
fake = Faker()

# Define counts for primary entities
num_patients = 4000
num_medications = 1000
num_meal_plans = 200
num_visitors = 800
num_staff = 2500
num_food_items = 100

# Multi-value counts
num_phones_per_patient = (1, 3)
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
meal_names = ["Breakfast", "Lunch", "Dinner", "Snack"] 


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
meal_plans_data = [] 
policy_ids = []
billing_address_ids = []


patient_conditions = {}  # {patient_id: [condition1, condition2, ...]}
medication_condition_map = {}  # {med_id: [condition1, condition2, ...]}
med_med_conflicts = []  # [(med_a, med_b)]
patient_allergy_map = {}  # {patient_id: [allergy1, allergy2, ...]}
medication_allergy_map = {}  # {med_id: [allergy1, allergy2, ...]}
food_allergy_conflicts = []
food_allergy_map = {} 

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
        
def generate_csv_writer(file_name, fieldnames):
    file = open(file_name, 'w', newline='')
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    return writer, file

# Open CSV files
csv_files = {
    "Patients.csv": ['patient_id', 'first_name', 'last_name', 'dob', 'sex', 'height', 'weight', 'insurance_check', 'dnr', 'address_id'],
    "Medications.csv": ['med_id', 'med_name', 'drug_class', "administration_details", 'storage_details'],
    "PatientPhone.csv": ['patient_id', 'phone_number'],
    "Staff.csv": ['staff_id', 'first_name', 'last_name', 'position', 'department'],
    "StaffPhone.csv": ['staff_id', 'phone_number'],
    "PatientMedicalConditions.csv": ['patient_id', 'medical_condition', 'description', 'diagnosis_date', 'diagnoser_id'],
    "PatientStaffCare.csv": ['staff_id', 'patient_id', 'staff_role_in_care', 'care_start_date', 'care_end_date'],
    "Insurance.csv": ['policy_id', 'provider', 'billing_address_id', 'patient_id'],  
    "InsuranceCoverageDetails.csv": ['policy_id', 'coverage_details'],  
    "BillingAddress.csv": ['billing_address_id', 'street_no', 'street_name', 'unit_no', 'city', 'state', 'country'],
    "MedsTreatCondition.csv": ['med_id', 'condition_name'],
    "MedSideEffects.csv": ['med_id', 'side_effect', 'severity'],
    "Allergy.csv": ['allergy_name', 'type', 'management_strategy', 'seasonal_considerations'],
    "AllergySymptom.csv": ['allergy_name', 'symptom', 'severity'],
    "AllergyTreatment.csv": ['allergy_name', 'treatment', 'considerations'],
    "PatientAllergies.csv": ['allergy_name', 'patient_id', 'severity', 'description'],
    "visitor.csv": ['visitor_id', 'first_name', 'last_name'],
    "Visits.csv": ['visit_id', 'visitor_id', 'patient_id', 'date', 'notes'],
    "VisitorPhone.csv": ['visitor_id', 'phone_number'],
    "FoodAndNutrition.csv": ['food_name', 'type', 'calories', 'protein', 'fats'],
    "MedAllergyConflict.csv": ['med_id', 'allergy_name', 'severity', 'conflict_check'],
    "MedMedConflict.csv": ['med_A', 'med_B', 'severity', 'conflict_check'],
    "MealPlans.csv": ['meal_plan_id', 'schedule', 'patient_id'],
    "Meal.csv": ['meal_plan_id', 'meal_name', 'foodName1', 'foodName2',],
    "FoodAllergyConflict.csv": ['food_name', 'allergy_name', 'conflict_check'],
    "PatientMedication.csv": ['patient_id', 'med_id', 'dosage', 'admin_schedule', 'prescribing_doc_id'],
    "PatientAddress.csv": ['address_id', 'street_no', 'street_name', 'unit_no', 'city', 'state', 'country'],
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

    
# Generate Patients and their Addresses
    for _ in range(num_patients):
        # Generate unique ID for the patient
        patient_id = generate_unique_id()
        address_id = generate_unique_id()  # Unique AddressID for each patient

        # Patient attributes
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        dob = fake.date_of_birth(minimum_age=50, maximum_age=100)
        height = fake.random_int(min=120, max=220)  # in cm
        weight = fake.random_int(min=40, max=150)  # in kg
        insurance_check = True if random.random() < 0.8 else False 
        sex = random.choice(['M', 'F'])
        dnr_present = False if random.random() < 0.8 else True  

        if insurance_check == True:
            patients_with_insurance.append(patient_id)

        # Write Patient data
        patient_writer = writers["Patients.csv"]
        patient_writer.writerow({
            "patient_id": patient_id,
            "first_name": first_name,
            "last_name": last_name,
            "dob": dob,
            "sex": sex,
            "height": height,
            "weight": weight,
            "address_id": address_id,
            "dnr": dnr_present,
            "insurance_check": insurance_check
        })

        # Address attributes
        street_no = fake.building_number()
        street_name = fake.street_name().replace("'", "''")
        unit_no = fake.random_int(min=1, max=100)
        city = fake.city().replace("'", "''")
        state = fake.state_abbr()
        country = 'Canada' if random.random() < 0.7 else 'US'  # 70% Canada, 30% US

        # Write PatientAddress data
        patient_address_writer = writers["PatientAddress.csv"]
        patient_address_writer.writerow({
            "address_id": address_id,
            "street_no": street_no,
            "street_name": street_name,
            "unit_no": unit_no,
            "city": city,
            "state": state,
            "country": country
        })

        # Generate data for PatientPhones table
        for _ in range(random.randint(*num_phones_per_patient)):  # Each patient can have 1-3 phone numbers
            phone_number = generate_unique_phone()

            patient_phone_writer=writers["PatientPhone.csv"]
            patient_phone_writer.writerow({'patient_id':patient_id, 'phone_number': phone_number})
    print("Patient, Phone and Address tables filled")
        
            
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
    print("Staff and Staffphone tables filled")

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
    print("PatientMedicalConditions table filled")

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
    print("Staffcare tables filled")

# Generate Insurance for patients with insurance
    for patient_id in patients_with_insurance:
        # Generate unique IDs for policy and billing address
        policy_id = generate_unique_id()

        billing_address_id = generate_unique_id()

        # Generate insurance provider and other details
        provider = random.choice(insurance_providers)

        # Write Insurance record
        insurance_writer = writers["Insurance.csv"]
        insurance_writer.writerow({
            'policy_id': policy_id,
            'provider': provider,
            'billing_address_id': billing_address_id,
            'patient_id': patient_id
        })

        # Generate BillingAddress details
        street_no = fake.building_number()
        street_name = fake.street_name().replace("'", "''")
        unit_no = fake.random_int(min=1, max=100)
        city = fake.city().replace("'", "''")
        state = fake.state_abbr()
        country = 'Canada' if random.random() < 0.7 else 'US'

        # Write BillingAddress record
        billing_address_writer = writers["BillingAddress.csv"]
        billing_address_writer.writerow({
            'billing_address_id': billing_address_id,
            'street_no': street_no,
            'street_name': street_name,
            'unit_no': unit_no,
            'city': city,
            'state': state,
            'country': country
        })

        # Generate coverage details for InsuranceCoverageDetails table
        coverage_details = fake.sentence().replace("'", "''")
        insurance_coverage_details_writer = writers["InsuranceCoverageDetails.csv"]
        insurance_coverage_details_writer.writerow({
            'policy_id': policy_id,
            'coverage_details': coverage_details
        })
    print("Insurance, Billing and Coverage tables filled")
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
    print("Meds and treatment tables filled")

# Generate Medication Side Effects
    for med_id in med_ids:
        for _ in range(random.randint(1, 3)):  # Each medication can have 1-3 side effects
            side_effect = random.choice(side_effects_list)
            severity = random.choice(["Mild", "Moderate", "Severe"])

            med_side_effects_write=writers["MedSideEffects.csv"]
            med_side_effects_write.writerow({'med_id':med_id, 'side_effect':side_effect, 'severity':severity})
    print("Meds Side effects tables filled")

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
    print("Allergy tables filled")

# Generate Visitor
    for _ in range(num_visitors):
        visitor_id = generate_unique_visitor_id()
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")

        visitor_write=writers["visitor.csv"]
        visitor_write.writerow({'visitor_id':visitor_id, 'first_name':first_name, 'last_name':last_name})
    print("visitor tables filled")
# Generate Visits
    for _ in range(num_visitors):
        visit_id = fake.unique.random_int(min=1000, max=9999)
        visitor_id = random.choice(visitor_ids)
        patient_id = random.choice(patient_ids)
        date = fake.date_this_year()
        notes = fake.sentence().replace("'", "''")

        visits_write=writers["Visits.csv"]
        visits_write.writerow({'visit_id':visit_id, 'visitor_id':visitor_id, 'patient_id':patient_id, 'date':date, 'notes':notes})
    print("visits tables filled")

# Generate VisitorPhone
    for visitor_id in visitor_ids:
        phone_number = generate_unique_phone()

        visitor_phone_writer=writers["VisitorPhone.csv"]
        visitor_phone_writer.writerow({'visitor_id':visitor_id, 'phone_number':phone_number})
    print("visitor phone tables filled")

 # Generate Foods and Nutritional Values
    for _ in range(num_food_items):
        food_name = generate_unique_food_name()
        food_type = random.choice(food_types)
        calories = random.randint(50, 300)
        protein = random.randint(0, 20)
        fats = random.randint(0, 20)

        food_nutrition_writer=writers["FoodAndNutrition.csv"]
        food_nutrition_writer.writerow({'food_name':food_name, 'type':type, 'calories':calories, 'protein':protein, 'fats':fats})
    print("food tables filled")

# Generate MedAllergyConflict (conflicts between medications and allergies)
    for _ in range(num_medications // 2):
        med_id = random.choice(med_ids)
        allergy_name = random.choice(allergy_names)
        severity = random.choice(["Low", "Medium", "High"])
        conflict_check = True  # Boolean indicating conflict exists
        
        
        med_allergy_conflict_writer=writers["MedAllergyConflict.csv"]
        med_allergy_conflict_writer.writerow({'med_id':med_id, 'allergy_name':allergy_name, 'severity':severity, 'conflict_check': conflict_check})
    print("medallergyconflict tables filled")


# Medication Conflicts
    med_ids_list = list(medication_condition_map.keys())
    for _ in range(len(med_ids_list) // 3):  # About 1/3 of meds have conflicts
        med_a = random.choice(med_ids_list)
        med_b = random.choice(med_ids_list)
        while med_b == med_a:
            med_b = random.choice(med_ids_list)  # Ensure unique pairs
        med_med_conflicts.append((med_a, med_b))
        conflict_check = True  # Boolean indicating conflict exist

        med_med_conflict_writer = writers["MedMedConflict.csv"]
        med_med_conflict_writer.writerow({'med_A': med_a, 'med_B': med_b, 'severity': random.choice(["Low", "Medium", "High"] ),'conflict_check': conflict_check})
    print("medmedconflict tables filled")


## Generate FoodAllergyConflict
    for _ in range(num_food_items * 2):  # Randomly create conflicts for some food items
        food_name = random.choice(food_names)
        allergy_name = random.choice(allergy_names)
        conflict_check = True  # Boolean indicating conflict exist

        # Write the conflict to the CSV file
        food_allergy_conflict_writer = writers["FoodAllergyConflict.csv"]
        food_allergy_conflict_writer.writerow({
            'food_name': food_name,
            'allergy_name': allergy_name,
            'conflict_check': conflict_check
    })
    print("foodallergy tables filled")

# Generate Meal Plans for every patient
    for patient_id in patient_ids:  # Ensure every patient gets a meal plan
        meal_plan_id = generate_unique_meal_plan_id()
        schedule = random.choice(["Breakfast", "Lunch", "Dinner"])

        # Add to MealPlans.csv
        meal_plans_writer = writers["MealPlans.csv"]
        meal_plans_writer.writerow({
            'meal_plan_id': meal_plan_id,
            'schedule': schedule,
            'patient_id': patient_id
        })

        # Store in meal_plans_data for later meal generation
        meal_plans_data.append({
            'meal_plan_id': meal_plan_id,
            'patient_id': patient_id
        })
    print("mealplan tables filled")

# Generate Meals for each meal plan
    for meal_plan in meal_plans_data:  # Iterate over the list of meal plan dictionaries
        meal_plan_id = meal_plan['meal_plan_id']
        patient_id = meal_plan['patient_id']

        # Get allergies for the patient
        patient_allergies = patient_allergy_map.get(patient_id, [])

        # Pre-generate all valid food pairs
        valid_food_pairs = [
            (food1, food2) for food1 in food_names for food2 in food_names
            if food1 != food2 and
            not any(
                allergy in food_allergy_map.get(food1, []) or allergy in food_allergy_map.get(food2, [])
                for allergy in patient_allergies
            )
        ]

        if not valid_food_pairs:
            print(f"No valid food pairs for PlanID={meal_plan_id}, PatientID={patient_id}.")
            continue

        assigned_foods = set()  # Reset for each meal plan

        for _ in range(random.randint(1, 3)):  # Each plan can have 1-3 meals
            if not valid_food_pairs:
                print(f"Exhausted valid food pairs for PlanID={meal_plan_id}.")
                break

            # Randomly pick a valid food pair
            food1, food2 = random.choice(valid_food_pairs)
            valid_food_pairs.remove((food1, food2))  # Remove the chosen pair to avoid reuse
            assigned_foods.update([food1, food2])

            # Write meal data to Meal.csv
            meal_writer = writers["Meal.csv"]
            meal_writer.writerow({
                'meal_plan_id': meal_plan_id,
                'meal_name': fake.word().capitalize(),
                'foodName1': food1,
                'foodName2': food2,
            })
    print("meal tables filled")
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
    print("Patient medication tables filled")

finally:
    # Ensure all file handles are closed
    for handle in file_handles.values():
        handle.close()

print("Data generation complete. CSV files are ready.")