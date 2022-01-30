import os
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Metadata": {
        "version": os.environ.get("VERSION", "not specified"),
        "environment": os.environ.get("ENVIRON", "not specified"),
    }}