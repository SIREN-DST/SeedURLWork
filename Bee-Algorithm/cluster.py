ips=open("PhysicalIPsorted","r").read()[1:-1].split(",")
i=0
total=0
k=1
for i in range(len(ips)):
	baseip=ips[i].strip("' ")
	ips[i]=ips[i].strip("' ")
	new=tuple(ips[i].split("."))
	if i!=0:
		diff=0
		for i in range(4):
			diff=diff*1000+(int)(prev[i].strip("' "))-(int)(new[i].strip("' "))
		print diff
		total+=diff
		if diff<-3470000000:
			k+=1
	f=open("PhysicalIPs"+str(k)),"a")
	baseip=baseip.replace("\s+","")
	f.write(baseip+"\n")
	f.close()
	prev=tuple(ips[i].split("."))
	i=i+1

print "avg diff=",total/(len(ips)-1)
print k

