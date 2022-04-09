from sys import stdin, stdout


for _ in range(int(stdin.readline())):

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))

    nums = [abs(i) for i in nums]


    print(nums)
    print(nums.index(min(nums)))


    # aabbdabdccc