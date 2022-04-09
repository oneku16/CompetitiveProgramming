# from typing import List

# def checker(row: List[str]) -> bool:
#     odd = []
#     even = []
#     for let in row:
#         odd.append(let) if row.count(let) % 2 == 1 else even.append(let)
#     pal = ""
#     pal = pal + "".join(even[i] for i in range (1, len(even), 2))
#     if any(odd) is True:
#         pal = pal+ "".join(odd) 
#     pal = pal+ "".join(even[i] for i in range (len(even)-1, -1, -2))
#     length = int(len(pal)/2) 
#     ls = "".join([pal[i] for i in range(length)])
#     rs = "".join(pal[len(pal)-1-i] for i in range(length))
#     return True if ls == rs else False

# n, m = map(int, input().split())
# matrix = [[chr(k) for k in sorted([ord(j) for j in list(input().strip())])] for i in range (n)]

# for i in range (m):
#     row = []
#     for j in range (n):
#         row.append(matrix[j][i])
#     matrix.append(row)

# # for row in matrix:
# #     print(row)

# check = []
# for row in matrix:
#     check.append("Yes") if checker(row) is True else check.append("")

# print("Yes" if all(check) is True else "No")




#Substring
# s1 = (input().strip())
# s2 = (input().strip())

# try:
#     ind = s2.index(s1)
#     print (ind)
# except BaseException:
#     print(-1)




#33

# m, n = map(int, input().split())




# mp, np = m**3, n**3

# print(mp, np)






#dots



# dots = list(map(int, input().split()))
# coor = []

# i = 0
# while i <= 6:
#     coor.append([dots[i], dots[i+1]])
#     i+=2

# def dis(x1, y1, x2, y2):
#     return ((x2-x1)**2+(y2-y1)**2)**0.5

# diss = []
# diss.append(dis(coor[0][0], coor[0][1], coor[1][0], coor[1][1]))
# diss.append(dis(coor[0][0], coor[0][1], coor[2][0], coor[2][1]))
# diss.append(dis(coor[0][0], coor[0][1], coor[3][0], coor[3][1]))
# diss.append(dis(coor[1][0], coor[1][1], coor[2][0], coor[2][1]))
# diss.append(dis(coor[1][0], coor[1][1], coor[3][0], coor[3][1]))
# diss.append(dis(coor[2][0], coor[2][1], coor[3][0], coor[3][1]))

# diss.sort()

# trash = diss
# def line(trash)-> bool:
#     check = []
#     if trash.count(max(trash)) == 1 and trash.count(min(trash)) == 1 and trash[1] == trash[2] and trash[-2] == trash[-3]:
#         check.append(True)
#     elif trash.count(max(trash)) == 1 and trash.count(min(trash)) == 2 and trash[-2] == trash[-3] and trash.count(trash[2]) == 1:
#         check.append(True)
#     elif trash.count(max(trash)) == 1 and trash.count(min(trash)) == 3 and trash[-2] == trash[-3]:
#         check.append(True)
#     else:
#         check.append(None)

#     return any(check)

# def trap(trash)-> bool:
#     check = []
#     if trash.count(min(trash)) == 1 and trash.count(max(trash)) == 1 and trash[-2] == trash[-3] and trash[1] == trash[2]:
#         check.append(True)
#     elif trash.count(min(trash)) == 2 and trash.count(max(trash)) == 1 and trash[-2] == trash[-3] and trash.count(trash[2]) == 1:
#         check.append(True)
#     elif trash.count(max(trash)) == 2 and trash[-3] == trash[-4]:
#         check.append(True)
#     else:
#         check.append(None)
#     return any(check)
# if trap(trash) is True or line(trash) is True:
#     print(2) 
# else:
#     print(3)




    
    




