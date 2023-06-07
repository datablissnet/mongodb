from pymongo import MongoClient

# Create a MongoClient object
print("Connecting to mongodb server")
connecturl = 'mongodb://localhost:27017/'
connection = MongoClient(connecturl)


# get database list
print("Getting list of databases")
dbs = connection.list_database_names()

for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")
# close the server connecton
# close the server connecton
connection.close()