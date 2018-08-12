from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class Event(Base):
	__tablename__ = 'events'
	event_id = Column(Integer, primary_key=True)
	event_name = Column(String)
	event_location = Column(String)
	event_description = Column(String)
	event_topic = Column(String)


	def __repr__(self):
		return ("event Name: {}\n"
				"event event_location: {} \n"
				"event topic: {}").format(
					self.event_name,
					self.event_location,
					self.event_topic)

