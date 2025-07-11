from fastapi import FastAPI, HTTPException, Depends, Path
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import List, Optional
import schemas
import query_helper as helpers

## initialisation de l'application FastAPI
app = FastAPI(
    title="Airoport API",
    description="API for managing and querying airoport CG   data",
    version="1.0.0",
    contact={
        "name": "Trinité",
        "email": "trinitemombouli@gmail.com"
    }
)

# dependance pour obtenir la session de la base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
## endpoint pour tester la connexion à l'API
@app.get("/", 
summary="Test de l'API",
description="Vérifie que l'api fonctionne correctement",
response_description="API est fonctionnelle",
operation_id="root_endpoint",
tags=["Root"])

def read_root():
    return {"message": "Bienvenue dans l'API des aéroports CG"}

## endpoint pour obtenir tous les aéroports
@app.get(
"/airoports",
summary="Obtenir tous les aéroports",
description="Récupère la liste de tous les aéroports",
response_model=List[schemas.AirportBase],
operation_id="get_all_airports",
tags=["Airports"])

def get_airports(db: Session = Depends(get_db)):
    airports = helpers.get_airports(db)
    return airports

## endpoint pour obtenir la liste des municipalités
@app.get(
"/municipalities",
summary="Obtenir la liste des municipalités",
description="Récupère la liste de toutes les municipalités",
response_model=List[schemas.municipalityBase],
operation_id="get_all_municipalities",
tags=["Municipalities"])

def get__municipalities(db: Session = Depends(get_db)):
    municipalities = helpers.get_municipalities(db)
    return municipalities

## endpoint pour obtenir les airoports avec filtre
@app.get(
"/airoports/filter",
summary="Obtenir les aéroports avec filtre",
description="Récupère la liste des aéroports avec des options de filtrage",
response_model=List[schemas.AirportFilter],
operation_id="get_filtered_airports",
tags=["Airports"])
def get_filtered_airports(
    type: Optional[str] = None,
    municipality: Optional[str] = None,
    score: Optional[int] = None,
    last_updated: Optional[int] = None,
    db: Session = Depends(get_db)
):
    airports = helpers.get_filtre_airports(db, type,municipality, score,last_updated)
    if not airports:
        raise HTTPException(status_code=404, detail="Aucun aéroport trouvé avec les critères spécifiés")
    return airports



# ## endpoint pour obtenir les aéroports par type
@app.get(
"/airoports/type/{type}",
summary="Obtenir les aéroports par type",
description="Récupère la liste des aéroports filtrés par type",
response_model=List[schemas.AirportBase],
operation_id="get_airports_by_type",
tags=["Airports"])
def get_airports_by_type(
    type: str = Path(..., description="Type d'aéroport à filtrer"),
    db: Session = Depends(get_db)
):
    airports = helpers.get_types_airoprt(db, type)
    if not airports:
        raise HTTPException(status_code=404, detail="Aucun aéroport trouvé pour ce type")
    return airports

## endpoint pour obtenir les aéroports mis à jour par année
@app.get(   
"/airoports/updated/{year}",
summary="Obtenir les aéroports mis à jour par année",
description="Récupère la liste des aéroports mis à jour pour une année spécifique",
response_model=List[schemas.AirportBase],
operation_id="get_airports_by_year",
tags=["Airports"])
def get_airports_by_year(
    year: int = Path(..., description="Année de mise à jour des aéroports"),
    db: Session = Depends(get_db)
):
    airports = helpers.get_anne_airoprt(db, year)
    if not airports:
        raise HTTPException(status_code=404, detail="Aucun aéroport trouvé pour cette année")
    return airports

# ## endpoint pour obtenir les 5 aéroports avec la plus haute élévation
@app.get(
"/airoports/top5_elevation",
summary="Obtenir les 5 aéroports avec la plus haute élévation",
description="Récupère les 5 aéroports ayant la plus haute élévation",
response_model=List[schemas.top5Elevation],
operation_id="get_top5_airports_elevation",
tags=["Airports"])
def get_top5_airports_elevation(db: Session = Depends(get_db)):
    airports = helpers.get_top5_elevation(db)
    if not airports:
        raise HTTPException(status_code=404, detail="Aucun aéroport trouvé")
    return airports

# ## endpoint pour obtenir les régions
@app.get(
"/regions",
summary="Obtenir les régions",
description="Récupère la liste de toutes les régions",
response_model=List[schemas.RegionBase],
operation_id="get_all_regions",
tags=["Regions"])
def get_all_regions(db: Session = Depends(get_db)):
    regions = helpers.get_regions(db)
    if not regions:
        raise HTTPException(status_code=404, detail="Aucune région trouvée")
    return regions

# ## endpoint pour obtenir le nombre d'aéroports par région
@app.get(
"/airoports/count_by_region",
summary="Obtenir le nombre d'aéroports par région",
description="Récupère le nombre d'aéroports pour chaque région",
response_model=List[schemas.AirportCountByRegion],
operation_id="get_airports_count_by_region",
tags=["Airports"])
def get_airports_count_by_region(db: Session = Depends(get_db)):
    airport_counts = helpers.get_airports_count_by_region(db)
    if not airport_counts:
        raise HTTPException(status_code=404, detail="Aucun aéroport trouvé par région")
    return airport_counts

## endpoint pour obtenir le nombre d'aéroports par type
@app.get(
"/airoports/count_by_type",
summary="Obtenir le nombre d'aéroports par type",
description="Récupère le nombre d'aéroports pour chaque type",
response_model=List[schemas.AirportTypeCount],
operation_id="get_airports_count_by_type",
tags=["Airports"])
def get_airports_count_by_type(db: Session = Depends(get_db)):
    airport_types = helpers.get_airports_count_by_type(db)
    if not airport_types:
        raise HTTPException(status_code=404, detail="Aucun aéroport trouvé par type")
    return [schemas.AirportTypeCount(type=airport_type.type, count=airport_type.airport_count) for airport_type in airport_types]

# ## endpoint pour obtenir les municipalités par région
@app.get(
"/municipalities/by_region",
summary="Obtenir les municipalités par région", 
description="Récupère les municipalités pour chaque région",
response_model=List[schemas.MunicipalityByRegion],
operation_id="get_municipalities_by_region",
tags=["Municipalities"])
def get_municipalities_by_region(db: Session = Depends(get_db)):
    municipalities = helpers.get_municipalities_by_region(db)
    if not municipalities:
        raise HTTPException(status_code=404, detail="Aucune municipalité trouvée par région")
    return municipalities

## endpoint pour obtenir les types d'airoports par region 
@app.get(
"/airoports/types_by_region",
summary="Obtenir les types d'aéroports par région",
description="Récupère les types d'aéroports pour chaque région",
response_model=List[schemas.AirportCountByTypeAndRegion],
operation_id="get_airport_types_by_region",
tags=["Airports"])
def get_airport_types_by_region(db: Session = Depends(get_db)):
    airport_types = helpers. get_airports_count_by_type_and_region(db)
    if not airport_types:
        raise HTTPException(status_code=404, detail="Aucun type d'aéroport trouvé par région")
    return airport_types

## endpoint pour obtenir la latitude et la longitude des municipalités
@app.get(
"/municipalities/lat_long_score",
summary="Obtenir la latitude et la longitude des municipalités",    
description="Récupère la latitude, la longitude et le score des municipalités",
response_model=List[schemas.municipalityLatling],
operation_id="get_lat_long_score_by_municipality",
tags=["Municipalities"])
def get_lat_long_score_by_municipality(db: Session = Depends(get_db)):
    lat_long_scores = helpers.get_lat_long_score_by_municipality(db)
    if not lat_long_scores:
        raise HTTPException(status_code=404, detail="Aucune latitude et longitude trouvée pour les municipalités")
    return lat_long_scores

## endpoint nombre d'airoports par type     
@app.get(   
"/airoports/count_by_type",
summary="Obtenir le nombre d'aéroports par type",
description="Récupère le nombre d'aéroports pour chaque type",
response_model=List[schemas.airoportCountByType],
operation_id="get_airports_count_by_type",
tags=["Airports"])
def get_airports_count_by_type(db: Session = Depends(get_db)):
    airport_counts = helpers.get_airports_count_by_type(db)
    if not airport_counts:
        raise HTTPException(status_code=404, detail="Aucun aéroport trouvé par type")
    return airport_counts

## endpoint pour obtenir le nombre total d'aéroports et de municipalités et de régions
@app.get(
"/analysis/result",
summary="Obtenir le résultat de l'analyse",
description="Récupère le nombre total d'aéroports, de municipalités et de régions",
response_model=schemas.analysisResult,
operation_id="get_analysis_result",
tags=["Analysis"])
def get_analysis_result(db: Session = Depends(get_db)):
    total_airports = helpers.get_total_airports_count(db)
    total_municipalities = helpers.get_distinct_municipalities_count(db)
    total_regions = helpers.get_distinct_regions_count(db)

    if total_airports is None or total_municipalities is None or total_regions is None:
        raise HTTPException(status_code=404, detail="Aucune donnée trouvée pour l'analyse")

    return schemas.analysisResult(
        total_airports=total_airports,
        total_municipalities=total_municipalities,
        total_regions=total_regions
    )