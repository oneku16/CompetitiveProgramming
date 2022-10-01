from random import randint


class LinkedListGenerator:

	class Node:
		# __slots__='item','next','prev'
		def __init__(self,item=None,next=None,prev=None):
		
			self.item=item
			self.next=next
			self.prev=prev

	#decorator
	def __init__(self):
		
		self.head=None
		self.size=0

	def addItem(self,newItem)->None:
		
		newNode=self.Node(item=newItem)
		newNode.next=self.head
		newNode.prev=None
		
		if self.head is not None:
			self.head.prev=newNode
		self.head = self.Node
		
		self.size+=1


def getLinkedList(n:int=8, randomMode=True):

	node=LinkedListGenerator()
	for i in range(n):
		node.addItem(newItem=[i+1,randint(10,99)][randomMode is True])

	return node.head