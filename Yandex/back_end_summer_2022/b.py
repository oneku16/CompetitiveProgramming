###############################
#       author: Elnazar       #
#  created: 16/06/2022 13:53  #
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


# my input 
str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline()[:-1].split(",")))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))

# my output
def output(val):
    if type(val) is list:
        length = len(val) 
        for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
    else: stdout.write(f"{val}\n")


# my solution
class Position:

    count = Counter()

    def __init__(self, line: str):

        line = line.strip().split(',')
        self.name = line[0]
        self.n = int(line[1])
        type(self).count[self.name] = self.n

    def __repr__(self) -> str:  return f"{self.name} {self.n}"


class Candidate:

    def __init__(self, line: str):

        line = line.strip().split(',')
        self.name = line[0]
        self.pos = line[1]
        self.score = int(line[2])
        self.penalty = int(line[3])

    def __repr__(self): return self.name

    def __lt__(self, other) -> bool:
        if self.score < other.score: return True
        elif self.score == other.score and self.penalty > other.penalty: return True
        else: return False

    def __eq__(self, other): return self.score == other.score and self.penalty == other.penalty


def solve():

    with open("input.txt", 'r') as file: lines = file.readlines()

    n = int(lines[0].strip())

    positions: list[Position] = [Position(line) for line in lines[1:n+1]]
    candidates: list[Candidate] = [Candidate(line) for line in lines[n+2:]]

    people_on_position = defaultdict(list)
    for p in candidates: people_on_position[p.pos].append(p)
    res: list[Candidate] = []
    for pos in people_on_position:
        people_on_position[pos].sort(reverse = True)
        people_on_position[pos] = people_on_position[pos][:Position.count[pos]]
        res.extend(people_on_position[pos])

    candidate = sorted(candidate.name for candidate in res)
    
    with open("output.txt", 'w') as file:
        for name in candidate: file.write(name +'\n') 
        


if __name__ == "__main__": solve()
