from sys import stdin, stdout

for _ in range(int(stdin.readline())):

    nums = list(stdin.readline())
    nums.pop()
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    maxval = 0
    ind1 = 0
    ind2 = 0
    for i in range(1, len(nums) - 2):
        if maxval < nums[i] + nums[i+1]: 
            maxval = nums[i] + nums[i+1]
            ind1 = i
            ind2 = i + 1
        if maxval < nums[i+1] + nums[i+2]: 
            maxval = nums[i+1] + nums[i+2]
            ind1 = i + 1
            ind2 = i + 2
    print(maxval, 21)

    if len(str(maxval)) == 1:
        nums[ind1] = maxval
        nums.pop(ind2)
    else:
        nums[ind1] = int(str(maxval)[0])
        nums[ind2] = int(str(maxval)[1])
    mynum = ''

    for num in nums:
        mynum+=str(num)
    
    stdout.write(mynum + '\n')
    
    