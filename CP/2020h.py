# my_dict = dict()
# A, B, C, D, E, F, G = 0, 0, 0, 0, 0, 0, 0
# abc = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G}

# for i in range(int(input())):
#     userinput = input()
#     if len(userinput) == 3:
# a b c d e f g 

from copy import deepcopy as dc

l = [1,0,0,0,0,0,0]
l1 = []
main = []

p = 0
for i in range(1001):
    l[5] = (l[1]+l[6]) % 265
    l[1] = (l[0]+l[1]) % 265
    l[0] = (l[5]+l[6]) % 265
    l1 = dc(l)
    if l1 not in main:
        main.append(l1)
    else: p = i




print(l)
print(l1)

# print(format(1001, 'b'))