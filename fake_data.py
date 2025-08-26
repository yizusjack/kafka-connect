import csv
from faker import Faker
from datetime import datetime

fake = Faker()

with open('fake/customers.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['first_name', 'last_name', 'email', 'created_at'])

    for _ in range(50000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([first_name, last_name, email, created_at])

print("customers.csv file generated successfully.")