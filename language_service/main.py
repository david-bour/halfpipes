import os
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

def metadata_service():
    return {
        'Metadata': {
            'version': os.environ.get('VERSION', ''),
            'environment': os.environ.get('ENVIRONMENT', ''),
        }
    }

@app.get("/")
def read_root():
    return metadata_service()