class Node:
	def __init__(self,data:any,next=None):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def reverse(self):
		prev=None
		current=self.head
		while current is not None:
			next=current.next
			current.next=prev
			prev=current
			current=next
		self.head=prev

	def addVal(self,val):
		newNode=Node(data=val)
		newNode.next=self.head
		self.head=newNode

	def getList(self):
		current=self.head
		while current:
			print(f'{current.data}',end=[' ','\n'][current.next is None])
			current=current.next

linkedList=LinkedList()
for i in range(5,0,-1):
	linkedList.addVal(i)
# print(linkedList.head.data)
linkedList.getList()
linkedList.reverse()
# print(linkedList.head.next.data)
# linkedList.getList()