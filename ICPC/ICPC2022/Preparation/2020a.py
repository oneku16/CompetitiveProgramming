# Bismillah
from sys import stdin, stdout
# import threading
# import queue
# from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

str_stdin = lambda: stdin.readline()[:-1]
# strs_stdin = lambda: list(map(str, stdin.readline().split()))
# int_stdin = lambda: int(stdin.readline())
# ints_stdin = lambda: map(int, stdin.readline().split())
# int_list_stdin = lambda: list(map(int, stdin.readline().split()))

def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): 
			stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: 
		stdout.write(f"{val}\n")


def solve(): 

	# n = int_stdin()
	# nums = int_list_stdin()
	# a, b = ints_stdin()
	# s = str_stdin()
	# s_list = strs_stdin() 
	pass 


class Solution:
	
	def __init__(self, word):  

		self.word=word
		self.size=len(word)
		self.box=['A','P','Q']
		self.ans=''
		self.found=True

	def isValid(self):
		return False if 'A' not in self.word else True


	def baseCase(self):
		if self.word.count('Q')==n:
			return True, 'A'*(n)


	def plusOne(self):
		for i, val in enumerate(self.word):
			if i==0:
				pass
			if self.box.index(val)+1<=2:
				self.word[i]= self.box[self.box.index(val)+1]
				break
			else:
				self.word[i]='A'


	def addA(self):
		self.word=self.word[::-1]
		if not self.isValid():
			print(''.join(self.word))
			self.word[0]='A'
			print(''.join(self.word))
			if self.word[0]=='P':
				self.word[1]=='Q'
			elif self.word[0]=='Q':
				self.word[1]==''
			for i in range(self.size-1):
			 	if self.word[i]=='P':
			 		self.word[i]='Q'
			 		break
			 	if self.word[i]=='Q':
			 		print(word[i])
			 		if self.size != i:
			 			pass 
			 		else: 
			 			self.word[i]=='Q'

			# self.word[0]='A'
			# if self.size==1:
			# 	self.word=['A']

			# elif self.size==2:
			# 	self.word=['Q','A']
			# else:
			# 	for i, val in enumerate(self.word[1:]):
			# 		if val=='P':
			# 			word[i+1]=''


					 

	
	def getAns(self):
		temp=self.word[::-1]
		return ''.join(temp) 

word=list(str_stdin())[::-1]
print()
solution=Solution(word=word)
solution.plusOne()
solution.addA()
print()
print(solution.getAns())

 # def main():



# if __name__ == "__main__": output(main())