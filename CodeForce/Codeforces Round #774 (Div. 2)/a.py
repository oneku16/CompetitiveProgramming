from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, s = map(int, stdin.readline().split())
    stdout.write(str(s // n ** 2) + '\n')
