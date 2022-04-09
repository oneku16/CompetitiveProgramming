
from sys import stdin, stdout
from collections import Counter



for _ in range(int(stdin.readline())):


    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    if len(set(nums)) == 1:
        stdout.write('0\n')
    else:
        nums = Counter(nums)
        rep = max(nums.values())  
        c = 0
        while rep * 2 < n:
            c+=1
            c+=rep
            rep*=2
        c += 1
        c += n - rep
        stdout.write(str(c) + '\n')