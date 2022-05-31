from sys import stdin, stdout
from collections import Counter
str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline().split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))

def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")

for _ in range(int_stdin()):

	n, w = ints_stdin()
	nums = ints_stdin()
	n_nums = Counter(nums)
	map_nums = sorted(n_nums.keys(), reverse = True)
	h = 0
	cnt = 0

	while cnt < n:
		val = w
		for i in map_nums:

			while n_nums[i] != 0 and val >= i:
				n_nums[i] -= 1
				val -= i
				cnt += 1
		h += 1

	output(h)
