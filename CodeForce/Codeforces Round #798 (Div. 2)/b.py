###############################
#        author: oneku        #
#  created: 10/06/2022 22:00  #
###############################


from sys import stdin, stdout
from copy import deepcopy as dc
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

	n = int_stdin()
	nums = ints_stdin()
	n_nums = dc(sorted(nums))
	# print(n_nums)
	status = True
	if n == 1: status = False
	for i in range(n):
		if not status: break
		if i == 0:
			if nums[i] == n_nums[i]: n_nums[i], n_nums[1] = n_nums[i + 1], n_nums[i]
		else: 
			if nums[i] == n_nums[i]:
				if i < n - 1:
					if n_nums[i] == n_nums[i - 1]: n_nums[i], n_nums[i + 1] = n_nums[i + 1], n_nums[i]
					if n_nums[i] == n_nums[i + 1]: n_nums[i], n_nums[i - 1] = n_nums[i - 1], n_nums[i]
					else: n_nums[i], n_nums[i - 1] = n_nums[i - 1], n_nums[i]

	if status: output(n_nums)
	else: output(-1)


def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()