from sys import stdin, stdout


for _ in range(int(stdin.readline())):

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))


    nums.sort(reverse = False)
    if n == 1: 
        if nums[-1] >= 2: stdout.write('NO\n')
        else: stdout.write('YES\n')
    elif nums[-1] - 1 > nums[-2]: stdout.write('NO\n')
    else: stdout.write('YES\n')


    # aabbdabdccc