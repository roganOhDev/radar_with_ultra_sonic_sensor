import uuid

from sqlalchemy import Column, String, Text, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from const.database_config import engine

Base = declarative_base()
Base.metadata.create_all(bind=engine)


class Capture(Base):
    __tablename__ = "capture"

    id = Column(INTEGER, primary_key=True, autoincrement= "auto")
    data = Column(Text, nullable=False)
    created_at = Column(INTEGER, nullable=False)

    def __init__(self, data, created_at):
        self.data = data
        self.created_at = created_at


