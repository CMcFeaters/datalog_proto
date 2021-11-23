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
thou=res.all()

print("finished query")
t1=time.time()


print("First 5:")
for i in range (0,5):
	print(thou[i])

print(type(thou))
print(type(thou[i]))
num=len(thou)
print("Begin writing")
t2=time.time()

with open('test_csv.csv', mode='w', newline='') as TFile:
	#setup the file for writing
	TWriter=csv.writer(TFile,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
	
	#write the headers
	TWriter.writerow(res[1].headers())
	
	#write teh data

	for i in range(0,num):
		TWriter.writerow(thou[i].csv())
'''

	TWriter.writerows(
		[
		[thou[i].EID,thou[i].fanName,thou[i].ts,thou[i].value0, 
			thou[i].value1, thou[i].value2, thou[i].value3, thou[i].value4, thou[i].datalog_id] for i in range(0,100)]
		)

	

	TWriter.writerows(
		[thou[i].csv() for i in range(0,500)])
'''
print("Finished Write")
t3=time.time()

print("Total Time: %.2f"%(t3-t0))
print("Query Time: %.2f"%(t1-t0))
print("Write Time: %.2f"%(t3-t2))

# simple function to create a vector from the query result and return for writing
def vectorizer(result):
	res_vector=[]
	
