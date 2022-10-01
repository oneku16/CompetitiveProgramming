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

def main():

	nP = int_stdin()
	numsP= sorted(int_list_stdin())

	nC = int_stdin()
	numsC = sorted(int_list_stdin())

	d = int_stdin()
	iP=0
	iC=0
	cnt=0
	while iP < nP and iC < nC:
		if numsC[iC]-d >= numsP[iP] and numsP[iP] <= numsC[iC]+d:
			iP+=1
			iC+=1
			cnt+=1
			continue
	
		if numsC[iC]+d<numsP[iP] or numsP[iP]>numsC[iC]-d:
			iC+=1
		else:
			iP+=1
	return cnt




if __name__ == "__main__": output(main())