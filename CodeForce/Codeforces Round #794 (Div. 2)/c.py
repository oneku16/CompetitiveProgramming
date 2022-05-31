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
	nums = ints_stdin()
	nums.sort()
	spots = []
	c = 0
	if n % 2: output("NO")
	else:
		while len(spots) < n:
			if len(spots) == n - 1: spots.append(nums[c])
			else:
				spots.append(nums[c])
				spots.append(True)
			c+=1
		yes = True
		for i in range(n):
			if spots[i] is True:
				spots[i] = nums[c]
				c+=1
		for i in range(n):
			if i == n - 1:
				if (spots[-2] == spots[-1] or spots[-1] == spots[0]):
					yes = False
				
					break
			elif i == 0:
				if (spots[0] == spots[-1] or spots[0] == spots[1]):
					yes = False
			
					break
			else:
				if (spots[i-1] == spots[i] or spots[i] == spots[i + 1]):
					yes = False
					break
		
		if yes: 
			output("YES")
			output(spots)
		else: output("NO")
	