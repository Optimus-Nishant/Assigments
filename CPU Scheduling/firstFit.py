#QUESTION :- Write a program to perform First Fit Memory Allocation
class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)



class FirstFit:
	def __init__(self,size):
		self.Jobs= Queue()
		self.Allocated={}
		self.memory = size
		self.freeMemory=0
		
	def addJob(self, job):
		if job[1]>self.freeMemory:
			self.Jobs.enqueue(job)
		else:
			self.Allocated[job[0]]=[job[1],job[2]]
			self.freeMemory=memory-job[1]
`	
	def getStatus(self,i):
		for task in Allocated:
			for item in Allocated[task]:
				if item[2]>i:
					print "JOB"+task+"=> : "+" Memory : "+str(item[1])+" Time Remaining : "+str(item[2])
					item[2]-=1
				elif item[2]==1:
					print "JOB ENDED...!!!"
					freeMemory-=item[1]
					memory+=item[1]
				

def 

					
				
			


