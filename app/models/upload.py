from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import Boolean
from sqlalchemy.orm import relationship
from ..extensions.database import Base
from datetime import datetime


class Upload(Base):
    __tablename__ = "upload"

    id = Column(String(50), primary_key=True, default='upload_'+datetime.now().strftime('%Y%m%d%H%M%S'))
    file_name = Column(String(50), nullable=False)
    status = Column(Boolean, nullable=False, default=False)
    create_at = Column(Date, nullable=False, default=datetime.now().strftime('%Y-%m-%d'))

    sales = relationship("Sale", back_populates="upload", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Upload(id={self.id}, file_name={self.file_name}, status={self.status}, create_at={self.create_at})"