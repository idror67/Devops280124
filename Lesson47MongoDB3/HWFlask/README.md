
# Flask Contacts Management Application

This is a Flask-based web application that allows users to manage contacts. The application supports adding, viewing, editing, deleting, and searching contacts. It also supports the use of different databases, such as **MySQL** or **MongoDB**, based on an environment variable setting.

## Features

- Add a new contact (name, email, phone, gender, and photo)
- View a list of all contacts
- Edit an existing contact
- Delete a contact
- Search contacts by name
- Save contact photos in the `static/images` directory

## Prerequisites

- Python 3.x
- Flask
- `python-dotenv` package for environment variable management
- A database (either **MySQL** or **MongoDB**) based on your choice

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/fullstackjava082023/Devops28012024.git
    cd Devops28012024
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory.
    - Set the database type to either `MYSQL` or `MONGO`.

    Example `.env` file:

    ```bash
    DATABASE_TYPE=MONGO
    ```

5. Set up your database:
    - **MySQL**: Ensure that the `data_sql.py` file contains functions for interacting with the MySQL database.
    - **MongoDB**: Ensure that the `data_mongo.py` file contains functions for interacting with the MongoDB database.

6. Ensure that the `static/images/` directory exists:

    ```bash
    mkdir -p static/images
    ```

## Running the Application

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. The app will be available at `http://127.0.0.1:5000/`.

## Endpoints

- **Home Page (Welcome)**: `GET /`
- **Add Contact**: `GET /addContact`
- **Create Contact**: `POST /createContact`
- **View Contacts**: `GET /viewContacts`
- **Delete Contact**: `GET /deleteContact/<number>`
- **Edit Contact**: `GET /editContact/<number>`
- **Save Updated Contact**: `POST /saveUpdatedContact/<number>`
- **Search Contacts**: `POST /search`

## Example Forms

### Add Contact Form (HTML Example):

```html
<form action="/createContact" method="POST" enctype="multipart/form-data">
    <input type="text" name="fullname" placeholder="Full Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="tel" name="phone" placeholder="Phone" required>
    <input type="text" name="gender" placeholder="Gender" required>
    <input type="file" name="photo" required>
    <button type="submit">Submit</button>
</form>
```

## Database Configuration

This app supports both **MySQL** and **MongoDB**. Depending on your configuration, the app will dynamically import the respective database interaction functions from either `data_sql.py` or `data_mongo.py`.

### MySQL

Ensure that `data_sql.py` contains functions to:
- Get contacts
- Create a contact
- Delete a contact
- Update a contact
- Check if a contact exists

### MongoDB

Similarly, ensure `data_mongo.py` contains the same functions for interacting with a MongoDB database.

## Folder Structure

```
.
├── app.py                # Main application file
├── templates/            # HTML templates
│   ├── addContactsForm.html
│   ├── contactsTable.html
│   ├── editContactForm.html
│   └── welcome.html
├── static/
│   └── images/           # Directory to store contact photos
├── data_sql.py           # MySQL database interactions (to be implemented)
├── data_mongo.py         # MongoDB database interactions (to be implemented)
├── .env                  # Environment variables file
├── requirements.txt      # Python dependencies
└── README.md             # This README file
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
