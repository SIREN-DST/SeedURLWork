import wikipedia
level1=["Physical","Hardware", "Operations Control", "Management"]
level2=[
["Desk Information Security", "Access Information Security",
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
     "Compliance Information Security", "Regulation Information Security", "Business Continuity Information Security"]
]
index=0
for l1 in level1:
	f=open("WikiLevel2Terms"+l1,"w")
	visited={}
	for i in level2[index]:
		f.write(i+"\n")
		term=set()
		for j in wikipedia.search(i):
			if j in visited:
				continue
			else:
				visited[j]=1
			try:
				term=term.union(wikipedia.page(j).links)
			except:
				pass
		print term
		visited.clear()
		f.write(str(term)+"\n")
	f.close()
	index+=1


