import os
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

def metadata_service():
    """ Returns metadata """
    return {
        'Metadata': {
            'version': os.environ.get('VERSION', ''),
            'environment': os.environ.get('ENVIRONMENT', ''),
            'region': os.environ.get('REGION', ''),
        }
    }

@app.get("/")
def read_root():
    return metadata_service()