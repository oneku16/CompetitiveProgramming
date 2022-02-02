from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nums = [[0 for i in range(n+2)]]
    nums = [0] + list(map(int, stdin.readline().split()))
    if sum(nums) % n == 0: print(0)
    else: print(1)