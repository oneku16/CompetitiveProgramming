from sys import stdin, stdout
# from math import inf
# # from copy import deepcopy as dc




# n, l, k = map(int, stdin.readline().split())


# dis = list(map(int, stdin.readline().split()))
# speed = list(map(int, stdin.readline().split()))

# for i in range(n-2):
#     dis[i] = dis[i+1] - dis[i]
# dis[-1] = l - dis[-1]
# for i in range(k):dis[dis.index(min(dis))] = inf
# dis[0] = 0

# stdout.write(str(dis))

# diss = []
# i = 0
# ind = dis.index(min(dis)) + 1
# for i in range(n - k):
#     while True:
#         if dis[ind] != inf:
#             diss.append(dis[ind] - dis[i])
#             i = ind
#             dis.remove(dis[i])
#             ind = dis.index(min(dis)) + 1
# print(diss)
# cnt = 0
# for i in range(n):
#     if dis[i] == inf: pass
#     else:

#         cnt += dis[i] * speed[i]

# stdout.write(str(cnt))


# # for _ in range(int(stdin.readline())):

# #     n = int(stdin.readline())
# #     nums = list(map(int, stdin.readline().split()))
# #     nums2 = dc(nums)
# #     numset = set(nums)
# #     print(numset)
    

























# a, b = map(int, stdin.readline().split())
# matrix = [[0 for i in range (b+1)] for j in range(a+1)]
# matrix[1][1] = 1

# for row in matrix: stdout.write(str(row)+'\n')
# stdout.write('\n')
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         matrix[i][j] += matrix[i-1][j] + matrix[i][j-1]

# for row in matrix: stdout.write(str(row)+'\n')
# stdout.write(str(matrix[a][b])+'\n')



a, b = map(int, stdin.readline().split())
matrix = [[0 for i in range (b+1)] for j in range(a+1)]
matrix[1][1] = 1

for row in matrix: stdout.write(str(row)+'\n')
stdout.write('\n')
for i in range(1, a+1):
    for j in range(1, b+1):
        matrix[i][j] += matrix[i-1][j] + matrix[i][j-1]

for row in matrix: stdout.write(str(row)+'\n')
stdout.write(str(matrix[a][b])+'\n')



