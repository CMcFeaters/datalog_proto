'''
	remembering how to use sqlalchemy
'''

import mariadb
import random
import sys
import sqlalchemy #(only n00bs and wizards write sql queries)
from sqlalchemy.ext.declarative import declarative_base
import datetime


#basic connection to a server
engine=sqlalchemy.create_engine("mariadb+mariadbconnector://USCGuser:USCG123@127.0.0.1:3307/datalogdb2")


#declare teh tables 

Base=declarative_base()
class DataEntry(Base):
	__tablename__='data'
	EID=sqlalchemy.Column(sqlalchemy.Integer,primary_key=True,autoincrement=True)
	#ts=sqlalchemy.Column(sqlalchemy.DateTime)
	value0=sqlalchemy.Column(sqlalchemy.Float)


Base.metadata.create_all(engine)

#start a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()

#query data
log=Session.query(DataEntry).all()

for thing in log:
	print(thing.value0)