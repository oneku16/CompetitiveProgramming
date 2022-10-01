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
	n,k=ints_stdin()
	a=int_list_stdin()

	output((sum([max([a[i + k * j] for j in range(n // k + 1) if i + k * j < n]) for i in range(k)])))
	







	# pass 


def main():

	# n = int_stdin()
	# nums = int_list_stdin()
	# a, b = ints_stdin()
	# s = str_stdin()
	# s_list = strs_stdin() 
	for _ in range(int_stdin()): solve()
	# pass 

if __name__ == "__main__": main()

	# s = str_stdin()
	# s_list = strs_stdin() 
	# ans=0
	# for i in range(n-k):
	# 	if nums[i] > nums[i+k]:
	# 		nums[i],nums[i+k]= nums[i+k], nums[i]
	# output(f'{nums=}')
	# for i in range(n-k+[0,1][n%2+k%2==2]):
	# 	ans=max(ans,sum(nums[i:k+i]))
	# 	# ans+=nums[a-1-i]