import psycopg2
from faker import Faker
import random

fake = Faker()

# Database connection setup
connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="1234",
    database="fastapi_project"
)

cursor = connection.cursor()

def generate_contact():
    return '07'+''.join(random.choices('0123456789', k=8))  


# def get_random_null_value():
#     return random.choice([None, fake.word()])  


# def insert_patient():
#     name = fake.name()
#     age = random.randint(18, 90)  
#     gender = random.choice(["Male", "Female"])
    
#     # contact = get_random_null_value()
#     contact = generate_contact() if random.random() > 0.3 else None

#     cursor.execute(
#         "INSERT INTO patients (name, age, gender, contact) VALUES (%s, %s, %s, %s) RETURNING id",
#         (name, age, gender, contact)
#     )
#     patient_id = cursor.fetchone()[0] 
#     connection.commit()
    
#     return patient_id



# def insert_doctor():
    name = fake.name()
    
    
    speciality = random.choice([
        'General Practitioner', 'Family Medicine Physician', 'Internal Medicine Physician', 
        'Pediatrician', 'Cardiologist', 'Endocrinologist', 'Gastroenterologist', 'Hematologist', 
        'Infectious Disease Specialist', 'Nephrologist', 'Oncologist', 'Pulmonologist', 'Rheumatologist', 
        'Allergist', 'Immunologist', 'Geneticist', 'General Surgeon', 'Cardiothoracic Surgeon', 'Neurosurgeon', 
        'Orthopedic Surgeon', 'Plastic Surgeon', 'Ophthalmic Surgeon', 'Otolaryngologist', 'Vascular Surgeon', 
        'Transplant Surgeon', 'Pediatric Surgeon', 'Trauma Surgeon', 'Radiologist', 'Pathologist', 
        'Nuclear Medicine Specialist', 'Emergency Medicine Physician', 'Intensivist', 'Anesthesiologist', 
        'Obstetrician', 'Gynecologist', 'Neurologist', 'Psychiatrist', 'Child and Adolescent Psychiatrist', 
        'Dermatologist', 'Ophthalmologist', 'Optometrist', 'Otolaryngologist', 'Dentist', 'Orthodontist', 
        'Oral Surgeon', 'Periodontist', 'Endodontist', 'Physiatrist', 'Sports Medicine Specialist', 
        'Palliative Medicine Specialist', 'Geriatrician', 'Occupational Medicine Specialist', 
        'Aerospace Medicine Specialist', 'Forensic Pathologist', 'Sleep Medicine Specialist', 
        'Pain Management Specialist', 'Addiction Medicine Specialist', 'Clinical Geneticist', 
        'Public Health Physician', 'Hyperbaric Medicine Specialist', 'Tropical Medicine Specialist', 
        'Urologist', 'Sexologist', 'Chiropractor', 'Acupuncturist', 'Naturopathic Doctor'
    ])
    speciality = speciality if random.random() > 0.2 else None 
    contact = generate_contact() 

    cursor.execute(
        "INSERT INTO doctors (name, speciality, contact) VALUES (%s, %s, %s) RETURNING id",
        (name, speciality, contact)
    )
    doctor_id = cursor.fetchone()[0]  
    connection.commit()

    return doctor_id


def generate_appointment(patient_id, doctor_id):
    appointment_date = fake.date_this_year()  
    
  
    reason_for_visit = random.choice([
        'Check-up', 'Consultation', 'Follow-up', 'Emergency', 'Routine Examination', 
        'Surgery Consultation', 'Specialist Referral', 'Vaccination', 'Chronic Condition Management', 
        'Infection', 'Injury', 'Diagnostic Test', 'Pregnancy Check', 'Health Screening',
        'Mental Health Consultation', 'Pain Management', 'Allergy Testing', 'Medical Records Review',
        'Weight Management', 'Asthma Management', 'Blood Pressure Check', 'Diabetes Management', 
        'Cold or Flu Symptoms', 'Skin Condition', 'Digestive Issues', 'Sleep Disorders', 
        'Eye Examination', 'Hearing Test', 'Immunization', 'Post-Operative Care', 'Blood Work Review',
        'Wound Care', 'Chronic Pain', 'Cardiovascular Checkup', 'Bone and Joint Health', 
        'Cancer Screening', 'Neurological Symptoms', 'Thyroid Issues', 'Urinary Tract Infection', 
        'Fertility Consultation', 'Hormonal Imbalance', 'Postpartum Checkup', 'Travel Medicine',
        'Depression', 'Anxiety', 'Mental Health Medication Review', 'Addiction Counseling', 
        'Stress Management', 'Eating Disorders', 'Weight Loss Surgery Consultation', 'Physical Therapy',
        'Speech Therapy', 'Occupational Therapy', 'Genetic Testing', 'Post-Surgical Rehab', 'Lung Disease',
        'Environmental Allergies', 'HIV/STI Testing', 'Infertility Treatment', 'Elderly Care', 'Pediatric Care',
        'Preventive Care', 'Physical Examination for Employment', 'Pre-Surgery Screening', 'Arthritis',
        'Rheumatology Consultation', 'Sleep Apnea', 'Detoxification', 'Maternity Care', 'Prostate Health',
        'Menopause', 'Chronic Fatigue Syndrome', 'Vertigo or Dizziness', 'Memory Issues', 'Sexual Health',
        'Infectious Disease Management', 'Autoimmune Disease', 'Immunodeficiency Treatment', 'Liver Disease',
        'Kidney Disease', 'Multiple Sclerosis', 'Parkinson’s Disease', 'Epilepsy', 'Cystic Fibrosis'
    ]) if random.random() > 0.15 else None 
    
    cursor.execute(
        """
        INSERT INTO appointments (patient_id, doctor_id, reason, date)
        VALUES (%s, %s, %s, %s)
        """, 
        (patient_id, doctor_id, reason_for_visit, appointment_date)
    )
    connection.commit()


def populate_data(num_patients=500000, num_doctors=500000, num_appointments=500000):


    # print("Inserting patients...")
    # for _ in range(num_patients):
    #     patient_id = insert_patient()


    # print("Inserting doctors...")
    # for _ in range(num_doctors):
    #     doctor_id = insert_doctor()
    

    print("Inserting appointments...")
    for _ in range(num_appointments):

        cursor.execute("SELECT id FROM patients ORDER BY RANDOM() LIMIT 1")
        patient_id = cursor.fetchone()[0]
        

        cursor.execute("SELECT id FROM doctors ORDER BY RANDOM() LIMIT 1")
        doctor_id = cursor.fetchone()[0]
        

        generate_appointment(patient_id, doctor_id)


populate_data()


cursor.close()
connection.close()
