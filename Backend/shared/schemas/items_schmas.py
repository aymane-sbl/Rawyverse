from pydantic import BaseModel


class BaseItemsSchemas(BaseModel):
    title: str

class PublicItemsSchemas(BaseItemsSchemas):
    pass

class AdminItemsSchemas(BaseItemsSchemas):
    pass