from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel
from geoalchemy2 import Geometry
from pydantic.dataclasses import dataclass
from pydantic import ConfigDict


T = TypeVar('T')

#Schema for data
class CountrySchema(BaseModel):
    country: Optional[str] = None
    geom: Optional[Geometry] = None
    iso_code: Optional[str] = None

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestCountry(BaseModel):
    parameter: CountrySchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]