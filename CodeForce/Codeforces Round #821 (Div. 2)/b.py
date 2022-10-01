###############################
#        author: oneku        #
# created at 18/09/2022 20:46 #
###############################

# Bismillah
from sys import stdin, stdout
# import threading
# import queue
# from collections import Counter
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
		for elem in range(length): 
			stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: 
		stdout.write(f"{val}\n")


def solve(): 

	# n = int_stdin()
	# nums = int_list_stdin()
	n,x,y = ints_stdin()
	nums=[0]*n

	for i in range(1, n+1):
		nums[i-1]=i
	i=0
	f=[0]*(n-1)
	s=0
	while s<x:
		for j in range(x):
			f[i]=(max(nums[i],nums[i+1]))
			i+=1

		s+=1
	# while y:
	# 	f[i]=(max(nums[i],nums[i+1]))
	# 	y-=1
	# 	i+=1
	print(f)
	result=[]


	# if x != 0 and y != 0:
	# 	result = [-1]
	# elif x == 0 and y == 0:
	# 	result = [-1]
	# else:
	# 	if (n - 1) % (x + y) != 0:
	# 		result = [-1]
	# 	else:
	# 		result = [((i // (x + y)) + 1) * (x + y) for i in range(n - 1)]
	# output(result)



def main():

	# n = int_stdin()
	# nums = int_list_stdin()
	# a, b = ints_stdin()
	# s = str_stdin()
	# s_list = strs_stdin() 
	for _ in range(int_stdin()): solve()
	# pass 

if __name__ == "__main__": main()