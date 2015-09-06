def sortList(n):
	global processList
	for i in range(1,n):
		key = processList[i][1]-processList[i]
		temp= processList[i]
		print temp, key
		j=i-1
		while j>=0 and processList[j][0] > key:
			processList[j+1]=processList[j]
			j-=1
		processList[j+1]=temp

def calwaiting(n):
	global processList
	wait=0
	for i in range(1,n):
		if processList[i][0]<processList[i-1][1]:
			wait+=processList[i-1][1]-processList[i][0]
	print wait
	return float(wait)//n

n= int(raw_input("Enter The Number Of Processes"))
processList=[]
for _ in range(n):
	x=[int(i) for i in raw_input().split()]
	processList.append(tuple(x))
sortList(n)
print "Average Waiting Time: "+str(calwaiting(n))


		
		
	 
