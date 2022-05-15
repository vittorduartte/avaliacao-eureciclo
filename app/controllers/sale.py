from sqlalchemy.orm import Session


def register(db: Session, sale_list: list):
    try:
        db.add_all(sale_list)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
