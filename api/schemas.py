from pydantic import BaseModel
from typing import List, Optional, Tuple

class AirportBase(BaseModel):
    id: int
    type: str
    municipality: Optional[str] = None
    score: Optional[float] = None
    last_updated: Optional[int] = None

    class Config:
        orm_mode = True

class RegionBase(BaseModel):
    region_name: str

    class Config:
        orm_mode = True



class municipalityBase(BaseModel):
    municipality: str
    region_name: str 
    elevation_ft: Optional[int] = None
    latitude_deg: float 
    longitude_deg:float
    class Config:
        orm_mode = True

class AirportFilter(BaseModel):
    type: Optional[str] = None
    municipality: Optional[str] = None
    score: Optional[int] = None
    last_updated: Optional[int] = None

    class Config:
        orm_mode = True

class top5Elevation(BaseModel):
    municipality: municipalityBase
    Airport: AirportBase
    class Config:
        orm_mode = True



class RegionList(BaseModel):
    regions: List[RegionBase] 
    class Config:
        orm_mode = True

class AirportTypeCount(BaseModel):  
    type: str
    count: int

    class Config:
        orm_mode = True

class AirportTypeCountList(BaseModel):
    airport_types: List[AirportTypeCount] 

    class Config:
        orm_mode = True

class AirportCountByRegion(BaseModel):
    region_name: str
    airport_count: int

    class Config:
        orm_mode = True

class AirportCountByRegionList(BaseModel):
    airport_counts: List[AirportCountByRegion] 

    class Config:
        orm_mode = True

class MunicipalityByRegion(BaseModel):
    region_name: str
    municipality: str

    class Config:
        orm_mode = True

class AirportScoreByMunicipality(BaseModel):
    municipality: str
    latitude_deg: Optional[float] = None
    longitude_deg: Optional[float] = None
    score:float

    class Config:
        orm_mode = True

class AirportScoreByMunicipalityList(BaseModel):
    scores: List[AirportScoreByMunicipality] 

    class Config:
        orm_mode = True

class TotalScoreByRegion(BaseModel):
    region_name: str
    total_score: float

    class Config:
        orm_mode = True

class TotalScoreByRegionList(BaseModel):
    total_scores: List[TotalScoreByRegion] 

    class Config:
        orm_mode = True

class DistinctRegionCount(BaseModel):
    count: int

    class Config:
        orm_mode = True     

class DistinctRegionCountList(BaseModel):
    distinct_regions: List[DistinctRegionCount] 

    class Config:
        orm_mode = True 



class AirportCountByTypeAndRegion(BaseModel):
    type: str
    region_name: str
    airport_count: int

    class Config:
        orm_mode = True

class AirportCountByTypeAndRegionList(BaseModel):
    airport_counts: List[AirportCountByTypeAndRegion] 

    class Config:
        orm_mode = True

    
class municipalityLatling(BaseModel):
    municipality: str
    latitude_deg: float
    longitude_deg: float
    score: Optional[float] = None

    class Config:
        orm_mode = True

class RegionScore(BaseModel):
    municipality: str
    total_score: float

    class Config:
        orm_mode = True

class airoportCountByType(BaseModel):
    type: str
    airport_count: int

    class Config:
        orm_mode = True
        
class analysisResult(BaseModel):
    total_airports: int
    total_municipalities: int
    total_regions: int

    class Config:
        orm_mode = True