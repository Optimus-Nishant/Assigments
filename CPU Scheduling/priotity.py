def sortList(n):
	global processList
	for i in range(1,n):
		key = processList[i][2] 
		temp= processList[i]
		#print temp, key
		j=i-1
		while j>=0 and processList[j][2] > key:
			processList[j+1]=processList[j]
			j-=1
		processList[j+1]=temp

def calwaiting(n):
	global processList
	#print processList
	wait=[0]*(n)
	for i in range(1,n):
		#if processList[i][0]<processList[i-1][1]:
		wait[i]=processList[i-1][1]-processList[i][0]+wait[i-1]
	print wait
	return float(sum(wait))/n

n= int(raw_input("Enter The Number Of Processes"))
processList=[]
print "Enter The Arrival Time Burst Time and Priority Of Job"
for _ in range(n):
	x=[int(i) for i in raw_input().split()]
	processList.append(tuple(x))
sortList(n)
#print processList
print "Average Waiting Time: "+str(calwaiting(n))


		
		
	 
