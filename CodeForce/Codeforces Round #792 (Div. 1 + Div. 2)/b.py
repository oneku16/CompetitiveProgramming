from sys import stdin, stdout


for _ in range(int(stdin.readline())):


	a, b, c = map(int, stdin.readline().split())


	n = [a,b,c]
	q = [a, b, c]
	q.sort()
	

	z = max(a, b, c)

	x = q[1] * q[2] + q[1] + q[0]

	y = x - n[0]



	stdout.write("{} {} {}".format(x, y, z) + "\n")