# num = int(input())
# # if num <= 2:
# #      print(1)
# # else:
# #      print(round(num/2))

# def converter(num: int)-> int:
#     caseBCD = {
#         1: '0001',
#         2: '0010',
#         3: '0011',
#         4: '0100',
#         5: '0101',
#         6: '0110',
#         7: '0111',
#         8: '1000',
#         9: '1001',
#         0: '0000',
#     }
#     return caseBCD.get(num)
    
# storedbcd = [converter(int(i)) for i in list(str(num))]
# for i in storedbcd:
#     print(i, end = ' ')
# # bcd = converter(num)
# # ind = bcd.index('1')
# # length = 0
# # while ind < 4:
# #     length+=1
# #     ind+=1
# # print(length)
