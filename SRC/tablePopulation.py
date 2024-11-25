import pymysql
import csv
import os

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "EandS2024!",  ###put in your pasword 
    "database": "longtermcare"
}

csv_directory = "C:\\Users\\sharl\\OneDrive\\Desktop\\3309\\assignment-3-group5" ###path to folder where all csv files are held on device 

# Mapping CSV files to tables
csv_to_table_mapping = {
    "Patients.csv": "Patient",
    "PatientAddress.csv": "PatientAddress",
    "PatientPhone.csv": "PatientPhone",
    "Medications.csv": "Medication",
    "Staff.csv": "Staff",
    "StaffPhone.csv": "StaffPhone",
    "PatientMedicalConditions.csv": "PatientCondition",
    "PatientStaffCare.csv": "PatientStaffCare",
    "Insurance.csv": "Insurance",
    "InsuranceCoverageDetails.csv": "InsuranceCoverageDetails",
    "BillingAddress.csv": "BillingAddress",
    "MedsTreatCondition.csv": "MedsTreatCondition",
    "MedSideEffects.csv": "MedicalSideEffects",
    "Allergy.csv": "Allergy",
    "AllergySymptom.csv": "AllergySymptoms",
    "AllergyTreatment.csv": "AllergyTreatment",
    "PatientAllergies.csv": "PatientAllergy",
    "visitor.csv": "Visitor",
    "Visits.csv": "Visit",
    "VisitorPhone.csv": "VisitorPhone",
    "FoodAndNutrition.csv": "food",
    "MedAllergyConflict.csv": "MedAllergyConflict",
    "MedMedConflict.csv": "MedtoMedConflict",
    "MealPlans.csv": "MealPlan",
    "Meal.csv": "Meal",
    "FoodAllergyConflict.csv": "FoodAllergyConflict",
    "PatientMedication.csv": "PatientMedication"
}

# Connect to MySQL
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

try:
    # Disable foreign key checks
    print("Disabling foreign key checks...")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

    # Clear all tables before inserting data
    print("Clearing existing data from tables...")
    for table_name in csv_to_table_mapping.values():
        cursor.execute(f"DELETE FROM {table_name};")
        cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1;")  # Reset auto-increment (if applicable)
    connection.commit()
    print("All tables cleared successfully.")

    # Enable foreign key checks
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    print("Foreign key checks re-enabled.")

    # Process and insert data
    for csv_file, table_name in csv_to_table_mapping.items():
        csv_path = os.path.join(csv_directory, csv_file)
        print(f"Processing {csv_file} for table {table_name}...")

        # Open CSV and read records
        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames

            # Generate INSERT query dynamically based on headers
            placeholders = ", ".join([f"%({header})s" for header in headers])
            query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"

            # Insert each record
            for row in reader:
                # Convert 'True'/'False' to 1/0 for boolean columns if necessary
                for key in row:
                    if row[key] in ['True', 'False']:
                        row[key] = 1 if row[key] == 'True' else 0
                cursor.execute(query, row)

            connection.commit()
            print(f"Inserted records into {table_name}.")

except Exception as e:
    print(f"Error: {e}")
    connection.rollback()

finally:
    cursor.close()
    connection.close()
    print("Database connection closed.")
