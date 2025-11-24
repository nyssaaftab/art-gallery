from fastapi import FastAPI
from db import artworks_collection, client

app = FastAPI(title="Community Gallery Widget API")

@app.get("/")
def read_root():
    return {"message": "Hello, gallery widget backend!"}

@app.get("/test-db")
def test_db():
    try:
        count = artworks_collection.count_documents({})
        return {"status": "success", "artworks_count": count}
    except Exception as e:
        return {"status": "error", "detail": str(e)}