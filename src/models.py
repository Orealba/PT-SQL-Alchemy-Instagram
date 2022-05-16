import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


    

class User(Base):
  __tablename__ = 'user'
  ID = Column(Integer, primary_key=True)
  user_name = Column(String(250), nullable=False)
  first_name = Column(String(250), nullable=False)
  last_name = Column(String(250), nullable=False)
  email = Column(String(250), nullable=False)
 
  
class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,ForeignKey("user.id"))
    user_to_id = Column(Integer,ForeignKey("user.id"))
    user = relationship ('User')


class Media(Base):
    __tablename__= 'media'
    ID = Column(Integer, primary_key=True)
    type =Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer,ForeignKey("post.id"))
    media = relationship ('Post')

class Post (Base):
  __tablename__= 'post'
  ID = Column(Integer, primary_key=True)
  user_id = Column(Integer,ForeignKey("user.id"))


class Comment (Base):
    __tablename__= 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer,ForeignKey("user.id"))
    post_id = Column(Integer,ForeignKey("post.id"))

  


# class Person(Base):
#    __tablename__ = 'person'
# Notice that each column is also a normal Python instance attribute.
# Here we define columns for the table person
# id = Column(Integer, primary_key=True)
#name = Column(String(250), nullable=False)
#last_name = Column(String(250), nullable=False)

#class Address(Base):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
  #  id = Column(Integer, primary_key=True)
 #   __tablename__ = 'address'
   # street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    #def to_dict(self):
     #   return {}

## Draw from SQLAlchemy base
try:
  result = render_er(Base, 'diagram.png')
  print("Success! Check the diagram.png file")
except Exception as e:
  print("There was a problem genering the diagram")
  raise e