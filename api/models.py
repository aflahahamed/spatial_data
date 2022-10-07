from sqlalchemy import  Column, Integer, String
from config import Base
from geoalchemy2 import Geometry

#Model Data to use for communication with postgres
class Data(Base):
    __tablename__ ="features"

    geom = Column(Geometry(geometry_type='POLYGON', management=True))
    country = Column(String,primary_key=True)
    iso_code = Column(String)
    
