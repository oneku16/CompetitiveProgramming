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

def main():
	a=[[i for i in range(5)] for j in range(5)]
	# n = (int_stdin()%8)
	# # return ( (pow(3, int_stdin()%8) + 1)//2)%8

	# ans=[( (3**i + 1)//2)%8 for i in range(1,5)]
	# return ans[n%4-1]
	return a[0,0]

if __name__ == "__main__": output(main())

# 72 67 41 49 