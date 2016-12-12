import wikipedia
level1=["Application", "Access", "Operations Control", "Management", "Endpoint","Cloud Computing","Cyber","Attacks"]
level2=[
["Operating System", "Data", "Web", "Code", "Web Application Firewall", "Middle Tier"],
["Account", "Authorization", "Authentication", "Cryptography"],
["Alert", "Monitor", "Asset Management", "Incident"],
["Policy", "People", "Standard", "Procedure", "Governance", "Contract", "Law", "Intellectual Property Rights", "Metrics", "Testing", "Certificate", "Compliance", "Regulation", "Business Continuity"],
["Computer", "Desktop", "Laptop", "Thin Client", "Mobile Device", "Projector", "Printer", "Keyboard", "Mouse", "USB", "Anti-virus"],
["Infrastructure as a Service", "Platform as a Service", "Software as a Service", "Virtualization", "Virtual Private Cloud"],
["Squatter", "Crime", "Security", "Social Engineering", "Safety"],
["deceptive software", "Injection", "Tampering", "Repudiation", "Information disclosure", "hacking", "hactivism", "adware", "spyware", "trojan", "zombie", "denial of service", "Distributed Denial of Service", "Cross site scripting", "Cross Site Request Forgery", "Buffer overflow", "sniffer", "spam", "spoofing", "Groupware", "Phishing", "Smishing", "Vishing", "ransomware", "malware", "botnet"],
]
index=0
for l1 in level1:
	f=open("WikiLevel2Terms"+l1,"w")
	visited={}
	for i in level2[index]:
		f.write(i+"\n")
		term=set()
		for j in wikipedia.search(i+" security"):
			if j in visited:
				continue
			else:
				visited[j]=1
			try:
				term=term.union(wikipedia.page(j).links)
			except:
				pass
		print term
		for j in wikipedia.search("Information Security "+i):
			if j in visited:
				continue
			else:
				visited[j]=1
			try:
				term=term.union(wikipedia.page(j).links)
			except:
				pass
		print term
		for j in wikipedia.search("Information "+i+" security"):
			if j in visited:
				continue
			else:
				visited[j]=1
			try:
				term=term.union(wikipedia.page(j).links)
			except:
				pass
		visited.clear()
		print term
		f.write(str(term)+"\n")
	f.close()
	index+=1


