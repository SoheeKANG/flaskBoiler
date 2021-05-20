from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
