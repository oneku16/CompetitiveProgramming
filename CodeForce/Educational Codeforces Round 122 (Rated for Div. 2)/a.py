from sys import stdin, stdout

nums = [str(i) for i in range(10, 1000) if i % 7 == 0]
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    l = n - 1
    r = n + 1
    if str(n) in nums:
        stdout.write(str(n) + '\n')
    else:
        while True:
            if str(l) in nums or str(r) in nums:
                if str(l) in nums and len(str(l)) == len(str(n)):#len(nums[nums.index(str(l))]):
                    c = 0
                    for i in range(len(str(l))): 
                        if str(l)[i] != str(n)[i]: c+=1
                    if c == 1: 
                        stdout.write(str(l) + '\n')
                        break
                    else: 
                        l-=1
                else: 
                    l-=1
                if str(r) in nums and len(str(r)) == len(str(n)):#len(nums[nums.index(str(r))]):
                    c = 0
                    for i in range(len(str(r))):
                        if str(r)[i] != str(n)[i]: c+=1
                    
                    if c == 1: 
                        stdout.write(str(r) + '\n')
                        break
                    else: 
                        r+=1
                else: 
                    r+=1
            else:
                r+=1
                l-=1



              