from statistics import median_low as mdl, median_high as mdh, median as md
from copy import deepcopy as dc
num = int(input())
floors = list(map(int, input().split()))
newfloor = dc(floors)
newfloor.sort()

if len(floors)%2==0:
    medl = mdl(newfloor)
    medh = mdh(newfloor)
    midmed = md(newfloor)
    ind = min([floors.index(medl), floors.index(medh)])

    if floors.index(medl) == floors.index(medh):
        print(floors.index(midmed)+1)
    else:
        print(ind+1)
else:
    midmed = md(newfloor)
    print(floors.index(midmed)+1)
