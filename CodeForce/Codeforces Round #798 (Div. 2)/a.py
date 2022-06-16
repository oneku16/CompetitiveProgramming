###############################
#        author: oneku        #
#  created: 10/06/2022 22:00  #
###############################


from sys import stdin, stdout
# import threading
# import queue
from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline().split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))
ints_map = lambda: map(int, stdin.readline().split())


def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(): 

	n, m, k = ints_map()
	s1 = [[key, val] for key, val in Counter(str_stdin()).items()]
	s2 = [[key, val] for key, val in Counter(str_stdin()).items()]	
	# s1_c = Counter(s1)
	# s2_c = Counter(s2)
	# s1 = [[key, val] for key, val in Counter(str_stdin()).items()]
	# print(s1_c.keys(), s2_c.keys())
	print(s1, s2)
	i1 = 0
	i2 = 0
	ans = ""
	rem = 0
	while n > 0 or m > 0:

		if s1[i1][0] == s2[i2][0]:
			loc_n = s1[i1][1] + s2[i2][1]
			rem = loc_n % k
			ans += s1[i1][0] * (loc_n - rem)
		
		elif ord(s1[i1][0]) > ord(s2[i2][0]):
			loc_n = s1[i1][1]



def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()