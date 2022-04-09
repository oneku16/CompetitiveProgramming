import typing


class Box:

    def __init__(self, d, w, h):
        self.h = h
        self.w = w
        self.d = d
 
    def __lt__(self, other):
        return self.d * self.w < other.d * other.w
 
def maxStackHeight(arr, n):
    rot = [Box(0, 0, 0) for _ in range(3 * n)]
    index = 0
 
    for i in range(n):
        rot[index].h = arr[i].h
        rot[index].d = max(arr[i].d, arr[i].w)
        rot[index].w = min(arr[i].d, arr[i].w)
        index += 1

        rot[index].h = arr[i].w
        rot[index].d = max(arr[i].h, arr[i].d)
        rot[index].w = min(arr[i].h, arr[i].d)
        index += 1
 
        rot[index].h = arr[i].d
        rot[index].d = max(arr[i].h, arr[i].w)
        rot[index].w = min(arr[i].h, arr[i].w)
        index += 1
 
    n *= 3
 
    # rot.sort(reverse = True)

    msh = [0] * n
 
    for i in range(n):
        msh[i] = rot[i].h
 
    for i in range(1, n):
        for j in range(0, i):
            if (rot[i].w < rot[j].w and rot[i].d < rot[j].d):
                if msh[i] < msh[j] + rot[i].h:
                    msh[i] = msh[j] + rot[i].h
 
    maxm = -1
    for i in range(n):
        maxm = max(maxm, msh[i])
 
    return maxm
 


arr2 = []
for i in range(int(input())):
    a, b, c = map(int, input().split())
    print("parameters: ", a,b,c)
    print(type(a), type(b), type(c))
    arr2.append(Box(a,b,c))
n = len(arr2) 
print(maxStackHeight(arr2, n))

