from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s  = [0] + list(str(stdin.readline()))
    s.pop()
    ansl = []
    ansr = []
    l = 1
    r = n
    while l < r:
        if s[l] == s[r]:
            r-=1
            l+=1
            ansl.append(s[l])
            ansr.append(s[r])
        else: r-=1
    print(ansr, ansl)



    # stdout.write(str(nums)+'\n')




