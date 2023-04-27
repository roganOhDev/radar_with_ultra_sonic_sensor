from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from const.config import db_name

engine = create_engine("sqlite+pysqlite:///./" + db_name, echo=True, future=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


def get_db():
    db = db_session
    try:
        yield db
    finally:
        db.close()
