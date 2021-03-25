# DATABASE 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "dsofos23nds62535"

# DATABASE CONFIG INPUT
# username = ""
# password = ""
server = "localhost:27017"

dbname = "mongotest"

# MYSQL DATABASE
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{}:{}@{}/{}".format(username, password, server, dbname)
# app.config["SQLALCHEMY_DATABASE_MODIFICATIONS"] = False

# MONGO DATABASE
app.config["MONGO_URI"] = "mongodb://{}/{}".format(server, dbname)

mongo_client = PyMongo(app)
# db = SQLAlchemy(app)