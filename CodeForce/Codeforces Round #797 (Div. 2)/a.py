###############################
#        author: oneku        #
#  created: 07/06/2022 15:25  #
###############################


from sys import stdin, stdout
# import threading
# import queue
# from collections import Counter
from math import ceil, floor
# import heapq
# import itertools

str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline().split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(): 

	n = int_stdin()

	a, b, c = int(n/3), int(n/3), int(n/3)
	b += n - sum([a, b, c])

	if b - 1 > a and a == c:
		a += 1
		c -= 1
	elif b - 1 == a and a == c:
		b+=1
		c -= 1
	if a == b and a == c:
		b += 1
		c -= 1
	output(f"{a} {b} {c}")

def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()