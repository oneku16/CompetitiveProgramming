from sys import stdin, stdout

for _ in range(int(stdin.readline())):

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    i = n - 1
    cnt = 0
    val = nums[-1]
    while i >= 0:
        if nums[i] != val:
            cnt += 1
            i-=(n-i-1)
        else: i-=1
    
    stdout.write(str(cnt) + '\n')