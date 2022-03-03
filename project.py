#!/usr/bin/env python

# 1. Library imports
import uvicorn ##ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}