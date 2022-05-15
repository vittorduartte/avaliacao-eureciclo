from ..extensions.database import myDatabase
from ..models.upload import Base as UploadBase
from ..models.sale import Base as SaleBase


def create_tables():
    Conn = myDatabase.get_engine()

    if not Conn.dialect.has_table(Conn.connect(), 'upload') or not Conn.dialect.has_table(Conn.connect(), 'sale'):
        try:
            UploadBase.metadata.create_all(bind=Conn)
            SaleBase.metadata.create_all(bind=Conn)
            print("\nCreated tables successfully!\n")
        except Exception as e:
            raise e

    else:
        pass
