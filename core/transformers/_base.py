from pydantic import BaseModel


class BaseTransformer(BaseModel):
    pass


class OrmTransformer(BaseModel):
    id: int

    class Config:
        orm_mode = True
