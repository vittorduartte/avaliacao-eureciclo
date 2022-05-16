from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

def init(app):
    router = APIRouter(
        tags=["Index"]
    )

    templates = Jinja2Templates(directory="app/templates")

    @router.get("/", response_class=HTMLResponse)
    async def index(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    app.include_router(router)

    return app