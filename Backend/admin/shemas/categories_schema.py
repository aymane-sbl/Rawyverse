from pydantic import BaseModel,Field
class CategoriesSchema(BaseModel):
    category_name : str = Field(alias="CategoryName")