from pymongo import MongoClient

# Create a MongoClient object
print("Connecting to mongodb server")
connecturl = 'mongodb://localhost:27017/'
connection = MongoClient(connecturl)


# select the 'training' database 
db = connection.training
# select the 'python' collection 
collection = db.mongodb_glossary
# create documents
doc1 = {"database":"a database contains collections"}
doc2 = {"collection":"a collection stores the documents"}
doc3 = {"document":"a document contains the data in the form or key value pairs."}
# insert documents
print("Inserting documents into collection.")
db.collection.insert_one(doc1)
db.collection.insert_one(doc2)
db.collection.insert_one(doc3)
# query for all documents in 'training' database and 'python' collection
docs = db.collection.find()
print("Printing the documents in the collection.")
for document in docs:
    print(document)
# close the server connecton
print("Closing the connection.")
connection.close()