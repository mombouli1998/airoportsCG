from sqlalchemy import Column, Integer, String, Float, ForeignKey, REAL
from sqlalchemy.orm import relationship
from database import Base

class Airport(Base):    
    __tablename__ = 'airports'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    name = Column(String)
    municipality = Column(String, ForeignKey('municipalities.municipality'))
    score = Column(Integer)
    last_updated = Column(Integer)

    municipalities_rel = relationship("Municipalities", back_populates="airports")


class Municipalities(Base):
    __tablename__ = 'municipalities'
    
    municipality = Column(String, primary_key=True)
    region_name = Column(String, nullable=False)
    latitude_deg = Column(REAL, nullable=True)
    longitude_deg = Column(REAL, nullable=True)
    elevation_ft = Column(Integer)
    airports = relationship("Airport", back_populates="municipalities_rel")
