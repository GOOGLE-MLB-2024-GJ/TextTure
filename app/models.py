from sqlalchemy import Column, Integer, String
from .database import Base


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    category = Column(String)
    contents = Column(String)
    source_site = Column(String, nullable=True)
