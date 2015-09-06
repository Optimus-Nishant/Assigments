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

	def isPresent(self, key):
		#print key in self.items
		return key in self.items

	def remove(self,key):
		k=self.items.remove(key)
		return k


	def printList(self):
		print ''.join(str(i) for i in self.items)
