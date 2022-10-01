###############################
#        author: oneku        #
#  created: 06/09/2022 20:19  #
###############################


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

	n,m=ints_stdin()
	if n==1:
		output('YES')
		return m
	if not m%n and not m==n:
		output('YES')
		return [m//n]*n
	else:
		if not n%2 and not m%2:
			output('YES')
			return [m-n]*(m-n) + [1]*(n*2-m)
		elif n%2 or m%2 or n==m:
			return 'NO'
		


def main():
	for _ in range(int_stdin()):  output(solve())


if __name__ == "__main__": main()