import requests
import pandas as pd


patients_data = requests.get("http://127.0.0.1:8000/patients/")
doctors_data = requests.get("http://127.0.0.1:8000/doctors/")
appointments_data = requests.get("http://127.0.0.1:8000/appointments/")

#these are dataframes put to json for easy reading
patients = pd.DataFrame(patients_data.json())
doctors = pd.DataFrame(doctors_data.json())
appointments = pd.DataFrame(appointments_data.json())


print('------------------------------- Before preprocessing -------------------------------')
# print(patients.describe())
# print(doctors.describe())
print(appointments.describe())
print(appointments.shape)
print(appointments.isnull().sum())


print('------------------------------- After preprocessing -------------------------------')

#finding and replacing null values using forward and backward fill
appointments_null = appointments.ffill(inplace=True)
appointments_null = appointments.bfill(inplace=True)

print(appointments.isnull().sum())


# converting datatypes a.k.a cleaning data
appointments['date'] = pd.to_datetime(appointments['date'])

# removing dups
appointments.drop_duplicates(inplace = True)
print(appointments)

appointments = pd.get_dummies(appointments, columns=['reason'])
print(appointments)

# #my feature creation
appointments['week_day'] = appointments['date'].dt.dayofweek
appointments['month'] = appointments['date'].dt.month
appointments['year']  = appointments['date'].dt.year

print(appointments)
