f=open("tempfile.txt","w")
for i in range (0,500):
	f.write("value"+str(i)+" FLOAT,\n")
	
f.close()