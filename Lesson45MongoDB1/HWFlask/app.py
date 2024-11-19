# bolilerplate for flask app
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


# Connect to MySQL database
db = mysql.connector.connect(
   host="localhost",
   user="root",
   password="admin",
   database="contacts_app"
)

cursor = db.cursor(dictionary=True)


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



@app.route('/search', methods=['POST'])
def search():
	contact_name = request.form['search_name']
	filtered_contacts = search_contact(contact_name)
	return render_template('contactsTable.html', contacts = filtered_contacts)
   




if __name__ == '__main__':
    app.run(debug=True, port=5000)