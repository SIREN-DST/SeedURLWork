import ping, socket
import sys
x=(int)(sys.argv[1])
ips=open("PhysicalIPsorted","r").read()[1:-1].split(",")
f=open("PhysicalIPsortedtimes"+str(x),"w")
total=0
for i in range(len(ips)):
	ips[i]=ips[i].strip("' ")
	print ((int)(ips[i].split(".")[0]))/10,ips[i]
	if(((int)(ips[i].split(".")[0]))/10!=x):
		continue
	print ips[i]

	try:
		delay = ping.Ping(ips[i], timeout=4000).do()
		f.write(ips[i]+" "+str(delay)+"\n")
		total+=delay
		print delay
	except socket.error, e:

		f.write(ips[i]+" "+"Ping Error:"+str(e)+"\n")
		print "#####################Ping Error:",e
		pass
	except TypeError:
		f.write(ips[i]+" "+"timeout"+"\n")
print total

