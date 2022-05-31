###############################
#        author: oneku        #
#  created: 31/05/2022 02:01  #
###############################


from sys import stdin, stdout
from collections import Counter
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
	n_nums = ints_stdin()
	n_counter = Counter(n_nums)
	values = n_counter.values()
	values = list(values)
	
	i = 0
	ans = []
	ind = 0
	check = True
	while i < len(values):
		length = values[i]
		if length == 1:
			check = False
			break
		elif length % 2:
			local_ans = [k for k in range (ind, length + ind)][::-1]
			local_ans[-1], local_ans[values[i]//2] = local_ans[length//2], local_ans[-1]
			i+=1
			ind += length
			for j in local_ans: ans.append(j+1)
		else:
			local_ans = [k for k in range (ind, length + ind)][::-1]
			i+=1
			ind += length
			for j in local_ans: ans.append(j+1)
	output(ans) if check else output(-1)

			


def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()