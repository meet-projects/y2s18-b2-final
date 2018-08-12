from model import Base, Event

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_event(event_name, event_topic, event_location , event_description , age_limit):

	event_object = Event(
		event_name=event_name,
		event_topic=event_topic,
		event_location=event_location,
		event_description = event_description, 
		age_limit = int(age_limit))
	session.add(event_object)
	session.commit()

def event_query_by_location(event_location):

	event = session.query(events).filter_by(event_location=event_location).first()
	return event

def event_query_by_topic(event_topic):

	event = session.query(events).filter_by(event_topic=event_topic).first()
	return event

def query_all():

	event = session.query(events).all()
	return event

def delete_event(event_name):
	
	session.query(events).filter_by(event_name=event_name).delete()
	session.commit()

def event_query_by_topiclocation(event_topic, event_location , age_limit , user_age):

	event = session.query(events).filter(event_topic=event_topic, event_location = event_location , age_limit < user_age).first()
	return event










