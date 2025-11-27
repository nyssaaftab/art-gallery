from db import artworks_collection, notes_collection
from models import Artwork, Note
import random
from datetime import datetime
import uuid


def get_random_artwork():
    count = artworks_collection.count_documents({})
    if count == 0:
        return None
    idx = random.randint(0, count-1)
    artwork_data = artworks_collection.find().limit(1).skip(idx)[0]
    return Artwork(**artwork_data)

def get_daily_artwork():
    today = datetime.utcnow().date()
    seed = int(today.strftime("%Y%m%d"))

    count = artworks_collection.count_documents({})
    if count == 0:
        return None

    daily_random = random.Random(seed)
    idx = daily_random.randint(0, count - 1)

    artwork_data = artworks_collection.find().limit(1).skip(idx)[0]
    return Artwork(**artwork_data)

def create_note(artwork_id, text, name=None, location=None):
    note_data = {
        "id": str(uuid.uuid4()),
          "artwork_id": artwork_id,
          "text": text,
          "created_at": datetime.utcnow(),
          "name": name,
          "location": location
    }
    notes_collection.insert_one(note_data)
    return Note(**note_data)

def get_random_note(artwork_id):
    notes = list(notes_collection.find({"artwork_id": artwork_id}))

    if not notes:
        return None
    
    random_note = random.choice(notes)
    return Note(**random_note)

