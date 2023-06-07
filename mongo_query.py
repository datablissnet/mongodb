from pymongo import MongoClient

# Create a MongoClient object
print("Connecting to mongodb server")
connecturl = 'mongodb://localhost:27017/'
connection = MongoClient(connecturl)


# select the 'training' database 
db = connection.training

# select the 'python' collection 
collection = db.python

# create a sample document
doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}


# insert a sample document
print("Inserting a document into collection.")
db.collection.insert_one(doc)

docs = db.collection.find()
print("Printing the documents in the collection.")
for document in docs:
    print(document)

# close the server connecton
print("Closing the connection.")
connection.close()