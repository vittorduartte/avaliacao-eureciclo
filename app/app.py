from urllib import response
from fastapi import FastAPI
from .resources import index as index_routes
from .resources import sale as sale_routes
from .utils import database

def create_app():
    database.create_tables()
    
    app = FastAPI()
    
    index_routes.init(app)
    sale_routes.init(app)

    return app