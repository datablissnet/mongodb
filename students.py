from pymongo import MongoClient

# Create a MongoClient object
print("Connecting to mongodb server")
uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)


# select the 'training' database 
campusDB = client.campusManagementDB

# select the 'python' collection 
students = campusDB.students


# create documents
student1 = {    "firstname":"John",
                "lastName": "Doe",
                "email": "john.doe@gmail.com",
                'studentID': 20217484
            }

student_list = [{"firstname":"Amy", 
                "lastName":"Goe",
                "email": "amy.goe@gmail.com",
                'studentID': 20217492},
                {"firstname":"Sara", 
                "lastName": "Doe",
                "email": "sara.jane@gmail.com",
                'studentID': 20217485},
                
            ]

# insert One
print("Inserting documents into collection.")
students.insert_one(student1)

# insert many
print("Inserting students list.")
students.insert_many(student_list)

# find the first student
print("Find the first student.")
students.find_one()

# find the first student
print("Find email: amy.goe@gmail.com")
students.find_one({"email": "amy.goe@gmail.com"})

# find()
print("Find lastName:Doe")
students.find({"lastName": "Doe"})

# Count documents with "lastName": "Doe"
students.count_documents({"lastName": "Doe"})

# Replace
print("Replacement")
arslan = students.find_one({"lastName": "Doe"})
arslan["lastName"] = "Arslan"
arslan["email"] = "arslan@gmail.com"
students.replace_one({"lastName": "Doe"}, arslan)
print(students.find_one({"lastName": "Arslan"}))


# Update
print("update")
student = students.find_one({"lastName": "Arslan"})
changes = {"$set": {"firstname": "Ertan"}}

students.update_one({"lastName": "Arslan"}, changes)

print(students.find_one({"lastName": "Arslan"}))

students.update_many({}, {"$set": {"onlineOnly":True}})

for i in students.find():
    print(i)
                     
# close the server connecton
print("Closing the connection.")
client.close()