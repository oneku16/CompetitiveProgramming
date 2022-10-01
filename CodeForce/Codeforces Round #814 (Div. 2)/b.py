###############################
#        author: oneku        #
#  created: 16/08/2022 19:41  #
###############################


from sys import stdin, stdout
# import threading
# import queue
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

	n,k=ints_stdin()
	nums:list=[0]*n
	ans:list=[]
	usedn:list=[True]*n
	for i in range(n):
		nums[i]=i+1

	for i in range(n):
		if not nums[i]%4:
			ans.append([nums[i-1], nums[i]])
			usedn[i]=False
			usedn[i-1]=False 

	for i in range(n):
		for j in range(n):
			if not ((nums[i]+k) * nums[j])%4 and usedn[i] and usedn[j] and i!=j:
				ans.append([nums[i], nums[j]])
				usedn[i]=False
				usedn[j]=False 

	if all(usedn):
		output('NO')
	else:
		output('YES')
		for row in ans:
			output(row)
def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()