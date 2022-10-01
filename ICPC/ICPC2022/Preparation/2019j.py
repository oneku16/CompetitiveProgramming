# Bismillah
from sys import stdin, stdout
# import threading
# import queue
# from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools

str_stdin = lambda: stdin.readline()[:-1]
# strs_stdin = lambda: list(map(str, stdin.readline().split()))
# int_stdin = lambda: int(stdin.readline())
# ints_stdin = lambda: map(int, stdin.readline().split())
# int_list_stdin = lambda: list(map(int, stdin.readline().split()))

def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): 
			stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: 
		stdout.write(f"{val}\n")

def isPalindrome(word:str)-bool:
	n=len(word)
	for i in range(n//2):
		if word[i]!=word[n-1-i]:
			return False
	return True

def main():

	nameOne=str_stdin()
	nameTwo=str_stdin()[::-1]
	n=len(nameOne)
	cnt=0
	for i in range(n//2):
		if nameOne[i]==nameTwo[i]:
			cnt+=1
		else:
			break
	if not n%2:
		if cnt*2+1==n:
			return cnt
		return n-cnt if isPalindrome(nameOne[:n-cnt]) else -1

	else:
		if cnt*2==n:
			pass

	# arttem
	# arttep
	# arttra







if __name__ == "__main__": output(main())