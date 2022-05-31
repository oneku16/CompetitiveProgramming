from sys import stdin, stdout


for _ in range(int(stdin.readline())):


	# n = int(stdin.readline())
	s = list(stdin.readline()[:-1])
	# nums = map(int, stdin.readline())
	nums = [int(i) for i in s]


	# cnt = 0
	if len(s) == 2: stdout.write(s[-1] + '\n')
	else: stdout.write(str(min(s) + '\n'))
