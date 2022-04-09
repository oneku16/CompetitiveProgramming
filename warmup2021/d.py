n = int(input())


xes = list(map(int, input().split()))


yaxes = xes

i = 1
j = 0
ys = []
ys.append(1)

while i < len(xes)-1:
    c = 1
    while c < (ys[-1] + xes[j]):
        print(c)
        
        print(*ys)
        c+=1
    ys.append(c)
    i+=1
    j+=1

print(*ys)



