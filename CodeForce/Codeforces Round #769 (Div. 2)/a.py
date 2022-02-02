from sys import stdin, stdout

for _ in range(int(stdin.readline())):

    n = int(stdin.readline())
    a = str(stdin.readline())
    
    if  n == 2:
        if a[0] == a[-1]: stdout.write('NO\n')
        else: stdout.write('YES\n')
    elif n == 1: stdout.write('YES\n')
    else: stdout.write('NO\n')