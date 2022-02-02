from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    nums.sort()
    memo = [nums[0]]
    for i in range(1, n):
        if nums[i] == 0: memo.append(0)
        elif nums[i] in memo and memo.count(nums[i]) == 1 and nums[i] != 0: memo.append(nums[i]*-1)
        else: memo.append(nums[i])
    memo = set(memo)
    stdout.write(str(len(memo))+'\n')