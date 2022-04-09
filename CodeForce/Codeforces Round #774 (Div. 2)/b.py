from sys import stdin, stdout


for _ in range(int(stdin.readline())):

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))

    nums.sort()

    i = 1
    j = n - 1
    l = nums[0]
    r = 0
    status = False
    while i < j:
        l += nums[i]
        r += nums[j]
        if l < r:
            status = True
            break
        else:
            i += 1
            j -= 1
            status = False
    if status: stdout.write("YES\n")
    else: stdout.write("NO\n")
