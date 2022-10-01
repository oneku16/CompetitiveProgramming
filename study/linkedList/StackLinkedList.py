class StackLinkedList:

	#non pub class that stores linked node
	class _Node:
		__slots__='_item','_next'
		def __init__(self,item,next=None):
			self._item=item
			self._next=next

	#decorator
	def __init__(self):
		self._head=None
		self._size=0

	#returns the length of linkedStack
	def __len__(self)->int:
		return self._size

	#returns True if linkedStack is empty
	def isEmpty(self)->bool:
		return not self._size

	def addItem(self,item)->None:
		self._head = self._Node(item=item, next=self._head)
		self._size+=1

	#returns item at the top of the linkedStack
	def topItem(self):
		if self.isEmpty():
			raise Empty('Stack is empty')
		return self._head._item

	#removes and returns item at the top of the linkedStack
	def popItem(self):
		if self.isEmpty():
			raise Empty('Stack is empty')
		localItem=self._head._item
		self._head=self._head.next
		self._size-=1
		return localItem









