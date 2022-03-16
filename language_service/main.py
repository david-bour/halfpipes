import os
from typing import Optional
from fastapi import FastAPI
from datetime import datetime
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def metadata_service():
    """ Returns metadata """
    return {
        'Metadata': {
            'version': os.environ.get('VERSION', ''),
            'environment': os.environ.get('ENVIRONMENT', ''),
            'region': os.environ.get('REGION', ''),
            'time': datetime.now()
        }
    }

@app.get("/")
def read_root():
    return metadata_service()