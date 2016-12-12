import ping, socket
import sys
x=sys.argv[1]
ips=open(x+"IPsorted","r").read()[1:-1].split(",")
f=open(x+"IPsortedtimes","w")
total=0.0
for i in range(len(ips)):
	ips[i]=ips[i].strip("' ")
	print ips[i]
	try:
		delay = ping.Ping(ips[i], timeout=4000).do()
		f.write(ips[i]+" "+str(delay)+"\n")
		total+=delay
		print delay
	except socket.error, e:
		f.write(ips[i]+" "+"Ping Error:"+e+"\n")
		print "#####################Ping Error:",e
		pass
	except TypeError:
		f.write(ips[i]+" "+"timeout"+"\n")
print total

#PhysicalIPnormal 135653.139353      count=706 avg=192.14325687366346
#PhysicalIPsorted 133323.0419159022  count=690 avg=193.22179987811913 