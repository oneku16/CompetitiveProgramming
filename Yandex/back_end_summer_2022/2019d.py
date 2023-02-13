###############################
#        author: oneku        #
#  	     just solving)   	  #
###############################
from sys import stdin,stdout
from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

# str_stdin = lambda:stdin.readline()[:-1]
# strs_stdin = lambda:list(map(str, stdin.readline().split()))
# int_stdin = lambda:int(stdin.readline())
ints_stdin = lambda:(map(int, stdin.readline().split()))
# int_list_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val, def_end = "\n") -> None:
	if type(val) is list:
		length = len(val) 
		for elem in range(length): 
			stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: 
		stdout.write(f"{val}{def_end}")


def solve()->str:

	n,m=ints_stdin()
	if max(m,n)==2:
		return 2
	return n**2-1 if n==m else n*m                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
	# return (min(n,m)**2)- 1 + (abs(n-m)*(2*min(n,m)-1))


if __name__ == "__main__": 
	print(solve())