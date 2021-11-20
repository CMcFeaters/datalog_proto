'''
	This generates the SCHEMA for the DB and initiates the session
	See file "datalog_schema.sql" for details.
	
'''

import mariadb
import sys
import sqlalchemy as sa #(only n00bs and wizards write sql queries)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os
from dotenv import load_dotenv

#load our basic environment variables
load_dotenv()
print(os.getenv("uname"),os.getenv("pw"))

#basic connection to a server
engine=sa.create_engine("mariadb+mariadbconnector://%s:%s@127.0.0.1:3307/datalogdb2"%(os.getenv("uname"),os.getenv("pw")))


#declare teh tables 
Base=declarative_base()

#primary table with all the relationships, this is actually probably not that importatnt
class Datalog(Base):
	__tablename__='datalog'
	CID=sa.Column(sa.Integer,primary_key=True,autoincrement=True)
	fans=relationship('Fan', back_populates='datalog')
	motors=relationship('Motor', back_populates='datalog')
	bearings=relationship('Bearing', back_populates='datalog')

#A generic class linked to the datalog.  1 datalog can have many fans.
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
	
	#a funciton to help with headers in a csv file
	def headers(self):
		return(['EID','fanName','timestamp','value0','value1','value2','value3','value4','datalog_id'])
	
	#csv_output format
	def csv(self):
		return([self.EID,self.fanName,self.ts,self.value0, 
			self.value1, self.value2, self.value3, self.value4, self.datalog_id])
		
	#what i do if i'm printed
	def __str__(self):
		s="| %s | %s | %s | %s | %s | %s | %s | %s | %s |"%(self.EID,self.fanName,self.ts,self.value0, 
			self.value1, self.value2, self.value3, self.value4, self.datalog_id)
		return s


#A generic class linked to the datalog.  1 datalog can have many motors.
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
	
	#a funciton to help with headers in a csv file
	def headers(self):
		return(['EID','motorName','timestamp','value0','value1','value2','value3','value4','datalog_id'])
	
	#csv_output format
	def csv(self):
		return([self.EID,self.motorName,self.ts,self.value0, 
			self.value1, self.value2, self.value3, self.value4, self.datalog_id])
		
	#what i do if i'm printed
	def __str__(self):
		s="| %s | %s | %s | %s | %s | %s | %s | %s | %s |"%(self.EID,self.motorName,self.ts,self.value0, 
			self.value1, self.value2, self.value3, self.value4, self.datalog_id)
		return s


#A generic class linked to the datalog.  1 datalog can have many Bearings.
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
	
	#a funciton to help with headers in a csv file
	def headers(self):
		return(['EID','bearingName','timestamp','value0','value1','value2','value3','value4','datalog_id'])
	
	#csv_output format
	def csv(self):
		return([self.EID,self.bearingName,self.ts,self.value0, 
			self.value1, self.value2, self.value3, self.value4, self.datalog_id])
		
	#what i do if i'm printed
	def __str__(self):
		s="%s | %s | %s | %s | %s | %s | %s | %s | %s |"%(self.EID,self.bearingName,self.ts,self.value0, 
			self.value1, self.value2, self.value3, self.value4, self.datalog_id)
		return s

#create the tables (if not already there, conditional by default)
Base.metadata.create_all(engine)

#create a session that can be used by anyone calling this file
Session = sa.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()


