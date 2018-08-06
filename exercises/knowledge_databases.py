from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(wiki_name,topic,rating):
	article=Knowledge(wiki_name=wiki_name,topic=topic,rating=rating)
	session.add(article)
	session.commit()

def query_all_articles():
	a=session.query(Knowledge).all()
	return a

def query_article_by_topic(topic):
	a=session.query(Knowledge).filter_by(topic=topic)
	return a

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

add_article("Warframe","Jeff",10)
#print(query_all_articles())
print(query_article_by_topic("Jeff"))