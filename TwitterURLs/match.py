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

f=open("tweetcleaned","r")
count=0
for i in level1:
	with open(i+"tweet","w") as f2:
		f2.write('')
for line in f:
	print line
	try:
		tweet=line.split(",")[1]
		url=line.split(",")[0]
	except IndexError:
		continue
	count+=1
	for i in range(len(level2)):
		k=0
		for j in range(len(level2[i])):
			phrase=level2[i][j].lower().split(" ")
			fl=1
			for word in phrase:
				if word not in tweet and word not in url:
					fl=0
					break
			if fl==1:
				with open(level1[i]+"tweet","a") as f2:
					f2.write(line.strip('\n ')+','+level2[i][j]+'\n')
				k=1
		if k==1:
			break
print count





