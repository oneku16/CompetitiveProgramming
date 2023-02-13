###############################
#       author: Elnazar       #
#  created: 16/06/2022 17:33  #
###############################


from sys import stdin, stdout
# import threading
# import queue
from collections import Counter
# from math import inf, gcd
# import heapq
# import itertools


str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline()[-1].split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(leftside, rightside) -> str: pass


def main():

	with open("input.txt", "r") as file:
		line = list(file.readline())

	# with open("output.txt", "w") as file:
	# 	file.write(line)
	length = len(line)
	new_line = []
	open_brackets = []
	close_brackets = []
	j = 0
	for i in range(length):
		if line[i].isalpha(): 
			new_line.append(f"{ord(line[i])}")
			j+=1
		elif line[i] in ['+', '-', '*', '/', '(', ')']: 
			if line[i] == '(': open_brackets.append([i, j])
			elif line[i] == ')': close_brackets.append([i, j])
			new_line.append(line[i])
			j+=1
	# super_l = len(open_brackets) + len(close_brackets)
	print(f"{new_line}")
	for j in range(len(open_brackets)):
		ind = open_brackets[j][-1]
		my_eval = "".join(new_line[:ind] + new_line[ind+1:]) 
		print(my_eval)
	# print(f"{super_l}") 
	print(f"{open_brackets}\n{close_brackets}")



if __name__ == "__main__": main()