from Queue import Queue
q=Queue()
n=input("Enter The Memory Size:\n")
Pages=[int(i) for i in raw_input("Give a List Of Pages\n" ).split()]
#print Pages
pf=0
for i in Pages:
	#q.printList() 
	if not q.isPresent(i):
		if q.size()==n:
			k=q.dequeue()
			print "Page \'"+str(k)+"\' is poped out"		
		q.enqueue(i)
		pf+=1
	if q.isPresent(i):
		temp=q.remove(i)
		q.enqueue(i)
print "No. of Page Faults :"+str(pf)



