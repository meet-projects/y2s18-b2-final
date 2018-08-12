from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_student(username, user_password, user_mail):

	user_object = User(
		username=username,
		user_password=user_password,
		user_mail=user_mail)
	session.add(user_object)
	session.commit()

def query_by_name(name):

	user = session.query(Users).filter_by(username=username).first()
	return student

def query_all():

	user = session.query(Users).all()
	return user

def delete_user(user_mail):
	
	session.query(User).filter_by(user_mail=user_mail).delete()
	session.commit()

