from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
class User(Base):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True)
	user_name = Column(String)
	user_location = Column(String)
	user_age = Column(Integer)


	

