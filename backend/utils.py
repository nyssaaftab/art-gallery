import requests
from models import Artwork
import json
from db import artworks_collection
import time


def get_image_url(base_endpt, image_id):
    return f"{base_endpt}/{image_id}/full/843,/0/default.jpg"

def fetch_batch(page=1, limit=100):
    url = "https://api.artic.edu/api/v1/artworks/search"


    params = {
          "query[bool][should][0][match][artwork_type_title]": "Painting",
          "query[bool][should][1][match][artwork_type_title]": "Print",
          "query[bool][should][2][match][artwork_type_title]": "Drawing and Watercolor",
          "query[bool][should][3][match][artwork_type_title]": "Mixed Media",
          "query[bool][should][4][match][artwork_type_title]": "Photograph",
          "query[bool][should][5][match][artwork_type_title]": "Miniature Painting",
          "query[bool][should][6][match][artwork_type_title]": "Graphic Design",
          "query[bool][must][0][exists][field]": "image_id",
          "query[bool][minimum_should_match]": "1",
          "fields": "id,title,artist_title,image_id,artwork_type_title",
          "limit": limit,
          "page": page
      }
    
    response = requests.get(url, params=params)
    data = response.json()

    return {
        "artworks": data.get("data", []),
        "config": data.get("config", {})
    }

def transform_artwork(raw_artwork, iiif_base_url):
     
    try:
          artwork = Artwork(
               id=str(raw_artwork["id"]),
               title = raw_artwork.get("title", "Untitled"),
               artist = raw_artwork.get("artist_title") or "Unknown Artist",
               image_url = get_image_url(iiif_base_url, raw_artwork["image_id"]),
               source = "chicago"
            )
          return artwork
    except Exception as e:
          print(f"Error transforming artwork {raw_artwork.get('id')}: {e}")
          return None
     
    
def seed_artworks(target_count=1000):
     
    stored_count = 0
    page = 1
    to_insert = []

    print(f"Starting seed process. Target: {target_count} artworks")
    
    while stored_count < target_count:
        print (f"fetching page {page}...")

        result = fetch_batch(page=page, limit=100)
        iiif_url = result["config"].get('iiif_url')

        if not result['artworks']:
             print(f"no more artworks available.")
             break
        
        for raw in result['artworks']:
            artwork = transform_artwork(raw, iiif_url)
            if artwork:
              to_insert.append(artwork.model_dump())
              stored_count += 1
              if stored_count >= target_count:
                  break
        
        print(f"Progress: {stored_count}/{target_count}")
        time.sleep(1)
        page += 1
    
    if to_insert:
        try:
            result = artworks_collection.insert_many(to_insert, ordered=False)
            print(f"\n✅ Successfully inserted {len(result.inserted_ids)} artworks into database")
            return len(result.inserted_ids)
        except Exception as e:
            print(f"Error inserting artworks: {e}")
            return 0

    return 0

    

if __name__ == "__main__":
      # Check current count
      current_count = artworks_collection.count_documents({})
      print(f"Current artworks in database: {current_count}\n")

      # Seed
      response = input("Seed 1000 artworks? (y/n): ")
      if response.lower() == 'y':
          seed_artworks(target_count=1000)
          print(f"\nFinal count: {artworks_collection.count_documents({})} artworks")

