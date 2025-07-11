from database import SessionLocal
from query_helper import *

db= SessionLocal()

#### Airoports

# airoports= get_airports(db)

# for airo in airoports:
#     print(f"Airoport_Id: {airo.id}, Type :{airo.type}, Municipality: {airo.municipality}, Score: {airo.score}, Last_updated:{airo.last_updated}")

## airoports par type

# airoports_type=get_types_airoprt(db,"small_airport")
# for airo in airoports_type:
#     print(f"Airoport_Id: {airo.id}, Type :{airo.type}, Municipality: {airo.municipality}, Score: {airo.score}, Last_updated:{airo.last_updated}")

## les airoports avec un score supérieur à 50
# airoports_score=get_score_airoprt(db)

# for airo in airoports_score:
#     print(f"Airoport_Id: {airo.id}, Type :{airo.type}, Municipality: {airo.municipality}, Score: {airo.score}, Last_updated:{airo.last_updated}")

## les airoports mis à jour par année
# airoports_anne=get_anne_airoprt(db,2008)  
# for airo in airoports_anne:
#     print(f"Airoport_Id: {airo.id}, Type :{airo.type}, Municipality: {airo.municipality}, Score: {airo.score}, Last_updated:{airo.last_updated}")

## les 5 airoports ayant la plus haute élévation
# airoports_top5_elevation=get_top5_elevation(db)
# for airo,elevation in airoports_top5_elevation:
#     print(f"Airoport_Id: {airo.id}, Type :{airo.type}, Municipality: {airo.municipality}, Score: {airo.score}, Elavation_lf:{elevation.elevation_ft}, Last_updated:{airo.last_updated}")   

### les airoports triés par date de mise à jour
# airoports_last_updated=get_last_updated_airoprt(db)   
# for airo in airoports_last_updated:
#     print(f"Airoport_Id: {airo.id}, Type :{airo.type}, Municipality: {airo.municipality}, Score: {airo.score}, Last_updated:{airo.last_updated}")




###MUNICIPALITIES

### les municipalités des airoports
# municipalities_airoprt=get_municipalities(db) 
# for municipality in municipalities_airoprt:
#     print(f"Municipality: {municipality.municipality}, Region Name: {municipality.region_name}, Latitude: {municipality.latitude_deg}, Longitude: {municipality.longitude_deg}")


### liste des régions
# regions = get_regions(db)     
# for region in regions:
#     print(f"Region Name: {region.region_name}") 

# ### nombre d'airoports par région
# airports_count_by_region = get_airports_count_by_region(db)
# for region in airports_count_by_region:
#     print(f"Region: {region.region_name}, Airport Count: {region.airport_count}")


## types d'airoports par région
# types_airoports_region = get_airport_types_by_region(db)
# for region, types in types_airoports_region:
#     print(f"Region: {region}, Airport Types: {types}")

### latitude et longitude et leurs score des municipalités 
# municipalities_lat_long = get_lat_long_score_by_municipality(db)
# for municipality in municipalities_lat_long:
#     print(f"Municipality: {municipality.municipality}, Latitude: {municipality.latitude_deg}, Longitude: {municipality.longitude_deg}, Score: {municipality.score}")  


## nombre d'airoports par type
# nombre_airoport=get_airports_count_by_type(db)
# for types, count in nombre_airoport:
#     print(f"Type :{types}, nombre :{count}")

## nombre de regions distinctes 
# nombre_regions =get_distinct_regions_count(db)
# print(f"Nombre de régions distinctes: {nombre_regions}")

## nombre d'airoports par type et par région distinct
# nombre_airoport_region = get_airports_count_by_type_and_region(db)
# for types, region,count in nombre_airoport_region:
#     print(f"Region: {region}, Type: {types}, Count: {count}")



### Statistiques
#nombre d'airoports par type
# nombre_airoport_type = get_airports_count_by_type(db)
# for types, count in nombre_airoport_type:
#     print(f"Type: {types}, Count: {count}")

# nombre total de scores par region
# total_scores_by_region = get_total_scores_by_region(db)     
# for region, total_score in total_scores_by_region:
#     print(f"Region: {region}, Total Score: {total_score}")

# nombre de score par municipalité
# scores_by_municipality = get_scores_by_municipality(db)     
# for municipality, total_score in scores_by_municipality:
#     print(f"Municipality: {municipality}, Total Score: {total_score}")


### nombre de municipalités distinctes
# nombre_municipalities = get_distinct_municipalities_count(db)
# print(f"Nombre de municipalités distinctes: {nombre_municipalities}")

###nombre total de score par region
total_scores_by_region = get_total_scores_by_region(db)
for region, total_score in total_scores_by_region:
    print(f"Region: {region}, Total Score: {total_score}")
db.close()  # Ferme la session de la base de données