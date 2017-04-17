from tabulate import tabulate
level1=["Physical","Hardware", "Operations Control", "Management","Network","Application", "Access","Endpoint","Cloud Computing","Cyber","Attacks"]

print "twitter"
head=["subdom","links","domain duplic","page sz","partMETAmatch","indom","outdom"]

data=[]
for level in level1:
	f=open("TwitterURLScore"+level,"r")
	partmetamatch=0.0
	indom=0
	outdom=0
	lines=0
	pagesz=0
	dom=set()
	for line in f:
		l=line.split(",")
		#print line
		#print l[-8],l[-7],l[-2],l[-1]
		partmetamatch+=float(l[-7])
		indom+=int(l[-2])
		outdom+=int(l[-1])
		pagesz+=float(l[-4])
		dom.add(l[-5])
		lines+=1

	#print partmatch,fullmatch,indom,outdom,lines
	if lines!=0:
		data.append([level,lines,lines,str(pagesz/lines),str(partmetamatch/lines),str((indom*1.0)/lines),str((outdom*1.0)/lines)])
	else:
		data.append([level,lines,lines,0,0,0,0,0,0,0])
	#if lines!=0:
	#	print str((outdom*1.0)/lines)+','+level
	f.close()

print tabulate(data,headers=head)


