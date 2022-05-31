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

def bob(a, a_nums, b, b_nums) -> str:

	if a_nums[-1] == b_nums[-1]: return "Bob"
	else:
		if a_nums[-1] > b_nums[-1]: return "Alice"
		else: return "Bob"
def alice(a, a_nums, b, b_nums) -> str:

	if a_nums[-1] == b_nums[-1]: return "Alice"
	else:
		if a_nums[-1] > b_nums[-1]: return "Alice"
		else: return "Bob"

for _ in range(int_stdin()):

	a = int_stdin()
	a_nums = ints_stdin()
	a_nums.sort()
	b = int_stdin()
	b_nums = ints_stdin()
	b_nums.sort()
	output(alice(a, a_nums, b, b_nums))
	output(bob(a, a_nums, b, b_nums))