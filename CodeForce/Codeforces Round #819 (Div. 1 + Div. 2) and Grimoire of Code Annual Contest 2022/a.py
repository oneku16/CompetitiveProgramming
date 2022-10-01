###############################
#        author: oneku        #
#  created: 06/09/2022 20:19  #
###############################


from sys import stdin, stdout
from copy import deepcopy
# import threading
# import queue
# from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline().split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: map(int, stdin.readline().split())
int_list_stdin = lambda: list(map(int, stdin.readline().split()))



def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(): 

	n=int_stdin()
	nums=int_list_stdin()
	if n==1:
		return 0
	ans=nums[-1]-nums[0]
	for i in range(n-1):
		ans=max(nums[i]-nums[i+1],ans)
	slice=max(max(nums[1:])-nums[0], nums[-1]-min(nums[:-1]))
	ans=max(slice,ans)
	return ans

	# sortedNums=deepcopy(sorted(nums))
	# ans=0
	# for i in range(n):
	# 	maxInd=nums.index(sortedNums[n-1-i])
	# 	minInd=nums.index(sortedNums[i])
	# 	if maxInd > minInd:
	# 		output(f'diff:{sortedNums[n-1-i]}-{sortedNums[i]}')
	# 		ans=max(abs(abs(sortedNums[n-1-i]-sortedNums[i])),ans)
	# output(f'{ans=}')
	# output(ans)



def main():
	for _ in range(int_stdin()): output(solve())


if __name__ == "__main__": main()