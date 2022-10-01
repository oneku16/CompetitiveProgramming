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
int_list_stdin = lambda: list(map(int, stdin.readline().split()))

def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): 
			stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: 
		stdout.write(f"{val}\n")


# def solve(): 

# 	# n = int_stdin()
# 	# nums = int_list_stdin()
# 	# a, b = ints_stdin()
# 	# s = str_stdin()
# 	# s_list = strs_stdin() 
# 	pass 



def main():

	n = int_stdin()
	nNums = sorted(int_list_stdin())
	m = int_stdin()
	mNums = sorted(int_list_stdin())
	d=int_stdin()
	nStep=0
	mStep=0
	cnt=0	
	# output(f'{nNums=}\n{mNums=}')
	for i in range(min(n,m)):
		if i+mStep >= min(n,m) or i+nStep >= min(n,m):
			break
		if mNums[i+mStep]-d<=nNums[i+nStep]<=mNums[i+mStep]+d:
			cnt+=1
		else:
			if mNums[i+mStep]-d<nNums[i+nStep] and mNums[i+mStep]+d<nNums[i+nStep]:
				mStep+=1
			else:
				nStep+=1
			if i+mStep < min(n,m) or i+nStep < min(n,m):
				if mNums[i+mStep]-d<=nNums[i+nStep]<=mNums[i+mStep]+d:
					cnt+=1
	
		# print(f'{nStep=}\n{mStep=}')

	output(cnt)

if __name__ == "__main__": 
	main()