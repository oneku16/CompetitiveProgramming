n = int(input())
nums = list(map(int, input().split()))

ans = []

if len(nums) <=4:
    print(-1)
else:
    if n%2==0:
        for i in range (0, len(nums), 2):
            ans.append(nums[i])
        for i in range (1, len(nums), 2):
            ans.append(nums[i])
        ans[-1], ans[-2] = ans[-2], ans[-1]
    else:
        for i in range (0, len(nums), 2):
            ans.append(nums[i])
        for i in range (1, len(nums), 2):
            ans.append(nums[i])

print(*ans)