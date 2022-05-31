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
	a = ints_stdin()
	b = ints_stdin()

	cnt = 0
	order = []
	# used = [False for i in range(n)]
	for i in range(n - 1):
		for j in range(n - 1 - i):
			if a[j] > a[j + 1] :
            	a[j], a[j + 1] = a[j + 1], a[j]
                b[j], b[j + 1] = b[j + 1], b[j]
                order.append([j, j + 1])
            

                




	

