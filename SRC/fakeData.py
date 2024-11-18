import random
from faker import Faker

# Initialize the Faker library
fake = Faker()

# Define the number of rows to generate
num_patients = 2000  # 2,000 tuples
num_phones_per_patient = (1, 3)  # Multi value (1 to 3)
num_emails_per_patient = (1, 2)  # multi value (1 to 2)
num_conditions_per_patient = (0, 5)  # Multi value (0 to 5)

# Store unique 12-digit IDs, phone numbers, and emails to avoid duplicates
patient_ids = set()
all_phone_numbers = set()
all_emails = set()

def generate_unique_id():
    """Generate a unique 12-digit patient ID."""
    while True:
        patient_id = ''.join(random.choices('0123456789', k=12))
        if patient_id not in patient_ids:
            patient_ids.add(patient_id)
            return patient_id

def generate_unique_phone():
    """Generate a unique phone number."""
    while True:
        phone_number = fake.phone_number().replace("'", "''")
        if phone_number not in all_phone_numbers:
            all_phone_numbers.add(phone_number)
            return phone_number

def generate_unique_email():
    """Generate a unique email."""
    while True:
        email = fake.email().replace("'", "''")
        if email not in all_emails:
            all_emails.add(email)
            return email

# Open the output file
with open('insert_patient_data.sql', 'w') as file:
    # Write header comments for clarity
    file.write("-- Patients Table\n")
    file.write("-- Insert statements for Patients table\n\n")
    
    # Generate and write data for the Patients table
    for _ in range(num_patients):
        # Generate unique ID for the patient
        patient_id = generate_unique_id()
        
        # Composite attributes
        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")
        
        # Simple attributes
        dob = fake.date_of_birth(minimum_age=0, maximum_age=100)
        age = fake.random_int(min=0, max=100)  # Derived, but including for simplicity
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
        INSERT INTO Patients (patient_id, first_name, last_name, dob, age, height, weight, insurance, sex, dnr_present, street_no, street_name, unit_no, city, province, country)
        VALUES ('{patient_id}', '{first_name}', '{last_name}', '{dob}', {age}, {height}, {weight}, '{insurance}', '{sex}', '{dnr_present}', '{street_no}', '{street_name}', {unit_no}, '{city}', '{province}', '{country}');
        """
        file.write(patient_sql + '\n')

    # Write data for PatientPhones table (few thousand tuples)
    file.write("\n-- PatientPhones Table\n")
    file.write("-- Insert statements for PatientPhones table\n\n")
    
    for patient_id in patient_ids:
        for _ in range(random.randint(*num_phones_per_patient)):  # Each patient can have 1-3 phone numbers
            phone_number = generate_unique_phone()
            phone_sql = f"INSERT INTO PatientPhones (patient_id, phone_number) VALUES ('{patient_id}', '{phone_number}');"
            file.write(phone_sql + '\n')

    # Write data for PatientEmails table (few thousand tuples)
    file.write("\n-- PatientEmails Table\n")
    file.write("-- Insert statements for PatientEmails table\n\n")
    
    for patient_id in patient_ids:
        for _ in range(random.randint(*num_emails_per_patient)):  # Each patient can have 1-2 emails
            email = generate_unique_email()
            email_sql = f"INSERT INTO PatientEmails (patient_id, email) VALUES ('{patient_id}', '{email}');"
            file.write(email_sql + '\n')

    # Write data for PatientConditions table (hundreds of tuples)
    file.write("\n-- PatientConditions Table\n")
    file.write("-- Insert statements for PatientConditions table\n\n")
    
    medical_conditions = [
        'Hypertension', 'Diabetes', 'Asthma', 'Heart Disease', 'Alzheimers', 'Dementia', 'Depression', 
        'Heart Failure', 'Arthritis', 'Obesity', 'High Cholesterol', 'Cancer', 'Hearing loss', 
        'Cataracts', "Stroke", 'Delirium', "Osteoporosis", 'Gout', 'Allergies', 'Anemia', 'Epilepsy', 'Migraine'
    ]

    for patient_id in patient_ids:
        num_conditions = random.randint(*num_conditions_per_patient)  # random number of unique conditions up to the specified limit
        selected_conditions = set()

        for _ in range(num_conditions):
            condition = random.choice(medical_conditions)
            
            # Ensure condition is unique for each patient
            while condition in selected_conditions:
                condition = random.choice(medical_conditions)
            
            # Add the condition to the set
            selected_conditions.add(condition)
            
            # Write SQL for each unique condition
            condition_sql = f"INSERT INTO PatientConditions (patient_id, condition) VALUES ('{patient_id}', '{condition}');"
            file.write(condition_sql + '\n')

print(f"Data for {num_patients} patients generated and saved to 'insert_patient_data.sql'.")
