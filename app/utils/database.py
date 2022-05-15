from ..extensions.database import myDatabase
from ..models.sale import Base as SaleBase

def create_tables():
    Conn = myDatabase.get_engine()

    if not Conn.dialect.has_table(Conn.connect(), 'sale'):
        try:
            SaleBase.metadata.create_all(bind=Conn)
            print("\nCreated tables successfully!\n")
        except Exception as e:
            raise e

    else:
        pass
