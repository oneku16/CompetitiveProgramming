
old, target = map(int, input().split())

g = list(map(int, input().split()))

if old == 1 and target == 1:
    print(0)
    exit()

power = 0

while 3**power< target:
    if 3**power not in g:
        g.append(3**power)
        power+=1
    elif target == 2 and g[0] == 1 and old == 1:
        g.append(3)
        power+=1
    else:
        power+=1



g.sort()
print(g)
if 0 in g:
    g.pop(0)
print(len(g)-old)