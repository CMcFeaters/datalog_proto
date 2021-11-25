
'''
Proof of concept file that takes a connection to a database, performs a basic query, and outputs a csv file of that query. 
Currently users are reuqired to hard code the query method in python.
'''

#import the tables, etc of our file
import time
import csv
from test_python_interface_alch import Fan, Motor, Bearing, Datalog, Session
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker


#basic connection
session=Session

#test the query and timestamp
print("testing query")
t0=time.time()

#basic query eery 10000 roews
res=session.query(Fan).filter(Fan.EID%10000==0)
print("finished query")
t1=time.time()

#convert query resutl to list
thou=res.all()	#the list
num=len(thou)	#the length
print("converted to list")
t2=time.time()

#displey feh first 5 for quick sanity check
print("First 5:")
for i in range (0,5):
	print(thou[i])


#begin writing the file to csv, uses python csv writer
with open('test_csv.csv', mode='w', newline='') as TFile:
	#setup the file for writing
	TWriter=csv.writer(TFile,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	
	#write the headers
	TWriter.writerow(res[1].headers())
	
	#write teh data
	for i in range(0,num):
		TWriter.writerow(thou[i].csv())

print("Finished Write")
t3=time.time()

#output the times
print("Total Time: %.2f"%(t3-t0))
print("Query Time: %.2f"%(t1-t0))
print("Convr Time: %.2f"%(t2-t1))
print("Write Time: %.2f"%(t3-t2))

	
