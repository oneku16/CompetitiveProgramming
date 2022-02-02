from sys import stdin, stdout


for _ in range(int(stdin.readline())):
    nums = list(map(int, stdin.readline().split()))
    
    
    nums.sort()
    if sum(nums) % 2 == 0: 
        if nums[0] == nums[1] or nums[1] == nums[2]: stdout.write('YES\n')
        elif nums[-1] - nums[0] == nums[1]: stdout.write('YES\n')
        else: stdout.write('NO\n')
    else: stdout.write('NO\n')