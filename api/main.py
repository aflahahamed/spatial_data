from fastapi import FastAPI
import models
from routes import router
from config import engine

models.Base.metadata.create_all(bind=engine)

#Initializing the app
app = FastAPI()

app.include_router(router, prefix="/country", tags=["country"])