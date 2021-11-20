#import the tables, etc of our file
import timing
import csv
from test_python_interface_alch import Fan, Motor, Bearing, Datalog, Session
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

#basic connection
session=Session

#simple query
print('testing query')

#timestamp
timing.log("finished counting")

#basic query eery 1000 roews
thou=session.query(Fan).filter(Fan.EID%1000==0)

timing.log("finished query")


print("First 5:")
for i in range (0,5):
	print(thou[i])


#creating CSV
with open('test_csv.csv', mode='w', newline='') as TFile:
	#setup the file for writing
	TWriter=csv.writer(TFile,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	
	#write the headers
	TWriter.writerow(thou[1].headers())
	
	#write teh data
	for i in range(0,100):
		TWriter.writerow(thou[i].csv())
