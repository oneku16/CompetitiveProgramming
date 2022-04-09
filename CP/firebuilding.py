n = int(input())

bu = []

maxvalue = 0
for i in range (n):
    row = list(map(int, input().strip().split(" ")))
    if row[0] > maxvalue:
        maxvalue = row[0]
    bu.append(row)

# print(maxvalue)
# print("output:")
# for row in bu:
#     print(row)

matrix = []

for i in range (len(bu)):
    row = []
    for j in range(bu[i][-1]*bu[i][0]):
        row.append('X')
    matrix.append(row)
# matrix.sort()
# matrix.reverse()


for row in bu:
    print(row)
for row in matrix:
    print(*row)


# c = 0
# for i in range (len(bu)):
#     for j in range (len(bu[-1])):
#         if matrix[i][j] == matrix[i][len(bu[0])-1-j]:
#             c+=1

# print(c) 



