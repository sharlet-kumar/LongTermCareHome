import random
from faker import Faker
import csv

# Initialize Faker for generating realistic names and data
fake = Faker()

# Define counts for primary entities
num_patients = 4000
num_medications = 1000
num_visitors = 800
num_staff = 2500
num_food_items = 200

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
address_ids=[]
policy_ids=[]


patient_conditions = {}  
medication_condition_map = {} 
med_med_conflicts = set()
medication_allergy_map = {}  
food_allergy_conflicts = set()
food_allergy_map = {} 
staff_patient_pairs = set()
med_side_effects_map = {}
assigned_conditions = {}  
assigned_symptoms = {}  
patient_allergy_map = {}  
med_allergy_conflicts = set()

# unique data generation
def generate_unique_patient_id():
    while True:
        patient_id = ''.join(random.choices('0123456789', k=10))
        if patient_id not in patient_ids:
            patient_ids.append(patient_id)
            return patient_id
        
def generate_unique_policy_id():
    while True:
        policy_id = ''.join(random.choices('0123456789', k=10))
        if policy_id not in policy_ids:
            policy_ids.append(policy_id)
            return policy_id
        
def generate_unique_address_id():
    while True:
        address_id = ''.join(random.choices('0123456789', k=10))
        if address_id not in address_ids:
            address_ids.append(address_id)
            return address_id

def generate_unique_med_id():
    while True:
        med_id = ''.join(random.choices('0123456789', k=8))
        if med_id not in med_ids:
            med_ids.append(med_id)
            return med_id

def generate_unique_staff_id():
    while True:
        staff_id = ''.join(random.choices('0123456789', k=10))
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
        phone_number = ''.join(random.choices('0123456789', k=15))
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
    "Patients.csv": ['patientID', 'firstName', 'lastName', 'DateOfBirth', 'Sex', 'Height', 'Weight', 'AddressID', 'DNR', 'InsuranceCheck'],
    "PatientAddress.csv": ['AddressID', 'StreetNo', 'StreetName', 'UnitNo', 'City', 'State', 'Country'],
    "Medications.csv": ['medID', 'medName', 'drugClass', 'adminDetails', 'storagedetails'],
    "PatientPhone.csv": ['patientID', 'phone'],
    "Staff.csv": ['staffID', 'firstName', 'lastName', 'position', 'department'],
    "StaffPhone.csv": ['staffID', 'phone'],
    "PatientMedicalConditions.csv": ['patientID', 'medicalCondition', 'description', 'diagnosisDate', 'diagnoserID'],
    "PatientStaffCare.csv": ['staffID', 'patientID', 'staffRoleInCare', 'careStartDate', 'careEndDate'],
    "Insurance.csv": ['PolicyID', 'provider', 'patientID', 'BillingAddressID'],
    "InsuranceCoverageDetails.csv": ['PolicyID', 'coverageDetails'],
    "BillingAddress.csv": ['BillingAddressID', 'streetNo', 'streetName', 'unitNo', 'city', 'state', 'country'],
    "MedsTreatCondition.csv": ['medId', 'conditionName'],
    "MedSideEffects.csv": ['medID', 'sideEffects', 'Severity'],
    "Allergy.csv": ['allergyName', 'managementStrategy', 'seasonalconsiderations'],
    "AllergySymptom.csv": ['allergyName', 'symptoms', 'severity'],
    "AllergyTreatment.csv": ['allergyName', 'treatment', 'considerations'],
    "PatientAllergies.csv": ['allergyName', 'patientID', 'severity', 'description'],
    "visitor.csv": ['visitorID', 'firstName', 'lastName'],
    "Visits.csv": ['visitID', 'visitorID', 'patientID', 'VisitDate', 'notes'],
    "VisitorPhone.csv": ['visitorID', 'phone'],
    "FoodAndNutrition.csv": ['foodname', 'foodgroup', 'calories', 'protein', 'fats'],
    "MedAllergyConflict.csv": ['allergyName','medID', 'ConflictCheck'],
    "MedMedConflict.csv": ['medicationAID', 'medicationBID', 'ConflictCheck', 'severity'],
    "MealPlans.csv": ['MealPlanID', 'schedule', 'PatientID'],
    "Meal.csv": ['MealPlanID', 'mealName', 'foodName1', 'foodName2'],
    "FoodAllergyConflict.csv": ['foodname', 'allergyName', 'ConflictCheck'],
    "PatientMedication.csv": ['PatientID', 'medID', 'dosage', 'AdminSchedule', 'prescribingDocID'],
    

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
        patient_id = generate_unique_patient_id()
        address_id = generate_unique_address_id()  # Unique AddressID for each patient

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
            "patientID": patient_id,  
            "firstName": first_name,  
            "lastName": last_name,    
            "DateOfBirth": dob,       
            "Sex": sex,               
            "Height": height,         
            "Weight": weight,         
            "AddressID": address_id,  
            "DNR": dnr_present,       
            "InsuranceCheck": insurance_check  
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
            "AddressID": address_id,
            "StreetNo": street_no,
            "StreetName": street_name,
            "UnitNo": unit_no,
            "City": city,
            "State": state,
            "Country": country
        })

        # Generate data for PatientPhones table
        for _ in range(random.randint(*num_phones_per_patient)):  # Each patient can have 1-3 phone numbers
            phone_number = generate_unique_phone()

            patient_phone_writer=writers["PatientPhone.csv"]
            patient_phone_writer.writerow({'patientID': patient_id, 
                                           'phone': phone_number})

    print("Patient, Phone and Address tables filled")
        
            
# Generate Staff and only keep Doctor IDs for diagnoserID in PatientMedicalConditions
    for _ in range(num_staff):
        staff_id = generate_unique_staff_id()
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        position = random.choice(["Nurse", "Doctor", "Administrator", "Technician"])
        department = random.choice(["Emergency", "Pediatrics", "Oncology", "Cardiology", "Radiology"])

        staff_writer=writers["Staff.csv"]
        staff_writer.writerow({'staffID': staff_id,
                               'firstName': first_name,
                               'lastName': last_name,
                               'position': position,
                               'department': department
})

        # Add to doctor_ids list if the position is "Doctor"
        if position == "Doctor":
            doctor_ids.append(staff_id)

        # StaffPhone
        phone_number = generate_unique_phone()

        staff_phone_writer=writers["StaffPhone.csv"]
        staff_phone_writer.writerow({'staffID': staff_id,
                                     'phone': phone_number
})

    print("Staff and Staffphone tables filled")

    # Generate Patient Medical Conditions, using only doctor IDs as diagnoserID
    for _ in range(num_patients // 2):
        patient_id = random.choice(patient_ids)
        diagnoser_id = random.choice(doctor_ids)
        condition = random.choice(health_conditions)
        description = fake.sentence().replace("'", "''")
        diagnosis_date = fake.date_this_decade()

        # Ensure the patient doesn't already have this condition
        if patient_id not in assigned_conditions:
            assigned_conditions[patient_id] = set()
        
        while condition in assigned_conditions[patient_id]:
            condition = random.choice(health_conditions)  # Pick a new condition until it's unique for the patient

        # Add the condition to the patient's set of assigned conditions
        assigned_conditions[patient_id].add(condition)

        # Write to the CSV file
        patient_medical_conditions_writer = writers["PatientMedicalConditions.csv"]
        patient_medical_conditions_writer.writerow({
            "patientID": patient_id,
            "medicalCondition": condition,
            "description": description,
            "diagnosisDate": diagnosis_date,
            "diagnoserID": diagnoser_id
        })

    print("PatientMedicalConditions table filled")

# Generate PatientStaffCare data
    for _ in range(num_patients * 2):  # Assign each patient to at least one staff member
        while True:
            staff_id = random.choice(staff_ids)
            patient_id = random.choice(patient_ids)
            pair = (staff_id, patient_id)

            # Ensure the pair is unique
            if pair not in staff_patient_pairs:
                staff_patient_pairs.add(pair)
                break  # Exit loop once unique pair is found

        staff_role = random.choice(["Primary Care", "Specialist", "Technician", "Nurse"])
        care_start_date = fake.date_this_year()
        care_end_date = fake.date_this_year()

        # Ensure care_end_date is after care_start_date
        if care_end_date < care_start_date:
            care_start_date, care_end_date = care_end_date, care_start_date

        # Write to the CSV file
        patient_staff_care_writer=writers["PatientStaffCare.csv"]
        patient_staff_care_writer.writerow({
            'staffID': staff_id,
            'patientID': patient_id,
            'staffRoleInCare': staff_role,
            'careStartDate': care_start_date,
            'careEndDate': care_end_date
        })

    print("Staff care tables filled")



# Generate Insurance for patients with insurance
    for patient_id in patients_with_insurance:
        # Generate unique IDs for policy and billing address
        policy_id = generate_unique_policy_id()

        billing_address_id = generate_unique_address_id()

        # Generate insurance provider and other details
        provider = random.choice(insurance_providers)

        # Write Insurance record
        insurance_writer = writers["Insurance.csv"]
        insurance_writer.writerow({'PolicyID': policy_id,
                                   'provider': provider,
                                   'patientID': patient_id,
                                   'BillingAddressID': billing_address_id
                                   
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
        billing_address_writer.writerow({'BillingAddressID': billing_address_id,
                                         'streetNo': street_no,
                                         'streetName': street_name,
                                         'unitNo': unit_no,
                                         'city': city,
                                         'state': state,
                                         'country': country
        })

        # Generate coverage details for InsuranceCoverageDetails table
        coverage_details = fake.sentence().replace("'", "''")
        insurance_coverage_details_writer = writers["InsuranceCoverageDetails.csv"]
        insurance_coverage_details_writer.writerow({ 'PolicyID': policy_id,
                                                    'coverageDetails': coverage_details
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
        medication_writer.writerow({'medID': med_id,
                                    'medName': med_name,
                                    'drugClass': drug_class,
                                    'adminDetails': administration_details,
                                    'storagedetails': storage_details
        })

        # Write the single treated condition to MedsTreatCondition.csv
        treat_conditions_writer = writers["MedsTreatCondition.csv"]
        treat_conditions_writer.writerow({'medId': med_id,
                                          'conditionName': treated_condition
})

    print("Meds and treatment tables filled")

# Ensure all med_ids have an entry in the map
    for med_id in med_ids:
        med_side_effects_map[med_id] = set()

    # Generate side effects for medications
    for med_id in med_ids:
        for _ in range(random.randint(1, 3)):  # Each medication can have 1-3 side effects
            while True:
                side_effect = random.choice(side_effects_list)
                # Ensure the side effect is not already assigned to this medication
                if side_effect not in med_side_effects_map[med_id]:
                    med_side_effects_map[med_id].add(side_effect)  # Add to the set
                    break  # Exit the loop once a unique side effect is found

            severity = random.choice(["Mild", "Moderate", "Severe"])

            # Write to the CSV file
            med_side_effects_writer = writers["MedSideEffects.csv"]
            med_side_effects_writer.writerow({
                'medID': med_id,
                'sideEffects': side_effect,
                'Severity': severity
            })

    print("Meds Side Effects table filled")

# Generate Allergies
    for allergy_name in allergy_names:
        # Generate Allergy information
        management_strategy = fake.sentence().replace("'", "''")
        seasonal_considerations = random.choice([True, False])

        allergy_write = writers["Allergy.csv"]
        allergy_write.writerow({ 'allergyName': allergy_name,
            'managementStrategy': management_strategy,
            'seasonalconsiderations': seasonal_considerations
        })

    print("Allergy table filled.")

    # Generate Symptoms for each Allergy
    for allergy_name in allergy_names:
        assigned_symptoms[allergy_name] = set()  # Initialize set for this allergy

        for _ in range(random.randint(1, 3)):  # Each allergy can have 1-3 symptoms
            symptom = random.choice(["Sneezing", "Itchy eyes", "Swelling", "Hives", "Shortness of breath"])
            severity = random.choice(["Low", "Moderate", "Severe"])

            # Ensure symptom is unique for the allergy
            while symptom in assigned_symptoms[allergy_name]:
                symptom = random.choice(["Sneezing", "Itchy eyes", "Swelling", "Hives", "Shortness of breath"])

            assigned_symptoms[allergy_name].add(symptom)

            # Write AllergySymptoms data
            allergy_symptom_write = writers["AllergySymptom.csv"]
            allergy_symptom_write.writerow({
                'allergyName': allergy_name,
                'symptoms': symptom,
                'severity': severity
            })

    print("AllergySymptom table filled.")

    # Generate Treatments for each Allergy
    for allergy_name in allergy_names:
        treatment = fake.sentence().replace("'", "''")
        considerations = fake.sentence().replace("'", "''")

        # Write AllergyTreatment data
        allergy_treatment_write = writers["AllergyTreatment.csv"]
        allergy_treatment_write.writerow({
            'allergyName': allergy_name,
            'treatment': treatment,
            'considerations': considerations
        })

    print("AllergyTreatment table filled.")

# Generate Patient Allergies
    for patient_id in patient_ids[:len(patient_ids) // 2]:  # Assign allergies to roughly half the patients
        if patient_id not in patient_allergy_map:
            patient_allergy_map[patient_id] = set()  # Initialize the set for each patient

        # Assign 1 to 3 unique allergies to the patient
        while len(patient_allergy_map[patient_id]) < random.randint(1, 3):
            allergy_name = random.choice(allergy_names)
            
            # Ensure no duplicate patient-allergy pair
            if allergy_name not in patient_allergy_map[patient_id]:
                patient_allergy_map[patient_id].add(allergy_name)  # Add allergy to the set
                
                # Generate attributes
                severity = random.choice(["Mild", "Moderate", "Severe"])
                description = fake.sentence().replace("'", "''")

                # Write to CSV
                patient_allergies_write = writers["PatientAllergies.csv"]
                patient_allergies_write.writerow({
                    'allergyName': allergy_name,
                    'patientID': patient_id,
                    'severity': severity,
                    'description': description
                })
    print("PatientAllergies table filled.")


# Generate Visitor
    for _ in range(num_visitors):
        visitor_id = generate_unique_visitor_id()
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")

        visitor_write=writers["visitor.csv"]
        visitor_write.writerow({'visitorID':visitor_id, 
                                'firstName':first_name, 
                                'lastName':last_name})
    print("visitor tables filled")
# Generate Visits
    for _ in range(num_visitors):
        visit_id = fake.unique.random_int(min=1000, max=9999)
        visitor_id = random.choice(visitor_ids)
        patient_id = random.choice(patient_ids)
        date = fake.date_this_year()
        notes = fake.sentence().replace("'", "''")

        visits_write=writers["Visits.csv"]
        visits_write.writerow({'visitID':visit_id, 
                               'visitorID':visitor_id, 
                               'patientID':patient_id, 
                               'VisitDate':date, 
                               'notes':notes})
    print("visits tables filled")

# Generate VisitorPhone
    for visitor_id in visitor_ids:
        phone_number = generate_unique_phone()

        visitor_phone_writer=writers["VisitorPhone.csv"]
        visitor_phone_writer.writerow({'visitorID':visitor_id,
                                        'phone':phone_number})
    print("visitor phone tables filled")

 # Generate Foods and Nutritional Values
    for _ in range(num_food_items):
        food_name = generate_unique_food_name()
        food_type = random.choice(food_types)
        calories = random.randint(50, 300)
        protein = random.randint(0, 20)
        fats = random.randint(0, 20)

        food_nutrition_writer=writers["FoodAndNutrition.csv"]
        food_nutrition_writer.writerow({'foodname':food_name, 
                                        'foodgroup':type, 
                                        'calories':calories,
                                        'protein':protein, 
                                        'fats':fats})
    print("food tables filled")

#Generate Med-Allergy Conflicts
    for med_id in med_ids:
        for _ in range(random.randint(1, 3)):  # Each medication can have 1-3 allergy conflicts
            allergy_name = random.choice(allergy_names)
            conflict_check = random.choice([True, False])

            # Ensure uniqueness of the combination
            while (allergy_name, med_id) in med_allergy_conflicts:
                allergy_name = random.choice(allergy_names)  # Pick a new allergy if duplicate found

            # Add the unique combination to the set
            med_allergy_conflicts.add((allergy_name, med_id))

            # Write to CSV
            med_allergy_conflict_writer = writers["MedAllergyConflict.csv"]
            med_allergy_conflict_writer.writerow({
                'allergyName': allergy_name,
                'medID': med_id,
                'ConflictCheck': conflict_check
            })

    print("MedAllergyConflict table filled")

# Medication Conflicts
    med_ids_list = list(medication_condition_map.keys())
    for _ in range(len(med_ids_list) // 3):  # About 1/3 of meds have conflicts
        med_a = random.choice(med_ids_list)
        med_b = random.choice(med_ids_list)

        # Ensure med_a is not equal to med_b and the pair is unique
        while med_b == med_a or (med_a, med_b) in med_med_conflicts or (med_b, med_a) in med_med_conflicts:
            med_b = random.choice(med_ids_list)

        # Add the pair to the set
        med_med_conflicts.add((med_a, med_b))

        # Generate conflict details
        conflict_check = True  # Boolean indicating conflict exist

        # Write to CSV
        med_med_conflict_writer = writers["MedMedConflict.csv"]
        med_med_conflict_writer.writerow({
            'medicationAID': med_a,
            'medicationBID': med_b,
            'ConflictCheck': conflict_check,
            'severity': random.choice(["Low", "Medium", "High"])
        })

    print("medmedconflict tables filled")


# Generate FoodAllergyConflict
    for _ in range(num_food_items * 2):  # Randomly create conflicts for some food items
        food_name = random.choice(food_names)
        allergy_name = random.choice(allergy_names)
        
        # Ensure the (food_name, allergy_name) pair is unique
        while (food_name, allergy_name) in food_allergy_conflicts:
            food_name = random.choice(food_names)
            allergy_name = random.choice(allergy_names)

        # Add the unique pair to the set
        food_allergy_conflicts.add((food_name, allergy_name))

        # Write the conflict to the CSV file
        conflict_check = True  # Boolean indicating conflict exist
        food_allergy_conflict_writer = writers["FoodAllergyConflict.csv"]
        food_allergy_conflict_writer.writerow({
            'foodname': food_name,
            'allergyName': allergy_name,
            'ConflictCheck': conflict_check
        })

    print("FoodAllergyConflict table filled")

# Generate Meal Plans for every patient
    for patient_id in patient_ids:  # Ensure every patient gets a meal plan
        meal_plan_id = generate_unique_meal_plan_id()
        schedule = random.choice(["Breakfast", "Lunch", "Dinner"])

        # Add to MealPlans.csv
        meal_plans_writer = writers["MealPlans.csv"]
        meal_plans_writer.writerow({
            'MealPlanID': meal_plan_id,
            'schedule': schedule,
            'PatientID': patient_id
        })

        # Store in meal_plans_data for later meal generation
        meal_plans_data.append({
            'MealPlanID': meal_plan_id,
            'PatientID': patient_id
        })
    print("mealplan tables filled")

# Generate Meals for each meal plan
    for meal_plan in meal_plans_data:  # Iterate over the list of meal plan dictionaries
        meal_plan_id = meal_plan['MealPlanID']
        patient_id = meal_plan['PatientID']

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
                'MealPlanID': meal_plan_id,
                'mealName': fake.word().capitalize(),
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
                    'PatientID': patient_id,
                    'medID': medication,
                    'dosage': dosage,
                    'AdminSchedule': admin_schedule,
                    'prescribingDocID': prescribing_doc
                })

                # Track assigned medication
                assigned_medications.add(medication)
    print("Patient medication tables filled")

finally:
    # Ensure all file handles are closed
    for handle in file_handles.values():
        handle.close()

print("Data generation complete. CSV files are ready.")