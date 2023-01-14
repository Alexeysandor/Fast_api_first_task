from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = create_engine("postgresql://Admin:Admin@localhost:5432/fast_api_db")
Base = declarative_base()


class SessionLocal(Session):
    def __init__(self):
        super().__init__(bind=engine)


def get_db():
    return SessionLocal()


class Menu(Base):
    __tablename__ = "Menu"
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String)
    description = Column(String)
    submenus_count = Column(Integer, default=0)
    dishes_count = Column(Integer, default=0)

    def add_submenu_count(self, value: int):
        self.submenus_count += value

    def add_dishes_count(self, value: int):
        self.dishes_count += value

    def delete_submenu_count(self, value: int):
        self.submenus_count -= value

    def delete_dishes_count(self, value: int):
        self.dishes_count -= value


class Submenu(Base):
    __tablename__ = "Submenu"
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String)
    description = Column(String)
    dishes_count = Column(Integer, default=0)
    menu_id = Column(UUID, ForeignKey(Menu.id, ondelete='CASCADE'))

    def update_dishes_count(self, value: int):
        self.dishes_count += value

    def delete_dishes_count(self, value: int):
        self.dishes_count -= value


class Dish(Base):
    __tablename__ = "Dish"
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(String)
    description = Column(String)
    price = Column(String)
    submenu_id = Column(UUID, ForeignKey(Submenu.id, ondelete='CASCADE'))
