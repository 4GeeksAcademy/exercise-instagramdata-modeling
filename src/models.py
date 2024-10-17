import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    __tablename__ = 'Follower'  
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id =  Column(Integer, ForeignKey('User.id'))

    user_from = relationship('User', back_populates='following')
    user_to = relationship('User', back_populates='followers')


class User(Base):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
     __tablename__ = 'User'
     id = Column(Integer, primary_key=True)
     username = Column(String(50))
     firstname = Column(String(50))
     lastname = Column(String(50))
     email = Column(String(50))

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))

class Media(Base):
    __tablename__= 'Media'
    id = Column(Integer, primary_key=True)
    type = Column (Enum)
    url = Column(String(50))
    post_id = Column(Integer, ForeignKey('Post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
