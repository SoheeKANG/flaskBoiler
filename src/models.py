from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey


class User:
    __tablename__ = "User"

    id = Column(String(20), primary_key=True)
    password = Column(String(20), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)


class Post:
    __tablename__ = "Post"

    post_number = Column(Integer, primary_key=True, autoincrement=True)
    post_title = Column(Text, nullable=False)
    post_body = Column(Text, nullable=False)
    post_time = Column(TIMESTAMP)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email


class Comment:
    __tablename__ = "comment"
    post_num = Column(Integer)
    comment_num = Column(Integer, autoincrement=True)
    comment_body = Column(Text)
    comment_time = Column(TIMESTAMP)