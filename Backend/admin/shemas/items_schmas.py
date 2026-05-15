from pydantic import BaseModel


class ItemsSchmas(BaseModel):
    title: str
    id: int