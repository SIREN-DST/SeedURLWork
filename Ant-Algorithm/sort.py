ips=open("PhysicalIPnormal","r").read()[1:-1].split(",")
for i in range(len(ips)):
	ips[i]=ips[i].strip("' ")
	ips[i] = "%3s.%3s.%3s.%3s" % tuple(ips[i].split("."))
ips.sort()
for i in range(len(ips)):
	ips[i] = ips[i].replace(" ", "")

f2=open("PhysicalIPsorted","w")
f2.write(str(ips))
print ips
print len(ips)
