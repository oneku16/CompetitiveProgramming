

from sys import stdin, stdout



for _ in range(int(stdin.readline())):


    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))

    i = 0
    ans = "YES"
    while i < n - 1:
        
        if nums[i] > nums[i + 1]:
            if (nums[i] + nums[i + 1]) % 2 == 1:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i+=1
            else:
                ans = "NO" 
                break
        else: i+=1

    stdout.write((str(nums)+": "+ans) + "\n")


