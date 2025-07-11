from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import Optional
from model import *

### airports

def get_airports(db: Session):
    return db.query(Airport).all()

## airoports par type 
def get_types_airoprt(db:Session, type:String):
    query=db.query(Airport)
    return db.query(Airport).filter(Airport.type == type).all()


## airoports avec des options de filtrage 
def get_filtre_airports(db: Session, type: Optional[str] = None, 
                        municipality: Optional[str] = None,
                        score: Optional[int] = None, last_updated: Optional[int] = None):
    query = db.query(Airport)
    if type:
        query = query.filter(Airport.type == type)
    if municipality:
        query = query.filter(Airport.municipality == municipality)
    if score is not None:
        query = query.filter(Airport.score == score)
    if last_updated is not None:
        query = query.filter(Airport.last_updated == last_updated)
    
    return query.all()

## airoports avec un meilleurs score (score >50)
def get_score_airoprt(db:Session):
    return(
        db.query(Airport)
        .filter(Airport.score > 50)  # Exclude null values
        .order_by(Airport.score.desc())
        .limit(5)
        .all()
    )



## donneés mise à jour par années
def get_anne_airoprt(db:Session, year:int):
    return (
        db.query(Airport)
        .filter(Airport.last_updated == year)  # Filter by year
        .all()
    )

## les 5  airoports ayant  (la plus haute haltitude) elevations_lf
# def get_top5_elevation(db: Session):
#     return (
#         db.query(Airport, Municipalities)
#         .join(Municipalities)
#         .filter(Municipalities.elevation_ft != None)  # Exclude null values
#         .order_by(Municipalities.elevation_ft.desc())
#         .limit(5)
#         .all()
#     )
def get_top5_elevation(db: Session):
    results = (
        db.query(Airport, Municipalities)
        .join(Municipalities)
        .filter(Municipalities.elevation_ft != None)
        .order_by(Municipalities.elevation_ft.desc())
        .limit(5)
        .all()
    )

    return [
        {
            "Airport": airport,
            "municipality": municipality
        }
        for airport, municipality in results
    ]



### les données triées par last_updated
def get_last_updated_airoprt(db: Session):
    return (
        db.query(Airport)
        .filter(Airport.last_updated != None)  # Exclude null values
        .order_by(Airport.last_updated.desc())
        .all()
    )

### les municipalités
def get_municipalities(db: Session):
    return db.query(Municipalities).all()

### liste des regions distinctes 
def get_regions(db: Session):
    return (
        db.query(Municipalities.region_name) 
        .distinct()
        .all()
    )

# ### nombre d'airoports par région
def get_airports_count_by_region(db: Session):  
    return (
        db.query(Municipalities.region_name, func.count(Airport.id).label('airport_count'))
        .join(Airport)
        .group_by(Municipalities.region_name)
        .all()
    )

### municipalities par région
def get_municipalities_by_region(db: Session):  
    return (
        db.query(Municipalities.region_name, Municipalities.municipality)
        .filter(Municipalities.municipality != None)  # Exclude null values
        .distinct()
        .all()
    )
###types d'airoports par région
def get_airport_types_by_region(db: Session):
    return (
        db.query(Region.region_name, Airport.type)
        .join(Airport)
        .filter(Airport.type != None)  # Exclude null values
        .distinct()
        .all()
    )

### latitude et longitude et leurs score des municipalités 
def get_lat_long_score_by_municipality(db: Session):
    return (
        db.query(Region.municipality, Region.latitude_deg, Region.longitude_deg, Airport.score)
        .join(Airport)
        .filter(Airport.score != None)  # Exclude null scores
        .all()
    )


### latitude et la longitude des municipalités et leurs score
def get_lat_long_score_by_municipality(db: Session):
    return (
        db.query(Municipalities.municipality, Municipalities.latitude_deg, Municipalities.longitude_deg, Airport.score)
        .join(Airport)
        .filter(Airport.score != None)  # Exclude null scores
        .all()
    )



### Statistiques

# ### nombre de score par municipalité
def get_scores_by_municipality(db: Session):
    return (
        db.query(Region.municipality, func.sum(Airport.score).label('total_score'))
        .join(Airport)
        .group_by(Region.municipality)
        .all()
    )

### nombre d'airoports par type
def get_airports_count_by_type(db: Session):
    return (
        db.query(Airport.type, func.count(Airport.id).label('airport_count'))
        .group_by(Airport.type)
        .all()
    )

## nombre d'airoports par type et par région distinct
def get_airports_count_by_type_and_region(db: Session):
    return (
        db.query(Airport.type, Municipalities.region_name, func.count(Airport.id).label('airport_count'))
        .join(Municipalities)
        .group_by(Airport.type, Municipalities.region_name)
        .all()
    )

### nombre de municipalités distinctes
def get_distinct_municipalities_count(db: Session):
    return (
        db.query(func.count(Municipalities.municipality.distinct())).scalar()
    )

## nombre de regions distinctes
def get_distinct_regions_count(db: Session):
    return (
        db.query(func.count(Municipalities.region_name.distinct())).scalar()
    )


# nombre total de scores par region
def get_total_scores_by_region(db: Session):
    return (
        db.query(Municipalities.region_name, func.sum(Airport.score).label('total_score'))
        .join(Airport)
        .group_by(Municipalities.region_name)
        .all()
    )

### nombre total de score par region trier par ordre décroissant
def get_total_scores_by_region(db: Session):
    return (
        db.query(Municipalities.region_name, func.sum(Airport.score).label('total_score'))
        .join(Airport)
        .group_by(Municipalitieq.region_name)
        .order_by(func.sum(Airport.score).desc())
        .all()
    )

## nombre total d'airoports
def get_total_airports_count(db: Session):
    return (
        db.query(func.count(Airport.id)).scalar()
    )       