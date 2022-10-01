###############################
#        author: oneku        #
# created at 12/09/2022 17:27 #
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

	s = str_stdin()
	sCounter=Counter(s)
	steps=0
	for k,v in sCounter.items(): 
		if v>=2 and not v%2:
			sCounter[k]=0
	print(sCounter)


def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()

