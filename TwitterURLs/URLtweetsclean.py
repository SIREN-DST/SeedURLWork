from ttp import ttp
from ttp import utils
import json
from numpy.random import choice
import re

p = ttp.Parser()
f=open('tweets-all.json')
f1=open("tweetscleaned","w")

level1=["Physical","Hardware", "Operations Control", "Management","Network","Application", "Access","Endpoint","Cloud Computing","Cyber","Attacks"]

level2=[["Desk Information Security", "Access Information Security",
     "Fire Extinguisher Information Security", "Emergency Information Security", "Lightning resister Information Security", 
     "Lock Information Security", "Power Information Security", "Location Information Security", "Surveillance Information Security",
     "Monitor Information Security", "Heating Ventillation Airconditioning Information Security", 
     "Alarm Information Security", "Floor Information Security", "Ceiling Information Security", "Rack Information Security"],
    
    ["Server Security", "Storage Security"],
    
    ["Alert Information Security", "Monitor Information Security", "Asset Information Security", "Incident Information Security"],
    
    ["Policy Information Security", "People Information Security",
     "Standard Information Security", "Procedure Information Security", "Governance Information Security",
    "Contract Information Security", "Law Information Security", "Intellectual Property Rights Information Security",
    "Metrics Information Security", "Testing Information Security", "Certificate Information Security",
     "Compliance Information Security", "Regulation Information Security", "Business Continuity Information Security"],

    ["Firewall ", "Network Time Protocol Security","Virtual Private Network ", "VPN", "Open Systems Interconnect Security", "Topology Security",
    "Throughput Security", "Bandwidth Security", "Local Area Network Security", "LAN Security", 
    "Wide Area Network Security", "WAN Security", "Virtual Local Area Network Security", 
    "Demilitarized zone  Network Security", "Domain Name System Security", "Internet Protocol V4 Security",
    "Internet Protocol V6 Security", "IP Security", "IPV4 Security", "IPV6 Security", "Wireless Security",
    "Internet Security", "Switch Network Security", "Router Network Security", "Multiplexer Network Security"],

    ["Operating System Security", "Data Security", "Web Security", "Code Application Security", "Web Application Firewall", "Middle Tier Security"],
    
    ["Account Security", "Authorization Security", "Authentication Security", "Cryptography"],

    ["Computer Information Security", "Desktop Information Security",
         "Laptop Information Security", "Thin Client Information Security", "Mobile Device Security",
        "Projector Information Security", "Printer Information Security", "Keyboard Information Security",
        "Mouse Information Security", "USB Information Security", "Anti-virus"],

    ["IaaS Security", "PaaS Security", "SaaS Security","Virtualization  Security", "Virtual Private Cloud", "VPC  Security "],

    ["Crime Cyber", "Cyber Squatter", "Cyber Security", "Social Engineering Cyber", "Safety Cyber"],
    
    ["deceptive software", "Injection Information",
         "Tampering Information", "Repudiation Security", "Information disclosure", "hacking", "hactivism",
        "adware", "spyware", "trojan Security", "zombie Security", "denial of service", "DOS attack", 
        "Distributed Denial of Service", "DDOS attack", "Cross site scripting", "XSS", "Cross Site Request Forgery",
        "CSRF", "Buffer overflow", "sniffer Information Security", "spam", "spoofing", "Groupware", "Phishing",
         "Smishing", "Vishing", "ransomware", "malware", "botnet"]]
i=0

elements = [0,1]
probabilities = [0.2, 0.8]    


for line in f:
    try:
    	tweet = json.loads(line)["text"]
    except:
    	continue
    randomElement = choice(elements, p=probabilities)
    if randomElement==1:
        continue

    if tweet.startswith("RT") or tweet.startswith("rt"):
    	continue 
    try:
    	result=p.parse(tweet)
    except:
    	continue
    for url in result.urls:
        tweet=tweet.replace(url,"")

    for ch in "{},();./\&@#*:?><|!":
        tweet=tweet.replace(ch,' ')
    tweet=''.join(x for x in tweet if (x.isalpha() or x==' '))
    pattern = re.compile(r"\s+")
    tweet = re.sub(pattern, " ", tweet)
    tweet=tweet.strip('\n ')  
    try:
    	url=utils.follow_shortlinks(result.urls)
    except:
    	continue

    for key in url:
    	try:
            i+=1
            print i
            f1.write(url[key][-1]+","+tweet)
    	except:
    		pass
