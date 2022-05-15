from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import HTTPException
from fastapi import Depends

from ..controllers import sale
from ..utils import files
from ..extensions.database import myDatabase
from sqlalchemy.orm import Session


def init(app):
    router = APIRouter(
        tags=["Vendas"]
    )

    @router.post('/vendas/', response_model=dict)
    async def create_sales(db: Session = Depends(myDatabase.get_session), file_upload: UploadFile = None):
        try:
            content_file = await file_upload.read()
            data = files.scrapper(content_file)
            sale.register(db, data["class"])
            return {"data": data["dict"]}

        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=e.__str__()
            )

    app.include_router(router)
