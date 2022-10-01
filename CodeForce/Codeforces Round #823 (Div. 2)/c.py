###############################
#        author: oneku        #
# created at 25/09/2022 20:14 #
###############################

# Bismillah
from sys import stdin, stdout
# import threading
# import queue
from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

str_stdin = lambda: stdin.readline()[:-1] 
strs_stdin = lambda: list(map(str, stdin.readline().split())) 
int_stdin = lambda: int(stdin.readline()) 
ints_stdin = lambda: map(int, stdin.readline().split()) 
int_list_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(): 

	s=str_stdin()
	used=[]
	ans=''
	sC=[i for i in Counter(sorted(list(str_stdin()),reverse=False)).keys()] 
	used.append(0)
	for i in range()


	# s = Counter(sorted(list(str_stdin()),reverse=True))
	# mins=[i for i in s.keys()]
	# print(mins)
	# ans=''
	# l=len(mins)-1
	# curr=''
	# cnt=0
	# for key, val in s.items():
	# 	cnt+=1
	# 	if not len(ans):
	# 		# l+=1
	# 		ans+=key*val
	# 		curr=key
	# 	else:
	# 		if key!=mins[l]:
	# 			# if curr > f'{min(int(key)+1,9)}':
	# 			ans+=f'{min(int(key)+1,9)}'*val
	# 			print(f'{key=}')

	# 		else:
	# 			print(mins[l])
	# 			ans+=key*val
	# 			l-=1
	# # s
	# print(cnt)
	# print(ans[::-1])
	# if s[-1]!=9:
	# 	for i in range(n):
	# 		nums[i]=(9-int(i))
	
	# for i in range(n-1):


	
	# 0 4 8 2 9
	# 0 4 2 9 9
	# 0 2 5 9 9


def main():

	# n = int_stdin() #ex: 1
	# nums = int_list_stdin() #ex: 1 2 3 4 5 ...
	# a, b = ints_stdin() #ex: 1 2
	# s = str_stdin() #ex: 'name'
	# s_list = strs_stdin() #ex: 'a', 'name', 'blahblah'
	for _ in range(int_stdin()): solve()

if __name__ == "__main__": main()