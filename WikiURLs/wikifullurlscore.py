import wikipedia
import extraction
import requests
from urllib import urlopen
import socket
import urlparse
from ttp import utils
import re
from bs4 import BeautifulSoup, SoupStrainer

level1=["Cloud Computing"]

index=0
for l1 in level1:
	f1=open("WikiURLsRank"+l1,"r")
	f2=open("WikiURLsFullRank"+l1,"w")
	f3=open("WikiSubURLs"+l1,"w")
	while 1:
		line=f1.readline().strip()
		if line=='':
			break
		line+=f1.readline().strip()
		url=line.split(",")[0]
		sublevel=line.split(",")[1]
		if url[-3:]=='pdf':
			continue
		try:
			html = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'}).text
		except:
			continue
		try:
			parsed_uri = urlparse(url)
			domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
		except:
			domain='++++++'
		indom=0
		outdom=0
		suburls=[]
		soup=BeautifulSoup(html)
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
		f3.write(sublevel+'\n'+url+'\n'+str(set(suburls))+'\n')
	f1.close()
	f2.close()
	f3.close()


