from sys import stdin, stdout

for _ in range(int(stdin.readline())):


    nums = list(map(int, stdin.readline().split()))
    n, m = map(int, stdin.readline().split())


    for row in nums: stdout.write(str(row) + '\n')