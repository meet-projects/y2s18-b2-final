
from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(user_name, user_age , user_location):

	user_object = User(
		user_name = user_name,
		user_age = user_age,
		user_location = user_location)
	session.add(user_object)
	session.commit()
	return user_object

def query_user(user_name):
	user = session.query(User).filter_by(user_name=user_name).first()
	return user













