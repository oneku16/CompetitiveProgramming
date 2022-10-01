###############################
#        author: oneku        #
#  created: 08/09/2022 20:35  #
###############################

# Bismi Allah
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

	n = int_stdin()
	nums1 = int_list_stdin()
	nums2 = int_list_stdin()
	
	if n==1:return 2
	else:
		if Counter(nums2)==Counter(nums1): return 0
		else:
			


def main():
	for _ in range(int_stdin()): output(solve())


if __name__ == "__main__": main()