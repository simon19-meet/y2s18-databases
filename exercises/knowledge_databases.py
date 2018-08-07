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

def query_article_by_rating(threshold):
	a=session.query(Knowledge).filter(Knowledge.rating<threshold).all()
	return a

def query_article_by_primary_key(id):
	a=session.query(Knowledge).filter_by(student_id=id).all()
	return a

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()


def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(updated_rating,article_title):
	art_rate=session.query(Knowledge).filter_by(wiki_name=article_title).first()
	art_rate.rating=updated_rating
	session.commit()

def delete_article_by_rating(threshold):
	session.query(Knowledge).filter(Knowledge.rating<threshold).delete()
	session.commit()

def get_top_rated_5():
	a=session.query(Knowledge).order_by(Knowledge.rating).limit(5)
	return a

add_article("Warframe","Yo",4)
#delete_all_articles()

#print(query_article_by_topic("Jeff"))

#print(query_article_by_rating(10))
#print(query_article_by_primary_key(6))
#delete_article_by_topic("Games")
#edit_article_rating(5,"Warframe")
#print(query_article_by_topic("Gay"))
#delete_article_by_rating(9)
print(get_top_rated_5())
#print(query_all_articles())
