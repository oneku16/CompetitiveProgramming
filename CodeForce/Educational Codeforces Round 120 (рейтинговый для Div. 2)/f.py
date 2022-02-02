from sys import stdin, stdout
from math import factorial as f

n = int(stdin.readline())
# memo = [0,1,2,6] + [0 for i in range(n)]
fac = []
for i in range(1, n+1): fac.append(f(i))

