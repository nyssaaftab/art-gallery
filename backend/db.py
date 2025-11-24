from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)

db = client['gallery-widget']    
artworks_collection = db.artworks
notes_collection = db.notes
users_collection = db.users
