import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()



############## MYSQL Functions ####################


# Connect to MySQL database
db = mysql.connector.connect(
   host=os.getenv("DB_HOST", "localhost"),
   user=os.getenv("DB_USER", "root"),
   password=os.getenv("DB_PASSWORD", "admin"),
   port=os.getenv("DB_PORT", "3306"),
   
)

def create_db():
   database=os.getenv("DB_NAME", "contacts_app")
   cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
   cursor.execute(f"USE {database}")
   db.commit()
   print(f"Database {database} created successfully")


def create_contacts_table():
	cursor.execute("Create Table IF NOT EXISTS contacts"
				   "(number INT AUTO_INCREMENT PRIMARY KEY,"
				   "name VARCHAR(255) not null,"
				   "phone VARCHAR(255),"
				   "email VARCHAR(255) not null,"
				   "gender VARCHAR(255),"
				   "photo VARCHAR(255))")
	db.commit()
	print("Table contacts created successfully")

cursor = db.cursor(dictionary=True)
# create database 
create_db()
# create contacts table
create_contacts_table()



def get_contacts():
   cursor.execute("SELECT * FROM contacts")
   result = cursor.fetchall()
   return result


# the function finds the contact by its number
def findByNumber(number):  # number = 2
	contacts_list = get_contacts()
	for contact in contacts_list:
		if contact['number'] == number:
			return contact
	return None


# the function checks if the contact exists by its name or email
def check_contact_exist(name, email):
	cursor.execute("SELECT * FROM contacts WHERE name = %s OR email = %s", (name, email))
	result = cursor.fetchone()
	return bool(result)


# function to search for the contact by its name
def search_contact(name):
	cursor.execute("SELECT * FROM contacts WHERE name LIKE %s", ('%' + name + '%',))
	result = cursor.fetchall()
	return result


# create contact in the database
def create_contact(name, phone, email, gender, photo):
	cursor.execute("INSERT INTO contacts (name, phone, email, gender, photo) VALUES (%s, %s, %s, %s, %s)", (name, phone, email, gender, photo))
	db.commit()
	return f"Contact {name} added successfully"


# delete contact from the database
def delete_contact(number):
	cursor.execute("DELETE FROM contacts WHERE number = %s", (number,))
	db.commit()
	return f"Contact {number} deleted successfully"


# update contact in the database
def update_contact(number, name, phone, email, gender):
   cursor.execute("UPDATE contacts SET name = %s, phone = %s, email = %s, gender = %s WHERE number = %s",
                  (name, phone, email, gender, number))
   db.commit()

