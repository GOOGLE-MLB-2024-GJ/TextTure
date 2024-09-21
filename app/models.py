from sqlalchemy import Column, Integer, String
from .database import Base


class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    main_category = Column(String(100), nullable=False)
    sub_category = Column(String(100), nullable=False)
    contents = Column(String(5000), nullable=False)
    source_site = Column(String(255), nullable=False)
