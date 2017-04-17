import wikipedia
import extraction
import requests
from urllib import urlopen
import socket
import urlparse
from ttp import utils
import re
from bs4 import BeautifulSoup, SoupStrainer

f=open("dmozURLS","r")
f2=open("dmozURLsranked","w")

for line in f:
	url=line.split(",")[0]
	indom=0
	outdom=0
	suburls=[]
	try:
		html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'}).text
	except:
		continue
	soup=BeautifulSoup(html)
	try:
		parsed_uri = urlparse(url)
		domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	except:
		domain='++++++'
	for link in soup.find_all('a', href=True):
		try:
			n=urlparse.urlparse(link['href']).netloc
		except:
			continue
		if domain in link['href'] or not bool(n):
			indom+=1
		else:
			outdom+=1
		suburls.append(link['href'])
		#except:
		#	continue
	print url,indom,outdom
	f2.write(line+','+str(indom)+','+str(outdom)+'\n')