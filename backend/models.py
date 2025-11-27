from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime



class Artwork(BaseModel):
    id: str
    title: str
    artist: str
    image_url: str
    source: Optional[str] = None

class Note(BaseModel):
    id: str
    artwork_id: str
    text: str
    created_at: datetime
    name: Optional[str] = None
    location: Optional[str] = None

class NoteCreate(BaseModel):
    text: str
    name: Optional[str] = None
    location: Optional[str] = None