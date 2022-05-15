from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import HTTPException
from fastapi import Depends

from sqlalchemy.orm import Session

from ..controllers import upload
from ..extensions.database import myDatabase


def init(app):
    router = APIRouter(
        tags=["Envios"]
    )

    @router.post("/upload", response_model=dict)
    async def enviar_arquivo(db: Session = Depends(myDatabase.get_session), upload_file: UploadFile = None):
        return {"filename": upload_file.filename}

    app.include_router(router)
