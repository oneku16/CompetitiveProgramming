

# # n = int(input())
# # nums = list(map(int, input().split()))

# # i = 0
# # j = 5
# # c = 0
# # while j <= len(nums):
# #     c2 = 0
# #     maxdeath = []
# #     for k in range (i, j):
# #         maxdeath.append(nums[k])
    
# #     print(maxdeath)
# #     indmax = maxdeath.index(max(maxdeath))
# #     if indmax == j:
# #         maxdeath.pop(indmax)
# #         maxdeath.pop(indmax-1)
# #         print(maxdeath)
# #         c2+=2
# #     elif indmax == i:
# #         maxdeath.pop(indmax)
# #         maxdeath.pop(indmax+1)
# #         print(maxdeath)
# #         c2+=2
# #     else:
# #         maxdeath.pop(indmax)
# #         maxdeath.pop(indmax+1)
# #         maxdeath.pop(indmax-1)
# #         print(maxdeath)
# #     j+=1
# #     i+=1

# # print(maxdeath)

# import math

# n, m = map(int, input().split())

# a = (n*m)
# b = (m-n)
# if (a/b) - int(a/b) == 0:
#     print(str(int(a/b))+'/1')
# else:
#     gcd1 = math.gcd(a,b)
#     a = a/gcd1
#     b = b/gcd1
#     print(str(int(a))+'/'+str(int(b)))


# main = []
# for i in range (int(input())):
#     main.append(list(map(int, input().split())))


# rotated = []
# for i in range(len(main)):
#     row = []
#     for j in range((main[i][-1][])):
#         row.append([j][i])
# print(main)

