import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:fc1d2ec4@crash-cluster.m8hdb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client["crash-database"]

users = db["users"]
games = db["games"]

def new_user(dict):
    users.insert_one(dict)

def get_balance(username):
    return users.find_one({"username": username})["balance"]

def set_balance(username, balance):
    users.update({"username": username}, {"$set": {"balance": balance}})

def find_user(query):
    doc = users.find_one({"username": query})
    if doc == None:
        return False
    else:
        return True
