###############################
#        author: oneku        #
# created at 22/09/2022 17:58 #
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
# strs_stdin = lambda: list(map(str, stdin.readline().split()))
int_stdin = lambda: int(stdin.readline())
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

	n = int_stdin()
	# nums=list(range(1,n+1))
	# print(nums)
	s=str_stdin()
	cnt=0
	used=[0]*n
	for i, v in enumerate(s):
		if v == '0':
			print(i+1)
			# stop=i
			for j in range(i,n):
				if not used[j] and not (j+1)%(i+1):
					cnt+=i+1
					used[j]=1
					print(f'{cnt=} {j+1}')
		else:
			used[i]=1

	# nums = int_list_stdin()
	# a, b = ints_stdin()
	# s = str_stdin()
	# s_list = strs_stdin() 
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