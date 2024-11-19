import pymongo

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# Create a database called "mydatabase":
mydb = myclient["mydatabase"]
# Create a collection called "customers":
mycol = mydb["customers"]

# # Insert a record in the "customers" collection:
# mydict = { "name": "John", "address": "Highway 37" }
# # Insert the dictionary into the collection
# result = mycol.insert_one(mydict)
# # Print the unique id of the inserted record
# print(result.inserted_id)

# mylist = [
#  { "name": "Amy", "address": "Apple st 652"},
#  { "name": "Hannah", "address": "Mountain 21"},
#  { "name": "Michael", "address": "Valley 345"},
#  { "name": "Sandy", "address": "Ocean blvd 2"},
#  { "name": "Betty", "address": "Green Grass 1"},
#  { "name": "Richard", "address": "Sky st 331"},
#  { "name": "Susan", "address": "One way 98"},
#  { "name": "Vicky", "address": "Yellow Garden 2"},
#  { "name": "Ben", "address": "Park Lane 38"},
#  { "name": "William", "address": "Central st 954"},
#  { "name": "Chuck", "address": "Main Road 989"},
#  { "name": "Viola", "address": "Sideway 1633"}
# ]
# # Insert multiple documents into the collection
# result = mycol.insert_many(mylist)
# # Print the unique ids of the inserted records
# print(result.inserted_ids)


# result = mycol.find_one()

# print(result)

# # to find all documents in the collection
# result = mycol.find()

# result = mycol.find({}, {"_id": 0, "name": 1})

# query = { "address": "Park Lane 38" }

# query = {"address": {"$gt": "S"}}

# result = mycol.find(query).sort({"name": -1})

# update the document with addres Valley 345 to sherlock holmes address
# myquery = {"address": "Valley 345"}
# newvalues = {"$set": {"address": "Baker Street 221B"}}
# mycol.update_one(myquery, newvalues)

# update all customers with address starts with S set name to be Minnie
# myquery = {"address": {"$regex": "^S"}}
# newvalues = {"$set": {"name": "Minnie"}}
# mycol.update_many(myquery, newvalues)


# 3 - update the document with name Betty to be name: Arja Stark and address to be Winterfell
# mycol.update_one({"name": 'Betty'}, {"$set" : {"name": "Arja Stark", "address": "Winterfell"}})

# query = {"address" : "Mountain 21"}
# mycol.delete_one(query)

# query = {"address": {"$regex": "^S"}}
# # mycol.delete_many(query)
# mycol.delete_many({})

# drop the collection
mycol.drop()

# drop the database
myclient.drop_database("mydatabase")

# Print all the results
for document in mycol.find():
    print(document)
