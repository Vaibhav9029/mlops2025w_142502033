

from pymongo import MongoClient
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Connect to MongoDB (default localhost:27017)
client = MongoClient('mongodb://localhost:27017/')

# Create database
db = client['my_random_db']

# Create collection
collection = db['random_records']

# Generate and insert 100 random records
records = []
for _ in range(100):
    record = {
        "name": fake.name(),
        "email": fake.email(),
        "age": random.randint(18, 70),
        "address": fake.address(),
        "phone": fake.phone_number()
    }
    records.append(record)

# Insert records into MongoDB
collection.insert_many(records)

print("100 random records inserted successfully!")

# Optional: print first 5 records
for doc in collection.find().limit(5):
    print(doc)

