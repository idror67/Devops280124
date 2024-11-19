# bolilerplate for flask app
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contacts_list = [
				{
					'number': 1,
					'name': 'Arja Stark',
					'phone': '044545',
					'email': 'Valan.Margulis@Winterfel.com',
					'photo': 'arja.png'
				},
                {
					'number': 2,
					'name': 'John Snow',
					'phone': '1132423',
					'email': 'john@theWall.com',
					'photo': 'john.png'
				},
                {
					'number': 3,
					'name': 'Thyrion Lannister',
					'phone': '234',
					'email': 'thyrion@KL.com',
					'photo': 'Thyrion.png'
				}				
]


# the function finds the contact by its number
def findByNumber(number):  # number = 2
	for contact in contacts_list:
		if contact['number'] == number:
			return contact
	return None



@app.route('/')
def welcome():
    return render_template('welcome.html')


# Create 2 routes for add contact 
# page and for view contacts list 
# page 
# /addContact  
# /viewContacts
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
	if photo:
		# create a full name for the file to be saved
		file_path = 'static/images/' + fullname + '.png'
		# save the file in the server
		photo.save(file_path)   
  
	new_contact = {
		'number': len(contacts_list) + 1,
		'name': fullname,
		'phone': phone,
		'email': email,
		'photo': fullname + '.png'
	}
	contacts_list.append(new_contact)
	return redirect('/viewContacts')
    
 

@app.route('/viewContacts')
def viewContacts():
    return render_template('contactsTable.html' , contacts = contacts_list)

# /deleteContact/2

@app.route('/deleteContact/<int:number>')
def deleteContact(number): # number = 2
	contact = findByNumber(number) # number = 2 contact = jon snow
	if contact: 
		contacts_list.remove(contact)
	return redirect('/viewContacts')



 




if __name__ == '__main__':
    app.run(debug=True, port=5000)