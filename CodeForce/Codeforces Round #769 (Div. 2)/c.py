from sys import stdin, stdout

for _ in range(int(stdin.readline())):

    a, b = map(int, stdin.readline().split())
    cnt = 0
    while True:
        if int(bin(a | b), 2) == a or int(bin(a | b), 2) == b:
            cnt += 1
            if a == b: break

            
    stdout.write("ans: " + str(cnt) + '\n')