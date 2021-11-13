#import the tables, etc of our file
import timing
from test_python_interface_alch import Fan, Motor, Bearing, Datalog, Session
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

#basic connection
print("creating engine and session connection")
#engine=sa.create_engine("mariadb+mariadbconnector://USCGuser:USCG123@127.0.0.1:3307/datalogdb2")
session=Session

#simple query
print('testing query')
#total=session.query(Fan).count()
total=1
#timestamp
timing.log("finished counting")

#basic query eery 1000 roews
thou=session.query(Fan).filter(Fan.EID%1000==0)

timing.log("finished query")


print("total entries:")
print(total)
print("First 5:")
for i in range (0,5):
	print(thou[i])
	

