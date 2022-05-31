from typing import List


parameters = list(map(int, input().split()))
parameters.sort()
parameters.reverse()
a, b, c = parameters[0], parameters[1], parameters[-1]



oside = 2*(a-2)*(b-2)+2*(a-2)*(c-2)+2*(b-2)*(c-2)


two = 4* (a-4) if [a-4>=0] is True else 0# + 4 * sum([b-4>=0]) + 4* sum([c-4>=0])

print(two)

# matrix = [[['x' for j in range(a)] for i in range (b)] for k in range (c)]

# matrix[0][0][0] = ' '
# matrix[0][0][-1] = ' '
# matrix[0][-1][0] = ' '
# matrix[0][-1][-1] = ' '

# matrix[-1][0][0] = ' '
# matrix[-1][0][-1] = ' '
# matrix[-1][-1][0] = ' '
# matrix[-1][-1][-1] = ' '

# for i in range (len(matrix)):
#     for j in range (len(matrix[i])):
#         for k in range (len(matrix[i][j])):
#             print(matrix[i][j][k], end = " ")
#         print()
#     print()

# indexes = []
# for i in range (len(matrix)):
#     for j in range (len(matrix[i])):
#         for k in range(len(matrix[i][j])):
#             if matrix[i][j][k] == ' ':
#                 indexes.append([i,j,k])



# for row in indexes:
#     for i in row:
#         pass 
         

# t = 0
# while i < len(matrix)-1:
#     j = 0
#     while j < len(matrix[i])-1:
#         k = 0 
#         while k < len(matrix[i][j])-1:
#             if matrix[i-1][j-1][k-1] == ' ' or matrix[i-1][-j][k-1] == ' ':
#                 print(i,j,k)
#                 t+=1
#             k += 1
#         j +=1
#     i+=1


# print(t)




# for i in range (len(matrix)):
#     for j in range (len(matrix[i])):
#         for k in range(len(matrix[i][j])):
#             if i == 0 and j == 0 and k == 0:
#                 matrix[i][k][k] = ' '

# for main in matrix:
#     for row in main:
#         print(row)


# def countzero(parameters: List[int])-> int:
#     if 1 in parameters or 2 in parameters:
#         return 0
#     else:
#         for i in range(len(parameters)):
#             parameters[i] = parameters[i]-2
#         producat = 1
#         for nums in parameters:
#             producat *= nums
#         return producat

# def countone(parameters: List[int])-> int:
#     if 1 in parameters:
#         return 0
#     elif 2 in parameters:
#         for i in range(len(parameters)):
#             parameters[i] = parameters[i]-2
#         a, b, c = parameters[0], parameters[1], parameters[-1]
#         return 2*(a*b)
        
#     else:
#         for i in range(len(parameters)):
#             parameters[i] = parameters[i]-2
#         a, b, c = parameters[0], parameters[1], parameters[-1]
#         return 2*(a*b + a*c + b*c)

# def counttwo(parameters: List[int])-> int:
    
#     if 1 in parameters:
#         for i in range(len(parameters)):
#             parameters[i] = parameters[i]-2
#         a, b, c = parameters[0], parameters[1], parameters[-1]
#         return a*b
#     elif parameters[-1] and max(parameters)-4>=1:
#         a, b, c = parameters[0], parameters[1], parameters[-1]
#         return (a-4)*4
#     elif min(parameters) - 4>=0 and max(parameters) - 4>= 0:
#         pass

        

        
    

# print(countone(parameters))





