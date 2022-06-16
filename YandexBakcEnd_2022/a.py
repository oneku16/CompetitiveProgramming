###############################
#       author: Elnazar       #
#  created: 16/06/2022 14:26  #
###############################

# libs
from sys import stdin, stdout
from collections import defaultdict, Counter
# import multiprocessing, time
# from typing import List
# import itertools 
# import threading
# import queue
# from math import inf, gcd
# import heapq

# my stdio 
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
    
    ## input part
    with open("input.txt", 'r') as file:
        line = list(word for word in file.readlines())
    
    s = list(line[0][:-1])
    q = list(line[1])
    
    ## initializing variables:
    s_count = Counter(s)
    q_count = Counter(q)
    length = len(s)
    answer = [1] * length

    # Solutions:
    for i in range(length):
        if s[i] == q[i]:
    
            answer[i] = 0
            q_count[s[i]] -= 1
            s_count[s[i]] -= 1


    with open("output.txt", 'w') as file:
        
        for i in range(length):
            if answer[i]:
                if q[i] in s_count:
                    if s_count[q[i]] == 0: file.write("absent" + ['','\n'][i != length - 1])
                    else:
                        s_count[q[i]] -= 1
                        file.write("present" + ['','\n'][i != length - 1])
                else: file.write("absent" + ['','\n'][i != length - 1])
            else: file.write("correct" + ['','\n'][i != length - 1])


if __name__ == '__main__': solve()