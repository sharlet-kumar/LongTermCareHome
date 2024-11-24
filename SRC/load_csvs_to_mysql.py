import pymysql
import os

# Database configuration
db_config = {
    'host': 'localhost',  
    'user': 'root',
    'password': 'EandS2024!',
    'database': 'longtermcare',  
}

# Path to folder containing CSV files
csv_folder = "C:\\Users\\sharl\\OneDrive\\Desktop\\3309\\assignment-3-group5\\Tables"


# Mapping CSV files to their respective tables
csv_to_table_mapping = {
    'Patients.csv': 'Patients',
    'Medications.csv': 'Medications',
    'PatientPhone.csv': 'PatientPhone',
    'PatientEmail.csv': 'PatientEmail',
    'Staff.csv': 'Staff',
    'StaffPhone.csv': 'StaffPhone',
    'PatientMedicalConditions.csv': 'PatientMedicalConditions',
    'PatientStaffCare.csv': 'PatientStaffCare',
    'Insurance.csv': 'Insurance',
    'InsuranceCoverageDetails.csv': 'InsuranceCoverageDetails',
    'MedsTreatCondition.csv': 'MedsTreatCondition',
    'MedSideEffects.csv': 'MedSideEffects',
    'Allergy.csv': 'Allergy',
    'AllergySymptom.csv': 'AllergySymptom',
    'AllergyTreatment.csv': 'AllergyTreatment',
    'PatientAllergies.csv': 'PatientAllergies',
    'visitor.csv': 'Visitor',
    'Visits.csv': 'Visits',
    'VisitorPhone.csv': 'VisitorPhone',
    'FoodAndNutrition.csv': 'FoodAndNutrition',
    'MedAllergyConflict.csv': 'MedAllergyConflict',
    'MedMedConflict.csv': 'MedMedConflict',
    'MealPlans.csv': 'MealPlans',
    'Meal.csv': 'Meal',
    'FoodAllergyConflict.csv': 'FoodAllergyConflict',
    'PatientMedication.csv': 'PatientMedication'
}

# Connect to MySQL
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

try:
    for csv_file, table in csv_to_table_mapping.items():
        csv_path = os.path.join(csv_folder, csv_file)
        if os.path.exists(csv_path):
            print(f"Loading {csv_file} into {table}...")

            # MySQL query to load CSV data
            load_query = f"""
            LOAD DATA LOCAL INFILE '{csv_path}'
            INTO TABLE {table}
            FIELDS TERMINATED BY ',' 
            ENCLOSED BY '"' 
            LINES TERMINATED BY '\\n'
            IGNORE 1 ROWS;
            """

            # Execute the query
            cursor.execute(load_query)
            connection.commit()

            print(f"Successfully loaded {csv_file} into {table}.")
        else:
            print(f"CSV file {csv_file} not found in the folder. Skipping...")
finally:
    # Close the connection
    cursor.close()
    connection.close()

print("All CSV files processed.")
