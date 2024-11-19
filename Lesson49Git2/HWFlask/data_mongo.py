import pymongo
from bson import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()



# Connect to MongoDB
myclient = pymongo.MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
# Create a database called "mydatabase":
mydb = myclient[os.getenv("DB_NAME", "contacts_app")]
# Create a collection called "customers":
my_collection = mydb["contacts"]

# implementation of the functions
# get_contacts, findByNumber, check_contact_exist,
# search_contacts, create_contact,
# delete_contact, update_contact_in_db in data_mongo.py

def get_contacts():
    return list(my_collection.find())

# the function finds the contact by its number
# _id is the number
def findByNumber(_id):
    return my_collection.find_one({"_id": ObjectId(_id)})

# the function checks if the contact exists by its name or email
def check_contact_exist(name, email):
    query = {"$or": [{"name": name}, {"email": email}]}
    result = my_collection.find_one(query)
    return bool(result)

# function to search for the contact by its name
def search_contact(name): 
    query = {"name": {"$regex" : name, "$options": "i"}}
    return list(my_collection.find(query))

def create_contact(name, phone, email, gender, photo):
    my_collection.insert_one(
        {"name": name, "phone": phone, "email": email,
         "gender": gender, "photo": photo}
    )
    return f"contact {name} added succesfully"

# delete contact from the database
def delete_contact(number):
    query = {"_id": ObjectId(number)}
    my_collection.delete_one(query)
    return f"Contact {number} deleted successfully"

# update contact in the database
def update_contact(number, name, phone, email, gender):
    my_collection.update_one(
        {"_id" : ObjectId(number)},
        {"$set": {"name" : name, "phone": phone,
                  "email": email, "gender": gender}}
    )
    return f"Contact {name} successfully"