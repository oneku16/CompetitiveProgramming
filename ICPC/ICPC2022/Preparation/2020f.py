# Bismillah
from sys import stdin, stdout
# import threading
# import queue
# from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

# str_stdin = lambda: stdin.readline()[:-1]
# strs_stdin = lambda: list(map(str, stdin.readline().split()))
# int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: map(int, stdin.readline().split())
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



def main():

	a,b,c=sorted(ints_stdin(),reverse=True)
	ans=[0]*4

	ans[0] = sum([
		(min(a,b)>=3)*(a-2)*(b-2), 
		(min(a,c)>=3)*(a-2)*(c-2), 
		(min(c,b)>=3)*(c-2)*(b-2) 
		])*2
	
	ans[1] = sum([
		(a>=5)*(a-4)*2,
		(b>=5)*(b-4)*2,
		(c>=5)*(c-4)*2
		])*2
	
	ans[2] = sum([
		(a>=4)*4,
		(b>=4)*4,
		(c>=4)*4,
		])*2

	ans[3] = sum([
		(a==3)*2,
		(b==3)*2,
		(c==3)*2
		])*2
	
	output(ans)
if __name__ == "__main__": main()