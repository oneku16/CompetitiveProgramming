from sys import stdin, stdout

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

	n = int_stdin()
	n_nums = ints_stdin()
	m = int_stdin()
	m_nums = ints_stdin()
	s = sum(m_nums) % n
	output(n_nums[s])