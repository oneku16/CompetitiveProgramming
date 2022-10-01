###############################
#        author: oneku        #
# created at 12/09/2022 17:25 #
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
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(): 
	a,b,c = ints_stdin()
	t1=abs(a-1)
	t2=abs(b-c)
	t3=abs(c-1)+t2
	if t1 == t3:
		output(3)
	else:
		if a>t3:
			output(2)
		else:output(1)

	# t=[abs(a-1),abs(b-c),abs(c-1)+abs(b-c)]
	# output(t.index(min(t))+1)

def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()