
import json
from pymongo import MongoClient

def mongo_conn(json_strings):


    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string

    # Select database
    db = client["pii"]  # Replace with your database name

    # Select collection
    collection = db["personal_information"]  # Replace with your collection name

    # Convert JSON strings to dictionaries
    data = [json.loads(json_str) for json_str in json_strings]

    # Insert data into the collection
    collection.insert_many(data)

    # Close the connection
    client.close()
