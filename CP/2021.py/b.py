from typing import List
from random import randint as rd
import time




# pn = int(input())
pl = list(map(int, input().split()))

# pl = [rd(10**9 - 10**5, 10**10) for i in range(10)]
# cn = int(input())
cl = list(map(int, input().split()))
d = int(input())
# cl = [rd(10**9 - 10**5, 10**10) for i in range(10)]
# d = (10**8)
# for nums in pl:
#     print(nums)

# for nums in cl:
#     print(nums)


pl.sort(reverse = True)
cl.sort(reverse = True)
print(pl)
print(cl)
def main(pl: List[int], cl: List[int], d: int)->int:

    c = 0
    if cl[-1] - pl[0] > d:
        return 0
    elif pl[-1] - cl[0] > d:
        return 0
    else:
        while any(cl):
            if abs(cl[-1] - pl[-1]) <= d:
                print(pl[-1], cl[-1])
                pl.pop()
                cl.pop()
                c+=1
            else:
                cl.pop()
                pl.pop()
    return(c)


start_time = time.time()
print(main(pl, cl, d))

print("--- %s seconds ---" % (time.time() - start_time))

