from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import CountrySchema, Request, Response, RequestCountry
import crud

router = APIRouter()

#Get the DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create end point
@router.post("/create")
async def create_country(request: RequestCountry, db: Session = Depends(get_db)):
    crud.create_by_country(db, data=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Country created successfully").dict(exclude_none=True)

#Reader end point
@router.get("/read")
async def get_countries(request: RequestCountry, db: Session = Depends(get_db)):
    _country = crud.get_by_country(db, country=request.parameter)
    return Response(status="Ok", 
                    code="200", 
                    message="Success fetched country data", 
                    result=[_country.country, _country.iso_code, str(_country.geom)])
    
#Get all matching country names by string
@router.get("/match")
async def match_countries(request: RequestCountry, db: Session = Depends(get_db)):
    _country = crud.get_by_name(db, country=request.parameter)
    matches=[]
    for i in _country:
        matches.append(i.country)
    return Response(status="Ok", 
                    code="200", 
                    message="Success fetched the matching countries", 
                    result=matches)

#Update end point
@router.patch("/update")
async def update_country(request: RequestCountry, db: Session = Depends(get_db)):
    _country = crud.update_by_country(db,request.parameter)
    return Response(status="Ok", 
                    code="200", 
                    message="Success updated country data", 
                    result=[_country.country, _country.iso_code, str(_country.geom)])

#delete end point
@router.delete("/delete")
async def delete_country(request: RequestCountry,  db: Session = Depends(get_db)):
    crud.remove_by_country(db, request.parameter.country)
    return Response(status="Ok", 
                    code="200", 
                    message="Success delete country data").dict(exclude_none=True)