
from database import SessionLocal
from model import Airport, Municipalities

db = SessionLocal()


# airports = db.query(Airport).all()  # Fetch all airports from the database
# for airoport in airports:
#     print(f"Airport ID: {airoport.id}, Type: {airoport.type}, Name: {airoport.name}, Score: {airoport.score}, Last Updated: {airoport.last_updated} ")

# regions = db.query(Municipalities).all()  # Fetch all regions from the database
# for region in regions:
#     print(f"Municipality: {region.municipality}, Region Name: {region.region_name}, elevation_ft:{region.elevation_ft},  Latitude: {region.latitude_deg}, Longitude: {region.longitude_deg}")

# type_airoport = db.query(Airport.type).distinct().all()  # Fetch distinct airport types from the database
# for type in type_airoport:
#     print(f"Type: {type}")  # type is a tuple, so we access the first element

