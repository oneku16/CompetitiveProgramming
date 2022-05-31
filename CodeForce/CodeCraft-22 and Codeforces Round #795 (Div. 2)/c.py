###############################
#        author: oneku        #
#  created: 31/05/2022 02:01  #
###############################


from sys import stdin, stdout
# from collections import Counter
# from math import inf, gcd
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

	n, k = ints_stdin()
	s = (str_stdin())
	used = [False for i in range(n)]
	longest = 0
	for i in range(k): pass






def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()