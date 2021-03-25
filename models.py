# mongo model
import pymongo
from model.pymongo_model import SimpleModel
from __init__ import mongo_client
# import os

# MONGO_KEY = os.getenv('MONGO_KEY')
# client = pymongo.MongoClient(MONGO_KEY)
# db = client["mongotest"]

db = mongo_client.db

class Users(SimpleModel):
    collection = db.Users


# Creating a new document
# first_user = Users({"username":"Laurion", "name":"Cris"})
# first_user.save() to commit 