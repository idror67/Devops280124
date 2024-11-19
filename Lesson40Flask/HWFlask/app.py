# bolilerplate for flask app
from flask import Flask, render_template

app = Flask(__name__)


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

@app.route('/viewContacts')
def viewContacts():
    return render_template('contactsTable.html')




if __name__ == '__main__':
    app.run(debug=True, port=5000)