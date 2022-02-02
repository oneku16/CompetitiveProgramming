from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    
    if n % 7 == 0:
        stdout.write(str(n) + '\n')
    
    elif n % 10 + (7 - n % 7) < 10:
        stdout.write(str(n + (7 - n % 7)) + '\n')
    else:
        stdout.write(str(n - n % 7) + '\n')