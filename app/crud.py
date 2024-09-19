from sqlalchemy.orm import Session

from . import models, schemas


def get_news(db: Session, news_id: int):
    return db.query(models.News).filter(models.News.id == news_id).first()


def get_all_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.News).offset(skip).limit(limit).all()


def create_news(db: Session, news: schemas.News):
    db_news = models.News(title=news.title,
                          main_category=news.main_category,
                          sub_category=news.sub_category,
                          contents=news.contents,
                          source_site=news.source_site)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news
