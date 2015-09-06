#Question:- Given a list of Processes , the CPU Burst and arrival time. Display and Print Grantt Chart
def sortList(A,n,k):
	for i in range(1,n):
		key = A[i][k] 
		temp= A[i]
		print temp, key
		j=i-1
		while j>=0 and A[j][k] > key:
			A[j+1]=A[j]
			j-=1
		A[j+1]=temp
	return A

def createsjf(t):
	global sjf
	for job in processList:
		if job[0]<=t and job not in sjf:
			sjf.append(job)
	sjf=sortList(sjf,len(sjf),1)


def calwaiting(n):
	global sjf,processlist
	t=sjf[0][1]
	createsjf(t)
	wait=0	
	for i in range(1,n):
		if sjf[i][0]<sjf[i-1][1]:
			wait+=sjf[i-1][1]-sjf[i][0]
	print wait
	return float(wait)//n

processList=[]
n=input("Enter No. Of Processes: ")
for _ in range(n):
	print "Enter Arrival Time Followed By Burst Time:"
	x=[int(i) for i in raw_input().split()]
	processList.append(tuple(x))
processList= sortList(processList,n,0)
sjf=[processList[0]]
print sjf
print calwaiting(n)

 
