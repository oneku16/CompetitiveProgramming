# from sys import stdin, stdout

# class Node:
# 	__slots__='item','next','prev'
# 	def __init__(self,item=None,next=None,prev=None):
# 		self.item=item
# 		self.next=next
# 		self.prev=prev


# class LinkedList(Node):
# 	# __slots__='head','size'
# 	def __init__(self):
# 		super().__init__()
# 		self.head=None
# 		self.size=0

# 	def addItem(self,newItem):
# 		newNode=Node()
# 		newNode.item=newItem
# 		newNode.next=self.head
# 		newNode.prev=None
# 		if self.head is not None:
# 			self.head.prev=newNode
# 		self.head=newNode
# 		self.size+=1

# class Solution:
# 	def solve(self,n=10):
# 		linkedList=LinkedList()
# 		while n:
# 			print(f'{n=}')
# 			linkedList.addItem(newItem=n)
# 			n-=1
# 		node=linkedList
# 		while node:
# 			stdout.write(f'{node.item}->')
# 			node=node.next
# 		# stdout.write(f'\n{linkedList.prev.item}')
# Solution().solve()










from random import randint
from time import time

def randomNumber()->int:
	temp=int(str(time()+0.00001)[-randint(1,len(str(time())))])

	# upperBound=float('inf')
	return randint(0, randint(1,9)**temp**2)

print(randomNumber())




