# Bismillah
##############################
#      author: oneku16       #
#  trying to solve problems  #
##############################


import os
import sys
from io import BytesIO, IOBase
from typing import Any

from collections import Counter, deque, defaultdict
# from itertools import accumulate, starmap
# from bisect import bisect, bisect_left, bisect_right
# from functools import reduce, wraps, lru_cache, cache
# from heapq import heappush, heappop
from re import compile, sub


BUFFER_SIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFFER_SIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, **kwargs):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFFER_SIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


# sys.stdin = IOWrapper(sys.stdin)
# sys.stdout = IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")

read_int = lambda: int(input())
read_ints = lambda _tuple=False: tuple(map(int, input().split())) if _tuple else map(int, input().split())
read_nums = lambda _sort=False, _reverse=False: list(map(int, input().split())) if not _sort else sorted(list(map(int, input().split())), reverse=_reverse)
read_str = lambda: str(input())
read_strs = lambda: map(str, input().split())
read_list_str = lambda: list(map(str, input().split()))

output = lambda value: sys.stdout.write(' '.join(map(str, value)) + "\n") if isinstance(value, (list, set, tuple)) else sys.stdout.write(f"{value}\n")

MAX = 1_000_000_007
MIN = -1_000_000_007

yes_no = lambda _status: "Yes" if _status else "No"
alice_bob = lambda _status: "Alice" if _status else "Bob"

'''

'''


def read_from_file():
    with open('input.txt', 'r') as file:
        return file.read().replace('\n', '')


def find_bounds(indexes, left, right, target):
    size = len(indexes)
    while indexes[left] == indexes[right] == target and left >= 0 and right <= size - 1:
        if indexes[left - 1] == target:
            left -= 1
        if indexes[right + 1] == target:
            right += 1

    return right - left + 1


def solve():

    k = read_int()
    string = read_str()
    positions = {}
    for index, letter in enumerate(string):
        if letter not in positions:
            positions[letter] = []
        positions[letter].append(index)
    answer = k
    for letter, indexes in positions.items():
        for i in range(len(indexes) - 1):
            delta = indexes[i + 1] - indexes[i] - 1
            if delta <= k:
                answer = max(find_bounds(indexes, indexes[i], indexes[i + 1], target=letter), answer)
            elif delta > k:
                pass


def main() -> None:
    output(solve())
    # solve()
    # for _ in range(read_int()):
    #     output(solve())


if __name__ == "__main__":
    main()
