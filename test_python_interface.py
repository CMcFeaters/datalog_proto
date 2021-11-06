'''
	test file jsut to get familiar with the python interface with mariadb
'''

import mariadb
import sys

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

cur.execute("DESCRIBE data")

#rsults stored in cur, let's see what's there
for thing in cur:
	print(thing)


cur.execute(
	"INSERT INTO data (EID,value0) VALUES (?,?)",
	(1,7.75))
	
cur.execute(
	"SELECT EID, value0 FROM data",
	)
	
for (eid,value) in cur:
	print(eid,value)
	
	
