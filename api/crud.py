from sqlalchemy.orm import Session
from models import Data
from schemas import CountrySchema
from psycopg2.extensions import register_adapter, AsIs

#Reading data from db using query
def get_by_country(db: Session, country: str):
    ans = db.query(Data).filter(Data.country == country.country).first()
    return ans

#Get all matching country names by string
def get_by_name(db: Session, country: str):
    ans = db.query(Data).filter(Data.country.like(country.country+'%'))
    return list(ans)

#Creating data in db using query
def create_by_country(db: Session, data: CountrySchema):
    _country = Data(country=data.country, iso_code=data.iso_code, geom =data.geom)
    db.add(_country)
    db.commit()
    db.refresh(_country)
    return _country

#Removing data in db using query
def remove_by_country(db: Session, country_name: str):
    _country = db.query(Data).filter(Data.country == country_name).first()
    db.delete(_country)
    db.commit()

#Updating data in db using query
def update_by_country(db: Session, data: CountrySchema):
    _country = get_by_country(db, data)
    _country.iso_code = data.iso_code
    _country.geom = data.geom

    db.commit()
    db.refresh(_country)
    return _country