from sqlalchemy import Column, Integer, String, Text
from .database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)


class Post(Base):
    __tablename__ = "Post"

    postNumber = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
