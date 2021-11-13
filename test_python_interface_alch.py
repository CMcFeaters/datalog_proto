'''
	remembering how to use sqlalchemy
'''

import mariadb
import random
import sys
import sqlalchemy as sa #(only n00bs and wizards write sql queries)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
import os
from dotenv import load_dotenv

#load our basic environment variables
load_dotenv()
print(os.getenv("uname"),os.getenv("pw"))

#basic connection to a server

engine=sa.create_engine("mariadb+mariadbconnector://%s:%s@127.0.0.1:3307/datalogdb2"%(os.getenv("uname"),os.getenv("pw")))


#declare teh tables 

Base=declarative_base()

#primary database with all the relationships, this is actually probably not that importatnt
class Datalog(Base):
	__tablename__='datalog'
	CID=sa.Column(sa.Integer,primary_key=True,autoincrement=True)
	fans=relationship('Fan', back_populates='datalog')
	motors=relationship('Motor', back_populates='datalog')
	bearings=relationship('Bearing', back_populates='datalog')

#the next 3 items are a bunchof generic classes just to fill the table and slightly look like 
#we have a datalogger db
class Fan(Base):
	__tablename__='fans'
	EID=sa.Column(sa.Integer,primary_key=True,autoincrement=True)
	fanName=sa.Column(sa.String(length=20))
	ts=sa.Column(sa.DateTime)
	value0=sa.Column(sa.Float)
	value1=sa.Column(sa.Float)
	value2=sa.Column(sa.Float)
	value3=sa.Column(sa.Float)
	value4=sa.Column(sa.Float)
	datalog_id=sa.Column(sa.Integer,sa.ForeignKey('datalog.CID'))
	datalog=relationship("Datalog",back_populates="fans")
	
	#what do i do if i'm called
	def __repr__(self):
		return("I'm a fan!")
		
	#what i do if i'm printed
	def __str__(self):
		s="| %s | %s | %s | %s | %s | %s | %s | %s | %s |"%(self.EID,self.fanName,self.ts,self.value0, 
			self.value1, self.value2, self.value3, self.value4, self.datalog_id)
		return s


class Motor(Base):
	__tablename__='motors'
	EID=sa.Column(sa.Integer,primary_key=True,autoincrement=True)
	motorName=sa.Column(sa.String(length=20))
	ts=sa.Column(sa.DateTime)
	value0=sa.Column(sa.Float)
	value1=sa.Column(sa.Float)
	value2=sa.Column(sa.Float)
	value3=sa.Column(sa.Float)
	value4=sa.Column(sa.Float)
	datalog_id=sa.Column(sa.Integer,sa.ForeignKey('datalog.CID'))
	datalog=relationship("Datalog",back_populates="motors")
	
class Bearing(Base):
	__tablename__='bearings'
	EID=sa.Column(sa.Integer,primary_key=True,autoincrement=True)
	bearingName=sa.Column(sa.String(length=20))
	ts=sa.Column(sa.DateTime)
	value0=sa.Column(sa.Float)
	value1=sa.Column(sa.Float)
	value2=sa.Column(sa.Float)
	value3=sa.Column(sa.Float)
	value4=sa.Column(sa.Float)
	datalog_id=sa.Column(sa.Integer,sa.ForeignKey('datalog.CID'))
	datalog=relationship("Datalog",back_populates="bearings")

fan_names=["exhaust1","supply1","exhaust2","supply2"]
motor_names=["pump1","pump2","pump3","pump4"]
bearing_names=["SSDG1","SSDG2","MDE1","THRUST1"]

Base.metadata.create_all(engine)

#start a session
Session = sa.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()


'''def addEntry():
	#simple add entry option
	newEntry=DataEntry(ts=datetime.datetime.now(),value0=random.random()*100)
	Session.add(newEntry)
	
for i in range(0,100):
	addEntry()
'''

#newDatalog=Datalog()
#Session.add(newDatalog)

#create a bunch of random garbage for our tables
if __name__=="__main__":

	
	for j in range (0,800):
		for i in range(0,100000):
			newFan=Fan(ts=datetime.datetime.now(),
			fanName=fan_names[random.randrange(4)],
			value0=random.random()*100,
			value1=random.random()*100,
			value2=random.random()*100,
			value3=random.random()*100,
			value4=random.random()*100,
			datalog_id=1)
			
			newMotor=Motor(ts=datetime.datetime.now(),
			motorName=motor_names[random.randrange(4)],
			value0=random.random()*100,
			value1=random.random()*100,
			value2=random.random()*100,
			value3=random.random()*100,
			value4=random.random()*100,
			datalog_id=1)
			
			newBearing=Bearing(ts=datetime.datetime.now(),
			bearingName=bearing_names[random.randrange(4)],
			value0=random.random()*100,
			value1=random.random()*100,
			value2=random.random()*100,
			value3=random.random()*100,
			value4=random.random()*100,
			datalog_id=1)

			Session.add(newFan)
			Session.add(newMotor)
			Session.add(newBearing)

		Session.commit()


#query data
#log=Session.query(Datalog).all()

'''
for thing in log:
	print(thing.EID, thing.ts, thing.value0)
'''