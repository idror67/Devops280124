from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector

db = mysql.connector.connect(
      host="localhost",
      user="root",
      password="admin",
      port = "3306",
      database = "flights_system"
)

# create cursor which is returning json data
cursor = db.cursor(dictionary=True)

#create basic flask boilerplate
app = Flask(__name__)

# print(db)
# create database flights_system
# cursor.execute("CREATE DATABASE IF NOT EXISTS flights_system")

def get_countries():
   query = "select * from countries"
   cursor.execute(query)
   countries = cursor.fetchall()
   print(countries)
   return countries

def get_country_by_id(id):
   countries = get_countries()
   for country in countries:
      if country[0] == id:
         return country
   return None

def get_country_by_id_from_db(id):
   query = f"select * from countries where id = {id}"
   cursor.execute(query)
   country = cursor.fetchone()
   return country

def get_country_by_id_secured(id):
   query = "select * from countries where id = %s"
   cursor.execute(query, (id,))
   country = cursor.fetchone()
   return country


def insert_country_by_name(name):
   query = f"insert into countries (name) values ('{name}')"
   cursor.execute(query)
   db.commit()
   return f"Country inserted successfully {cursor.lastrowid}"

# print(get_country_by_id_from_db(3))
# print(insert_country_by_name("Bulgary"))




#route to show all countries from DB
@app.route('/api/countries/')
def countries_api():
   countries = get_countries()
   return jsonify(countries)

#route to show a specific country from DB
@app.route('/api/countries/<id>/')
def country_by_id_api(id):
   country = get_country_by_id_secured(id)
   return jsonify(country)

#route to insert a country in DB
@app.route('/api/addCountry/', methods=['POST'])
def add_country_api():
   name = request.json['name']
   result = insert_country_by_name(name)
   return jsonify(result)


if __name__ == '__main__':
   # allow external connections
   app.run(host='0.0.0.0', debug=True, port=5000)
   
   