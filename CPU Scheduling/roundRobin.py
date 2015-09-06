def sortList(n):
	global processList
	for i in range(1,n):
		key = processList[i][0] 
		temp= processList[i]
		print temp, key
		j=i-1
		while j>=0 and processList[j][0] > key:
			processList[j+1]=processList[j]
			j-=1
		processList[j+1]=temp

def calwaiting(n):
	global processList
	wait,t,i=0,0,0
	while len(processList)>0:
		if processList[i][1] <= 0:
			wait+=(t-processList[i][0])			
			processList.pop(i)
		else:
			processList[i][1]-=2
			i=(i+1)%len(processList)
		t+=2
	print wait
	return float(wait)//n

n= int(raw_input("Enter The Number Of Processes"))
processList=[]
jobPool=[]
print "Enter The Arrival Time And Burst Time(Optimum Time):\n"
for _ in range(n):
	x=[int(i) for i in raw_input().split()]
	processList.append(x)
sortList(n)
print "Average Waiting Time: "+str(calwaiting(n))


		
		
	 
