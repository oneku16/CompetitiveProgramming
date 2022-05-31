
from typing import List


def solve(item :List[int])-> str:
    def converter(target: List[int])-> str:
        answer = ""
        for num in target:
            answer+=chr(num)
        return answer
    dig = [65,80,81]
    let = ['A', 'P', 'Q']
    newitem = []
    for i in range (len(item)-1, -1, -1):
        newitem.append(item[i])
    ind_max = item.index(max(newitem))
    if item[-1] != max(newitem):
      item[ind_max + 1] = dig[dig.index(item[ind_max + 1])+1]
      return converter(item)
    
    if item.count(item[-1]) == len(item):
        if item[-1] == 81:
            item[0]
            for i in range(len()):
                pass
    
    
    elif item.count(item[-1]) != len(item):
        print(i)
        print(item)
        print(item[i])
        print(max(newitem))
        i = len(item)-1
        while item[i] == max(newitem):
            i-=1
            if i == 0:
                break
        item[i] = dig[dig.index(item[i])+1]
        item[i+1] = 65
        return converter(item)
    # item[i], item[i-1] = dig[let.index(chr(max(newitem)))], dig[let.index(chr(max(newitem)))]
    
    
    # print(item)
    # stop = True
    # while stop:
    #     if item[i] == max(newitem):
    #         i-=1
    #         if item[i] == item[i+1]:
    #             i-=1
    #             pass
    #         else:
    #             item[i] = dig[let.index(chr(max(newitem)))]
    #             return converter(item)



item = input()
item1 = [ord(i) for i in item]

print(solve(item1))


