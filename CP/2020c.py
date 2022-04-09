from collections import Counter
from typing import List

brackets = list(map(str, input().strip()))


# def checker(target: List[chr])->bool:
#     for i in range (len(target)-1):

#         if target.count('(') == target.count(')') and target[0] == '(' and target[-1] == ')':
#             return True


def remove(target: List[chr]):
    target.pop(-1)
    target.pop(0)
    

counter = 0
while any(brackets):
    
    ind_open = 0
    ind_close = 1
    i = 0
    while True:
        if brackets[i] == ')':
            brackets.pop(i)
        else:
            if brackets[ind_open] == '(' and brackets[ind_close] ==')':
                brackets.pop(ind_open)
                brackets.pop(ind_close)
                print(34, brackets[ind_open], brackets[ind_close])
            elif brackets[ind_open] == '(' and brackets[ind_close] == '(':
                ind_open+=1
                ind_close+=1
                print(brackets[ind_open], brackets[ind_close])
                brackets.pop(ind_open)
                brackets.pop(ind_close)
                print(41)

        if any(brackets) is False:
            break



            
        
            

        



# counter = 0
# for i in range (len(brackets)):
#     target = []
#     if brackets[i] == '(':
#         for j in range (i, len(brackets)):
#             target.append(brackets[j])
#             if checker(target) is True:
#                 counter+=1
#                 print(*target)
# print(counter)




