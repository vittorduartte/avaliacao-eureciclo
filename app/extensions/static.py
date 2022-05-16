from fastapi.staticfiles import StaticFiles


def init(app):

    app.mount("/static", StaticFiles(directory="app/static"), name="static")
