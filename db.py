import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Post(Base):
	__tablename__ = 'posts'
	
	# Define Columns
	id = Column(Integer, primary_key=True)
	title = Column(String(250), nullable=False)
	post  = Column(Text, nullable=False)
	comments = Column(Text, nullable=False)
	link = Column(String(250), nullable=False)

engine = create_engine('sqlite:///praw.db')

Base.metadata.create_all(engine)
