from pydantic import BaseModel


class MenuValidator(BaseModel):
    title: str
    description: str


class SubmenuValidar(BaseModel):
    title: str
    description: str


class DishValidator(BaseModel):
    title: str
    description: str
    price: str
