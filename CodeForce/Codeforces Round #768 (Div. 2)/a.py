from sys import stdin, stdout

for _ in range(int(stdin.readline())):

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
  
    for i in range(n):
        if b[i] > a[i]: a[i],  b[i] = b[i], a[i]
        else: pass
   
    stdout.write(str(max(a) * max(b)) + '\n')