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
	
	def __repr__(self):
		if self.rating<7:
			return "Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!."
		return("If you want to learn about {},"
		" you should look at the Wikipedia article called {}."
		" We gave this article a rating of {} out of 10!"
		"ID:{}").format(self.topic,self.wiki_name,self.rating,self.student_id)

	
x=Knowledge(student_id=44,wiki_name="rainbow",topic="weather",rating=9)
print(x)