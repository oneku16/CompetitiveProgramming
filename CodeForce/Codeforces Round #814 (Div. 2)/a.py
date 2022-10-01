# ###############################
# #        author: oneku        #
# #  created: 16/08/2022 19:41  #
# ###############################


# from sys import stdin, stdout
# # import threading
# # import queue
# # from collections import Counter
# # from math import inf, gcd
# # import heapq
# # import itertools

# str_stdin = lambda: stdin.readline()[:-1]
# strs_stdin = lambda: list(map(str, stdin.readline().split()))
# int_stdin = lambda: int(stdin.readline())
# ints_stdin = lambda: list(map(int, stdin.readline().split()))


# def output(val):
# 	if type(val) is list:
# 		length = len(val) 
# 		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
# 	else: stdout.write(f"{val}\n")


# def solve(): 


# 	n,m=ints_stdin()
# 	winner:str=''
# 	if n==m:
# 		winner='Tonya'
# 	else:
# 		if n>m:
# 			if n%2 and not m%2:
# 				winner='Burenka'
# 			elif m%2 and not n%2:
# 				winner='Burenka'
# 			elif n%2 and m%2:
# 				winner='Tonya'
# 			elif not n%2 and not m%2:
# 				 winner='Tonya'
# 		else:
# 			if n%2 and not m%2:
# 				winner='Burenka'
# 			elif m%2 and not n%2:
# 				winner='Burenka'
# 			elif n%2 and m%2:
# 				winner='Tonya'
# 			elif not n%2 and not m%2:
# 				 winner='Tonya'
# 	output(winner)




	

# def main():
# 	for _ in range(int_stdin()): solve()


# if __name__ == "__main__": main()



###############################
#        author: oneku        #
#  created: 16/08/2022 19:41  #
###############################
 
 
from sys import stdin, stdout
# import threading
# import queue
from collections import Counter
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
    string:str=''
    for i in range(2):
    	string+=str_stdin()
    string=Counter(string)	
    output(len(string)-1)
 
 
 
 
	
 
def main():
	for _ in range(int_stdin()): solve()
 
 
if __name__ == "__main__": main()