from urllib import response
from fastapi import FastAPI
from .resources import index as index_routes

def create_app():
    app = FastAPI()

    index_routes.init(app)

    return app