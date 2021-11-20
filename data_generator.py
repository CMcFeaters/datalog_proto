'''
A file that generates a bunch of garbage for us to use in our DB
'''

import sqlalchemy as sa #(only n00bs and wizards write sql queries)
import random
import datetime
from test_python_interface_alch import Fan, Motor, Bearing, Session

#some random names to populate the garbage data
fan_names=["exhaust1","supply1","exhaust2","supply2"]
motor_names=["pump1","pump2","pump3","pump4"]
bearing_names=["SSDG1","SSDG2","MDE1","THRUST1"]


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