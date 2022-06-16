###############################
#       author: Elnazar       #
#  created: 07/06/2022 01:23  #
###############################


from sys import stdin, stdout
# import threading
# import queue
from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools


str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline()[-1].split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(leftside, rightside) -> str:

	def calc(collection: list, counter: dict) -> float:
	
		for key, val in counter.items():
			if key == '/':
				for i in range(val):
					ind = collection.index(key)
					collection[ind] = float(collection[ind - 1]) / float(collection[ind + 1])
					collection.pop(ind - 1)
					collection.pop(ind)
			if key == '*':
				for i in range(val):
					ind = collection.index(key)
					collection[ind] = float(collection[ind - 1]) * float(collection[ind + 1])
					collection.pop(ind - 1)
					collection.pop(ind)
			if key == '+':
				for i in range(val):
					ind = collection.index(key)
					collection[ind] = float(collection[ind - 1]) + float(collection[ind + 1])
					collection.pop(ind - 1)
					collection.pop(ind)
			if key == '-':
				for i in range(val):
					ind = collection.index(key)
					collection[ind] = float(collection[ind - 1]) - float(collection[ind + 1])
					collection.pop(ind - 1)
					collection.pop(ind)
		# output(collection[0])
		return collection[0]
	# leftside = ["".join()]
	counter_right_sign = Counter(sorted([elem for elem in rightside if not elem.isnumeric()]))
	counter_left_sign = Counter(sorted([elem for elem in leftside if not elem.isnumeric()]))
	return "YES" if calc(leftside, counter_left_sign) == calc(rightside, counter_right_sign) else "NO"


def main():

	l, r = str_stdin().split('=')
	left = []
	right = []
	var = ""
	for i in range(len(l)):
		if l[i].isnumeric(): 
			var += l[i]
			if i == len(l) -1: left.append(var)
		else: 
			left.append(var)
			left.append(l[i])
			var = ""
	var = ""
	for i in range(len(r)):
		if r[i].isnumeric(): 
			var += r[i]
			if i == len(r) - 1: right.append(var)		
		else: 
			right.append(var)
			right.append(r[i])
			var = ""
	output(solve(leftside = left, rightside = right))
	 

if __name__ == "__main__": main()