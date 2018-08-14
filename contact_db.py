from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_massege(massege_name , massege_description):

	event_object = Event(
		massege_name=massege_name,
		massege_description = massege_description)
	print(event_object)
	session.add(event_object)
	session.commit()