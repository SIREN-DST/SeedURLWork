from ttp import ttp
from ttp import utils
import json

p = ttp.Parser()
f=open('tweets-all.json')
f1=open("twitterurls2","w")


i=0
for line in f:
	#if i<3764*2:
	#	continue
	try:
		tweet = json.loads(line)["text"]
	except:
		continue
	if tweet.startswith("RT") or tweet.startswith("rt"):
		continue 
	try:
		result=p.parse(tweet)
	except:
		continue
	for url in result.urls:
		tweet=tweet.replace(url,"")
	try:
		url=utils.follow_shortlinks(result.urls)
	except:
		continue

	for key in url:
		try:
			i+=1
			f1.write(url[key][-1]+"|||"+tweet)
			print url,i
		except:
			pass






