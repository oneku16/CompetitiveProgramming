###############################
#        author: oneku        #
# created at 28/09/2022 11:32 #
###############################

# Bismillah
from sys import stdin, stdout
# import threading
# import queue
# from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

str_stdin = lambda: stdin.readline()[:-1] # reads only one input str type: input-> 'a' 
strs_stdin = lambda: list(map(str, stdin.readline().split())) # reads list with str odjects: ['a','b','c',...]   
int_stdin = lambda: int(stdin.readline()) # reads input int type: 1 
ints_stdin = lambda: map(int, stdin.readline().split()) # same with prev but use it if u know all ur variables like a b <-> 1 2 
int_list_stdin = lambda: list(map(int, stdin.readline().split())) #same with strs_stdin but reads int only: [1,2,3,4,5,6,7,8,9,10,...]


# use output() instead of print(), ex: output('YES') -> YES, output(3.14) -> 3.14 
def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")

# u can write main logic here, but remember that calling methods is expensive
def solve(): 

	n = int_stdin()
	nums = int_list_stdin()
	nums2=[0]*n
	nums2[0]=nums[0]
	for i in range(1,n):
		a,b=nums2[i-1]+nums[i], nums2[i-1]-nums[i]
		if a*b<0 or a==b:
			nums2[i]=max(a,b)
		else:
			return -1
	return nums2
	# a, b = ints_stdin()
	# s = str_stdin()
	# s_list = strs_stdin() 
	# pass 


# u can write main logic here as well!
def main():

	# n = int_stdin() #ex: 1
	# nums = int_list_stdin() #ex: 1 2 3 4 5 ...
	# a, b = ints_stdin() #ex: 1 2
	# s = str_stdin() #ex: 'name'
	# s_list = strs_stdin() #ex: 'a', 'name', 'blahblah'
	for _ in range(int_stdin()): output(solve()) # calls solve() method user_input times
	# pass # remove it

if __name__ == "__main__": main()