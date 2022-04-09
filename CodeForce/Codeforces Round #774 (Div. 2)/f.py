from sys import stdin, stdout



cards =[]
for _ in range(int(stdin.readline())):cards.append(list(map(int, stdin.readline().split())))

status = True
while status:

    for c in cards:
        if len(set(c)) == 1:Status = False
        else:status = True


if status is False: stdout.write(str(0)+'\n')
for row in cards: stdout.write(str(row) + '\n')
