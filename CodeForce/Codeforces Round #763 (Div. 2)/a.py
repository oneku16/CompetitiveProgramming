from sys import stdin, stdout

for _ in range(int(stdin.readline())): 

    n, m, rb, cb, rd, cd = map(int, stdin.readline().split())
    cnt = 0
    if cb == cd or rb == rd: stdout.write('0\n')
    else:
        if cb < cd or rb > rd:
            stdout.write(str(abs(cd - cb)))
        elif cb < cd or rb > rd: pass 
            # stdout.write(str(min(abs(cd-cb), abs(rd - rb))) + '\n')
        



