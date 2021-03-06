
from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

engine = create_engine('sqlite:///students.db', poolclass=NullPool)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_event(event_name, event_topic, event_location , event_description , age_limit, event_time , event_adress, event_date):

	event_object = Event(
		event_name=event_name,
		event_topic=event_topic,
		event_location=event_location,
		event_description = event_description, 
		age_limit = age_limit,
		event_adress = event_adress,
		event_date =event_date,
		event_time=event_time)
	print(event_object)
	session.add(event_object)
	session.commit()

def event_query_by_location(event_location):

	events = session.query(Event).filter_by(event_location=event_location).all()
	return events

def event_query_by_topic(event_topic):

	events = session.query(Event).filter_by(event_topic=event_topic).all()
	return events

def query_all():

	events = session.query(Event).all()
	return events

def delete_event(event_name):
	
	session.query(Event).filter_by(event_name=event_name).delete()
	session.commit()

def event_query_by_topiclocation(event_topic, event_location):

	events = session.query(Event).filter_by(event_topic=event_topic, event_location = event_location).all()
	return events

def query_event_by_topic(event_topic):

	events = session.query(Event).filter_by(event_topic=event_topic).all()
	print (events)
	return events
