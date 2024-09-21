from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    main_category: str
    sub_category: str
    contents: str
    source_site: str


class News(NewsBase):
    id: int

    class Config:
        orm_mode = True


class RawContent(BaseModel):
    contents: str
    source_site: str