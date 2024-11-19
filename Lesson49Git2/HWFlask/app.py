# bolilerplate for flask app
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
load_dotenv()


db_to_use = os.getenv("DATABASE_TYPE", "MONGO") # "MYSQL" or "MONGO"

if db_to_use == "MYSQL":
	from data_sql import (get_contacts, create_contact, delete_contact, 
						findByNumber, update_contact, search_contact, 
						check_contact_exist)
elif db_to_use == "MONGO":
	from data_mongo import (get_contacts, create_contact, delete_contact, 
						findByNumber, update_contact, search_contact, 
						check_contact_exist)




app = Flask(__name__)



##################################################################
########## ROUTES ################################################
##################################################################

@app.route('/')
def welcome():
    return render_template('smelcome.html')


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
			file_path = 'HWFlask/static/images/' + fullname + '.png'   # "hound"   -> 'static/images/hound.png
			# save the file in the server
			photo.save(file_path)   
	
		create_contact(fullname, phone, email, gender, f'{fullname}.png')
		return redirect('/viewContacts')
	else: 
		return render_template('addContactsForm.html', message = 'Contact already exists')
 

@app.route('/viewContacts')
def viewContacts():
    return render_template('contactsTable.html' , contacts = get_contacts())



@app.route('/deleteContact/<number>')
def deleteContact(number): # number = 2
	delete_contact(number)
	return redirect('/viewContacts')

# edit contact route
@app.route('/editContact/<number>')
def editContact(number):
	contact = findByNumber(number)
	return render_template('editContactForm.html', contact = contact)



@app.route('/search', methods=['POST'])
def search():
	contact_name = request.form['search_name']
	filtered_contacts = search_contact(contact_name)
	return render_template('contactsTable.html', contacts = filtered_contacts)
   

@app.route('/saveUpdatedContact/<number>', methods=['POST'])
def saveUpdatedContact(number):
	name = request.form['fullname']
	phone = request.form['phone']
	email = request.form['email']
	gender = request.form['gender']
	update_contact(number, name, phone, email, gender)
	return redirect('/viewContacts')




if __name__ == '__main__':
    app.run(debug=True, port=5000)