###############################
#        author: oneku        #
# created at 12/09/2022 17:27 #
###############################

# Bismillah
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
ints_stdin = lambda: map(int, stdin.readline().split())
int_list_stdin = lambda: list(map(int, stdin.readline().split()))

def output(val):
	if type(val) is list:
		length = len(val) 
		for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
	else: stdout.write(f"{val}\n")


def solve(): 

    n = int_stdin()
    x = ints_stdin()
    y = ints_stdin()
    ans = 0
    z = []
    zneg = []
    for i in range(n):
        tmp =  y[i] - x[i]
        if tmp < 0:
            zneg.append(tmp)
        else:
            z.append(tmp)
 
    zi = len(z)-1
    zni = len(zneg)-1
    z.sort()
    zneg.sort()
 
    print(f'{x=}')
    print(f'{y=}')
    print(f'{z=}')
    print(f'{zneg=}')
    k = 0
    for i in range(len(z)-1,-1,-1):
        for j in range(k,len(zneg)):
            if zneg[j] != 0 and z[i] + zneg[j] >= 0:
                ans += 1
                zneg[j] = 0
                k = j+1
                break
        else:
            ans += (i+1)//2
            break
    return ans



def main():
	for _ in range(int_stdin()): solve()


if __name__ == "__main__": main()


