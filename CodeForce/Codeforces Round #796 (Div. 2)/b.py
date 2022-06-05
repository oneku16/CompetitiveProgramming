###############################
#        author: oneku        #
#  created: 03/06/2022 17:31  #
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

	n = int_stdin()
	nums = sorted(ints_stdin())

	odd = 0
	even = 0
	cnt = 0
	evenlist = []

	for i in range(n):
		if nums[i] % 2: odd += 1
		else:
			even += 1
			evenlist.append(i)
	if not even: output(0)
	elif odd == even: output(even)
	elif odd > even: output(even)
	# elif n == 1 and even == 1:
	# 	while: pass 
	elif odd < even: 
		cnt = odd
		if even > 1: even -= odd + 1
		else:
			cnt -= 1 
			even - odd
		summ = 0
		# output(even)
		for i in range(even):

			summ += nums[evenlist[i]]
			cnt += 1
		# output(summ)
		while not summ % 2:
			cnt += 1
			summ /= 2
		output(cnt)



def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()