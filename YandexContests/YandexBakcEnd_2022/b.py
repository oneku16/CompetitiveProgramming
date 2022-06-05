###############################
#        author: oneku        #
#  created: 03/06/2022 17:31  #
###############################

# libs
from sys import stdin, stdout
# from collections import Counter
# import multiprocessing, time
# from typing import List
# import itertools 
# import threading
# import queue
# from math import inf, gcd
# import heapq


# my input 
str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline().split(",")))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))

# my output
def output(val):
    if type(val) is list:
        length = len(val) 
        for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
    else: stdout.write(f"{val}\n")


def solve():

    # input part
    n = int_stdin()
    length = 0
    pos_counter = dict()
    for i in range(n):
        s, m = strs_stdin()
        length += int(m)
        pos_counter.update({s: int(m)})
    
    k = int_stdin()
    peoples = [0] * k
    # pos_counter = dict()
    for i in range(k):

        c, q, r, p = strs_stdin()
        peoples[i] = [c, q, int(r), (- 1 * int(p))]
        # peo_counter.update({q: [c, r, (- 1 * int(p))]})
        

    # creating sorted dict with sorted values 
    peoples = sorted(peoples, key = lambda val: (val[1], val[2], val[3]), reverse = True)
    peoples = {elem[1]: [name[0] for name in peoples if name[1] == elem[1]] for elem in peoples}
    
    candidates = ["~"] * length
    j = 0

    # for key, val in pos_counter.items():
    #     for i in range(val):
    #         candidates[j] = peoples[key][i]
    #         j+=1
    for key, val in pos_counter.items():
        for i in range(len(peoples[key])):
            candidates[j] = (peoples[key][i])
            j+=1
            if i == val - 1:
                break


    candidates.sort()
    for i in range(j):
        output(candidates[i]) 
    

def main(): solve()

if __name__ == '__main__': main()
