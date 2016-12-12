f=open('NIST.IR.7298r2.txt')
g=open('terms','w')
i=0
for line in f:
	k=''
	s=line.decode('utf-8').strip()
	if i==0:
		c=s[-1]
		print c
	i+=1
	for j in line:
		try:
			k+=j.encode('utf-8')
		except:
			if s[-1]==c:
				g.write(k)
				g.write('\n')
				break