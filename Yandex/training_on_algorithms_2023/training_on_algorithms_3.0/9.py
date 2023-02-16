# Bismillah
##############################
#      author: oneku16       #
#  trying to solve problems  #
##############################


import os
import sys
from io import BytesIO, IOBase
from typing import Any

# from collections import Counter, deque, defaultdict
from itertools import accumulate, starmap
# from bisect import bisect, bisect_left, bisect_right
# from functools import reduce, wraps, lru_cache, cache
# from heapq import heappush, heappop


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


sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

read_int = lambda: int(input())
read_ints = lambda _tuple=False: tuple(map(int, input().split())) if _tuple else map(int, input().split())
read_nums = lambda _sort=False, _reverse=False: list(map(int, input().split())) if not _sort else sorted(list(map(int, input().split())), reverse=_reverse)
read_str = lambda: str(input())
read_strs = lambda: map(str, input().split())
read_list_str = lambda: list(map(str, input().split()))

output = lambda value: sys.stdout.write(' '.join(map(str, value)) + "\n") if isinstance(value, (list, set, tuple)) else sys.stdout.write(f"{value}\n")

MAX = 1_000_000_007
MIN = -1_000_000_007

'''
'''


def read_from_file():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        n, m, k = map(int, lines[0].split())
        matrix = [[]] * n
        commands = [[]] * k
        for i in range(1, n + 1):
            matrix[i - 1] = list(accumulate(map(int, lines[i].split())))
        for i in range(n + 1, n + 1 + k):
            commands[i - n - 1] = list(map(int, lines[i].split()))
        return n, m, k, matrix, commands


def solve() -> Any:

    n, m, k, matrix, commands = read_from_file()

    answer = [0] * k
    for q in range(k):
        x_1, y_1, x_2, y_2 = commands[q]
        counter = 0
        for i in range(x_1 - 1, x_2):
            if y_1 - 1:
                counter += matrix[i][y_2 - 1] - matrix[i][y_1 - 2]
            else:
                counter += matrix[i][y_2 - 1]
        # output(counter)
        answer[q] = counter

    return '\n'.join(map(str, answer))


def main() -> None:
    output(solve())
    # solve()
    # for _ in range(read_int()):
    #     output(solve())


if __name__ == "__main__":
    main()
