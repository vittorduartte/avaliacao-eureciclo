from urllib import response
from fastapi import FastAPI


def create_app():
    app = FastAPI()

    @app.get("/", response_model=dict)
    def index():
        return {"Message": "Hello EuReciclo"}

    return app