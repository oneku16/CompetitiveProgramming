n = int(input())
bu = []
for i in range (n):
    row = list(map(int, input().strip().split(" ")))
    bu.append(row)
sund  = []
for i in bu:
    sund.append(i[0]*i[-1])
summm = sum(sund)
xx = [i[0] for i in bu]
summmmx = sum(xx)
answer = (summm/summmmx)
print(format(answer, ".3f"))









# minn = bu[0][0]*(bu[0][-1]-answer)**2
# qwe = []
# for i in bu:
#     if i[0]*(i[-1]-answer)**2 >= minn:
#         minn = i[0]*(i[-1]-answer)**2
#         qwe.append(minn)

# print("%.3f" % minn)

# print(sum(qwe))


    
