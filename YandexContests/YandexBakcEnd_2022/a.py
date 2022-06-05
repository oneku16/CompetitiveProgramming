from sys import stdin, stdout
from collections import Counter
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
    s = list(str_stdin())
    q = list(str_stdin())
    

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

    for i in range(length):
        if answer[i]:
            if q[
            i] in s_count:
                if s_count[q[i]] == 0:output("ABSENT")
                else:
                    s_count[q[i]] -= 1
                    output("PRESENT")
            else: output("ABSENT")
        else: output("CORRECT")


def main(): solve()

if __name__ == '__main__': main()
