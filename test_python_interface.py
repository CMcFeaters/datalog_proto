'''
	test file jsut to get familiar with the python interface with mariadb
'''

import mariadb
import random
import sys
import sqlalchemy #(only n00bs and wizards write sql queries)
from sqlalchemy.ext.declarative import declarative_base


#basic connection to a server
try:
	conn = mariadb.connect(
		user="USCGuser",
		password="USCG123",
		host="127.0.0.1",
		port=3307,
		database="datalogdb2"
	)
	print("success!")
except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("show tables")

#rsults stored in cur, let's see what's there
for thing in cur:
	print(thing)

try:
	for i in range(0,100):
		cur.execute(
			"INSERT INTO data (value0) VALUES (%s)"%
			(random.random()*100))
except mariadb.Error as e:
	print(f"Error: {e}")
		

cur.execute(
	"SELECT EID, value0 FROM data",
	)
	
for (eid,value) in cur:
	print(eid,value)

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
conn.close()
	
