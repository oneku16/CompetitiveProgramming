###############################
#        author: oneku        #
#  created: 16/06/2022 18:58  #
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
ints_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(): 


	a, b = ints_stdin()
	ans = ""
	if a == b: output('1' * b + '0' * a)
	elif a < b:
		if a % 2: output('0' * a + '1' * b)
	else:
		if 


		

def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()