from flask import Flask, render_template
import requests

def addCountry(name):
   url = 'http://localhost:5000/api/addCountry'
   data = {
      'name': name
   }
   response = requests.post(url, json=data)
   print(response.json())
   return response.json()

def getCountries():
   url = 'http://localhost:5000/api/countries'
   response = requests.get(url)
   print(response.json())
   return response.json()


getCountries()