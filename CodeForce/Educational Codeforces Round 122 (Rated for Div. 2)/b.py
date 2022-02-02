from sys import stdin, stdout

for _ in range(int(stdin.readline())):

    n = input()
    o = 0
    z = 0
    for i in n:
        if i == 0: z+=1
        else: o+=1
    if o == z: stdout.write(str(min(o,z) -1) + "\n")
    else: stdout.write(str(min(o,z)) + "\n")