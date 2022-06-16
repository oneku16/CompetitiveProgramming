###############################
#        author: oneku        #
#  created: 07/06/2022 15:25  #
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

	n = int_stdin()
	a_nums = ints_stdin()
	b_nums = ints_stdin()

	if 0 not in b_nums: output("NO")
	else:
		check = True
		diff = 0
		for i in range(n):
			if b_nums[i] or a_nums[i]: 
				diff = abs(a_nums[i] - b_nums[i])
				break
		for i in range(n):
			if b_nums[i] and a_nums[i]:
				if diff != abs(b_nums[i] - a_nums[i]):
					check = False
					break

		if check: output("YES")
		else: output("NO")
	# zezo = False
	# ans = False
	# diff = 0
	# for i in range(n):
	# 	if b_nums[i] > a_nums[i]: 
	# 		break
	# 		ans = True 
	# 	if a_nums[i] and b_nums[i]: diff = a_nums[i] - b_nums[i] 
	
	# if ans: output("NO")
	# else:
	# 	if 0 not in 
	# 	for i in range(n):
	# 		if a_nums[i]



def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()