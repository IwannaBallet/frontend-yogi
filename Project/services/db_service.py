# services/db_service.py

from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Connect to MongoDB (use local or Atlas URI)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)

# Use your DB and collection
db = client["mo_meogeul_naeng"]
users_collection = db["users"]

def get_user(username):
    return users_collection.find_one({"username": username})

def create_user(user):
    users_collection.insert_one(user)
