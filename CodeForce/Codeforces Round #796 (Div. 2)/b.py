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
	n_nums = sorted(ints_stdin())

	odd = 0
	even = 0
	def iseq(a: int, b: int):
		return True if a > b else False
	evenlist = []
	# two = [1] * n
	for i in range(n):
		if n_nums[i] % 2: odd+=1
		else:
			# if str(n_nums[i])[-1] == "2" and len(str(n_nums[i])) != 1: two[i] = 0
			evenlist.append(n_nums[i]) 
			even += 1
	if odd == even: output(n/2)
	
	elif odd > even: output(even)

	elif odd < even:
		cnt = 0
		if odd: 
			while (even > odd):
				cnt+=odd
				even -= odd
		else:
			cnt += (even - 1)
		i = 0
		summ = 0
		while even > 0:
			summ+= n_nums[i]
			even -= 1
			i += 1
		while(summ%2==0):
			cnt+=1
			summ /= 2

		output(cnt)



def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()