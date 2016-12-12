from urlparse import urlparse
import socket
from ttp import ttp
from ttp import utils
import requests
f=open("WikiURLsFullRank2Network")
ips=set()
i=1
for line in f:
	print "hi"
	url=line.split(',')[0]
	print url,
	try:
		response = requests.get(url, timeout=10)
	except:
		continue
	try:
		finalurl=response.history[-1].url
		print finalurl,
	except:
		finalurl=url
	try:
		dom=urlparse(finalurl).netloc
	except:
		continue
	dom=dom.split(".")
	dom=dom[-2]+"."+dom[-1]
	print dom,
	try:
		ip=socket.gethostbyname(dom)
	except:
		continue
	print ip,i
	i+=1
	ips.add(ip)

ips=list(ips)
for i in range(len(ips)):
    ips[i] = "%3s.%3s.%3s.%3s" % tuple(ips[i].split("."))
ips.sort()
for i in range(len(ips)):
    ips[i] = ips[i].replace(" ", "")

f2=open("NetworkIPsorted","w")
f2.write(str(ips))



