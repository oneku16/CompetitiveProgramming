from sys import stdin, stdout


for _ in range(int(stdin.readline())):

    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    
    linlsit = []
    for i in range(n):
        linlsit.append([a[i], b[i]])

    linlsit.sort()
    
    i = 0
    while linlsit[i][0] <= k:
        
        k+=linlsit[i][-1]
        i+=1
        if i == n: break
        
    stdout.write(str(k)+'\n')

    