from operator import length_hint
from sys import stdin, stdout


for _ in range(int(stdin.readline())):

    characters = [0] + list(stdin.readline())
    characters.pop()
    length = len(characters)
    cnt = 0
    
    i = 1
    while i < length:
        for j in range(i, length):
            print('i: ', i)
            if characters[i] == characters[j]:
                i += j
                print(i)
                cnt += i - j - 2
                print('end p: ', i, cnt)
                break
       
        i+=1
        
    print(cnt)

    # i = 1
    # while i <= 
    # i = 1
    # while i <= length:
    #     for j in range(i + 1, length):
    #         if characters[i] != characters[j]: 
    #             cnt += 1
    #         elif characters[i] == characters[j]:
    #             i += j
    #             break
    #         else: 
    #             i += 1
    #             cnt += 1
    # print(cnt)

