'''
basic script to just create the 500 'valueX' columns instead of copy and pasting
like a troglodyte
'''
f=open("tempfile.txt","w")
for i in range (0,500):
	f.write("value"+str(i)+" FLOAT,\n")
	
f.close()