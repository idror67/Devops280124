# bolilerplate for flask app
from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

# Connect to MySQL database
db = mysql.connector.connect(
   host=os.getenv("DB_HOST", "localhost"),
   user=os.getenv("DB_USER", "root"),
   password=os.getenv("DB_PASSWORD", "admin"),
)


def create_db():
    db_name = os.getenv('DB_NAME', 'contacts_app')
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.execute(f"USE {db_name}")
    db.commit()
    print(f"Database {db_name} created successfully")


def create_contacts_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts ("
                   "number INT AUTO_INCREMENT PRIMARY KEY,"
                   "name VARCHAR(255) NOT NULL,"
                   "phone VARCHAR(255),"
                   "email VARCHAR(255) NOT NULL,"
                   "gender VARCHAR(10),"
                   "photo  VARCHAR(255))")
    db.commit()
    print("Table created successfully")



cursor = db.cursor(dictionary=True)
create_db()
create_contacts_table()




############## MYSQL Functions ####################
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



##################################################################
########## ROUTES ################################################
##################################################################

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/addContact')
def addContact():
    return render_template('addContactsForm.html')


@app.route('/createContact', methods=['POST'])
def createContact():
	# adding the contact to the list (to the database)
	fullname = request.form['fullname']
	email = request.form['email']
	phone = request.form['phone']
	gender = request.form['gender']
	photo = request.files['photo']
	if not check_contact_exist(fullname, email):			
		if photo:
			# create a full name for the file to be saved
			file_path = 'static/images/' + fullname + '.png'   # "hound"   -> 'static/images/hound.png
			# save the file in the server
			photo.save(file_path)   
	
		create_contact(fullname, phone, email, gender, f'{fullname}.png')
		return redirect('/viewContacts')
	else: 
		return render_template('addContactsForm.html', message = 'Contact already exists')
 

@app.route('/viewContacts')
def viewContacts():
    return render_template('contactsTable.html' , contacts = get_contacts())



@app.route('/deleteContact/<int:number>')
def deleteContact(number): # number = 2
	delete_contact(number)
	return redirect('/viewContacts')

# edit contact route
@app.route('/editContact/<int:number>')
def editContact(number):
	contact = findByNumber(number)
	return render_template('editContactForm.html', contact = contact)



@app.route('/search', methods=['POST'])
def search():
	contact_name = request.form['search_name']
	filtered_contacts = search_contact(contact_name)
	return render_template('contactsTable.html', contacts = filtered_contacts)
   

@app.route('/saveUpdatedContact/<int:number>', methods=['POST'])
def saveUpdatedContact(number):
	name = request.form['fullname']
	phone = request.form['phone']
	email = request.form['email']
	gender = request.form['gender']
	update_contact(number, name, phone, email, gender)
	return redirect('/viewContacts')




if __name__ == '__main__':
    app.run(debug=True, port=5000)