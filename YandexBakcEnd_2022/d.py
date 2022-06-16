###############################
#       author: Elnazar       #
#  created: 16/06/2022 16:13  #
###############################


from sys import stdin, stdout
from collections import Counter
import time
import json
# import multiprocessing
# from typing import List
# import itertools 
# import threading
# import queue
# from math import inf, gcd
# import heapq




# my stdio 
str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline()[:-1].split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val):
    if type(val) is list:
        length = len(val) 
        for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
    else: stdout.write(f"{val}\n")


def solve():

    with open("input.txt", 'r') as file:

        lines = [line[:-1] for line in file.readlines()]
    n, m = map(int, lines[0].split())
    

if __name__ == '__main__': solve()