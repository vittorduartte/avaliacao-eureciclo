from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import HTTPException
from fastapi import Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ..controllers import sale
from ..utils import files
from ..extensions.database import myDatabase
from sqlalchemy.orm import Session


def init(app):
    router = APIRouter(
        tags=["Vendas"]
    )

    templates = Jinja2Templates(directory="app/templates")

    @router.post('/vendas/', response_class=HTMLResponse)
    async def create_sales(request: Request, db: Session = Depends(myDatabase.get_session), file_upload: UploadFile = None):
        try:
            content_file = await file_upload.read()
            sale_data = files.scrapper(content_file)
            sale.register(db, sale_data["class"])
            return templates.TemplateResponse("preview.html", {"request": request, "sales": sale_data["dict"], "total": sale_data["total"]})

        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=e.__str__()
            )

    app.include_router(router)
