from distutils.command.upload import upload
from sqlalchemy.orm import Session
from ..models.upload import Upload


def register(db: Session, filename: str):
    try:
        upload_in = Upload(file_name=filename)
        db.add(upload_in)
        db.commit()
        db.refresh(upload_in)
        return {"data": upload_in.id, "status": "success", "message": "Upload created successfully"}

    except Exception as e:
        db.rollback()
        raise e


def delete(db: Session, upload_id: str):
    try:
        db.query(Upload).filter(Upload.id == upload_id).delete()
        db.commit()
        return {"data": True, "status": "success", "message": "Upload deleted successfully!"}

    except Exception as e:
        db.rollback()
        raise e
