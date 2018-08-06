from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__='students'
	student_id=Column(Integer, primary_key=True)
	wiki_name=Column(String)
	topic=Column(String)
	rating=Column(Integer)
	

	pass