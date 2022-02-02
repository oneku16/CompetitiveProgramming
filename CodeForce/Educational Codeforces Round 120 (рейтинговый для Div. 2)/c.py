from sys import stdin, stdout


for _ in range(int(stdin.readline())):

    n, k = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))
    if sum(nums) < k:stdout.write('0\n')
    else:
        nums.sort()
        new_nums = []
        i = 0
        while sum(new_nums) < k: 
            new_nums.append(nums[i])
            i+=1
        print (new_nums) 





