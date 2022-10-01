###############################
#       author: Elnazar       #
#  created: 28/06/2022 01:27  #
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

	n, m = map(int, stdin.readline().split())
	nums = ints_stdin()

	return (f"{sum(nums) % m}")


def main():
	for i in range(int_stdin()): output(f"Case #{i + 1}: {solve()}")


if __name__ == "__main__": main()