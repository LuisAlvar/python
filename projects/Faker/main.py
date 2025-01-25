# pip install pandas
# pip install Faker
# pip install openpyxl
import pandas as pd
from faker import Faker

# Create a Faker instance
fake = Faker()

# Define the number of records you want to generate
num_records = 10001

# Generate fake data
data = []
for _ in range(num_records):    
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    phone_number = fake.phone_number()
    email = fake.email()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
    license_plate = fake.license_plate()
    data.append([first_name, last_name, address, phone_number, email, date_of_birth, license_plate])

# Create a DataFrame
df = pd.DataFrame(data, columns=['First Name', 'Last Name', 'Address', 'Phone Number', 'Email', 'Date of Birth', 'License Plate'])

# Save DataFrame to Excel file
df.to_excel('fake_data.xlsx', index=False)
