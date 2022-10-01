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

def main():


	s=str_stdin()
	n=len(s)
	if s.count('K') == 1 or s.count('G')==1:
		if s[-1] == s[0]:
			return 1
		else:
			return 0
	if s.count('K') == n or s.count('G')==n:
		return 0
	l=0
	r=0
	# if not n%2:
	for i in range(n//2):
		if s[i]=='G':
			l+=1
		if s[n-1-i] =='G':
			r+=1
	ans1=min(l,r)
	if n%2:
		if s[n//2]=='G':
			ans1+=1
	return ans

	# def isPalindrome(s:str,n:int):
		
	# 	cnt=0
	# 	for i in range(n//2):
	# 		cnt+=1
	# 		if s[i]!=s[n-1-i]:
	# 			return False
	# 	return True

	# nameOne=str_stdin()
	# nameTwo=str_stdin()[::-1]
	# n=len(nameOne)

	# stop=0
	# for i in range(n//2):
	# 	if nameOne[i]==nameTwo[i]:
	# 		stop+=1
	# 	else: break

	# if stop*2==n:
	# 	return stop
	# elif stop*2>n:
	# 	if nameOne[stop]==nameTwo[stop]:
	# 		return stop
	# 	else:























	# if n==1:
	# 	return -1
	# if n==2:
	# 	name1,name2=isPalindrome(nameOne,n),isPalindrome(nameTwo,n)
	# 	if name1 and name2 and nameOne==nameTwo:
	# 		return -1
	# 	if name1 and name2 and nameOne!=nameTwo:
	# 		return n


	





























	# cnt=0
	# for i in range(n):
	# 	if nameOne[i]==nameTwo[i]:
	# 		cnt+=1
	# 	else:
	# 		break
	# 	if cnt==2:
	# 		break
	# if cnt==2:
	# 	return cnt
	# 	# for i in range(cnt,n-cnt):
	# 	# 	if nameOne[i]==nameOne[n-1-i]:
	# 	# 		cnt=min(cnt,)
	# else:

	# 	return n if isPalindrome(nameOne,n) else -1
	# return 1



if __name__ == "__main__": output(main())