from urlparse import urlparse
import socket
from ttp import ttp
from ttp import utils
import requests
f=open("WikiURLsFullRank2Physical")
ips=list()
i=1
ipurlmatch=''
for line in f:
	url=line.split(',')[0]
	print url,
	try:
		response = requests.get(url, verify=False, timeout=10)
	except:
		pass
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
	print ip+' '+url+'\n'
	ipurlmatch+=ip+' '+url+'\n'
	ips.append(ip)

known_links = set()
newlist = []

for d in ips:
	link = d
  	if link in known_links: 
  		continue
  	newlist.append(d)
  	known_links.add(link)

ips[:] = newlist

f3=open("PhysicalIPURLmatch","w")
f3.write(ipurlmatch)

