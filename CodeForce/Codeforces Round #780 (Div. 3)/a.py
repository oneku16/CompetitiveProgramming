from sys import stdin, stdout


for _ in range(int(stdin.readline())):

    a, b = map(int, stdin.readline().split())
    
    s = 0
    if a == 0: s = a + 1
    else:  
        s = a * 1 + b * 2
        s += 1
    stdout.write(str(s) + '\n')