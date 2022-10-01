###############################
#        author: oneku        #
#  created: 18/06/2022 18:20  #
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

	n, m = ints_stdin()
	matrix = [0] * n
	idn = 0
	idm = 0
	maxval = 0
	for i in range(n):
		matrix[i] = ints_stdin()
		if max(matrix[i]) > maxval: 
			maxval = max(matrix[i])
			idn = i + 1
			idm = matrix[i].index(maxval) + 1
	# h = 0
	# w = 0
	# h = max((n - idn) + 1, idn)
	# w = max((m - idm) + 1, idm)
	if n % 2 and m % 2:
		if n % 2 + 1 <= idn and m % 2 + 1 <= idm:
			output(idn * idm)
		elif n % 2 + 1 > idn and m % 2 + 1 > idm:
			output((n - idn) * (m - idm))

	# output(f"ind: {idn} {idm} hw {h} {w}")
	# output(h * w)




def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()