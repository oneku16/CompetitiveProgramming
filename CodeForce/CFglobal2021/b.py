from statistics import mode
from sys import stdin
for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    nums = [i for i in range(a, b+1)]
    bincode = [(bin(i)[2:]) for i in nums]
    # print(b-a - max(set(bincode), key = bincode.count))
    for row in bincode: print(row)


