from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://Ijass:HICr32ALYGYRDUGo@python.lvsvs4f.mongodb.net/?retryWrites=true&w=majority&appName=PYTHON"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# CRUD commands

# C - Create
# R - Read
# U - Update
# D - Delete


# creating a database

db = client["OA_PY_JAN_4_5"]

# creating a collection

student = db["Students"]

# insert a document

# doc = {
#     "firstName": "Alice",
#     "lastName": "Johnson",
#     "email": "alice@gmail.com",
#     "mobileNumber": "Johnson",
#     "age": 20,
#     "address": {
#         "doorNo": 15,
#         "street": "ABC Street",
#         "city": "Chennai",
#         "state": "Tamil Nadu",
#         "country": "India",
#         "pincode": 600001,
#     },
#     "skills": ["PYTHON", "JAVA", "JAVASCRIPT"],
# }

# student.insert_one(doc)

# insert multiple documents

# data = [
#     {
#         "firstName": "Bob",
#         "lastName": "Smith",
#         "email": "bob@gmail.com",
#         "mobileNumber": "+91-9876543210",
#         "age": 25,
#         "address": {
#             "doorNo": 42,
#             "street": "XYZ Avenue",
#             "city": "Mumbai",
#             "state": "Maharashtra",
#             "country": "India",
#             "pincode": 400001,
#         },
#         "skills": ["C++", "JAVA", "REACT"],
#     },
#     {
#         "firstName": "Charlie",
#         "lastName": "Brown",
#         "email": "charlie@gmail.com",
#         "mobileNumber": "+91-1122334455",
#         "age": 22,
#         "address": {
#             "doorNo": 78,
#             "street": "DEF Lane",
#             "city": "Bengaluru",
#             "state": "Karnataka",
#             "country": "India",
#             "pincode": 560001,
#         },
#         "skills": ["PYTHON", "ANGULAR", "NODEJS"],
#     },
#     {
#         "firstName": "Diana",
#         "lastName": "Prince",
#         "email": "diana@gmail.com",
#         "mobileNumber": "+91-5566778899",
#         "age": 28,
#         "address": {
#             "doorNo": 3,
#             "street": "GHI Street",
#             "city": "Hyderabad",
#             "state": "Telangana",
#             "country": "India",
#             "pincode": 500001,
#         },
#         "skills": ["JAVA", "SPRING", "MYSQL"],
#     },
#     {
#         "firstName": "Eve",
#         "lastName": "Adams",
#         "email": "eve@gmail.com",
#         "mobileNumber": "+91-9988776655",
#         "age": 30,
#         "address": {
#             "doorNo": 88,
#             "street": "JKL Boulevard",
#             "city": "Delhi",
#             "state": "Delhi",
#             "country": "India",
#             "pincode": 110001,
#         },
#         "skills": ["HTML", "CSS", "JAVASCRIPT"],
#     },
#     {
#         "firstName": "Frank",
#         "lastName": "Wright",
#         "email": "frank@gmail.com",
#         "mobileNumber": "+91-5544332211",
#         "age": 27,
#         "address": {
#             "doorNo": 54,
#             "street": "MNO Road",
#             "city": "Kolkata",
#             "state": "West Bengal",
#             "country": "India",
#             "pincode": 700001,
#         },
#         "skills": ["PYTHON", "DJANGO", "POSTGRESQL"],
#     },
#     {
#         "firstName": "Grace",
#         "lastName": "Hopper",
#         "email": "grace@gmail.com",
#         "mobileNumber": "+91-6677889900",
#         "age": 32,
#         "address": {
#             "doorNo": 23,
#             "street": "PQR Street",
#             "city": "Pune",
#             "state": "Maharashtra",
#             "country": "India",
#             "pincode": 411001,
#         },
#         "skills": ["JAVA", "KOTLIN", "ANDROID"],
#     },
#     {
#         "firstName": "Henry",
#         "lastName": "Ford",
#         "email": "henry@gmail.com",
#         "mobileNumber": "+91-4433221100",
#         "age": 29,
#         "address": {
#             "doorNo": 67,
#             "street": "STU Avenue",
#             "city": "Ahmedabad",
#             "state": "Gujarat",
#             "country": "India",
#             "pincode": 380001,
#         },
#         "skills": ["REACT", "NODEJS", "MONGODB"],
#     },
#     {
#         "firstName": "Ivy",
#         "lastName": "Green",
#         "email": "ivy@gmail.com",
#         "mobileNumber": "+91-1234432100",
#         "age": 24,
#         "address": {
#             "doorNo": 90,
#             "street": "VWX Street",
#             "city": "Chandigarh",
#             "state": "Chandigarh",
#             "country": "India",
#             "pincode": 160001,
#         },
#         "skills": ["RUBY", "RAILS", "JAVASCRIPT"],
#     },
#     {
#         "firstName": "Jack",
#         "lastName": "Ryan",
#         "email": "jack@gmail.com",
#         "mobileNumber": "+91-2233445566",
#         "age": 26,
#         "address": {
#             "doorNo": 101,
#             "street": "YZA Boulevard",
#             "city": "Jaipur",
#             "state": "Rajasthan",
#             "country": "India",
#             "pincode": 302001,
#         },
#         "skills": ["GO", "PYTHON", "KUBERNETES"],
#     },
# ]


# student.insert_many(data)

# find all documents

# result = student.find()

# find one document

filter = {"_id": ObjectId("664dd6b7dc52703dddddc369")}

result = student.find_one(filter)

print(result["firstName"])
print(result["lastName"])
print(result["address"])
