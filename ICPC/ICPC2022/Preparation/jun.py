ans1=[]
ans2=[]
with open('input.txt', 'r') as f:
    for line in f.readlines():
        a, b, c = map(int, line.split())
        ans=0
        if a == 0 and b == 0 and c == 0:    #for single solution
            ans=1
        elif a > 0:                         #for z no solution
            ans=0
        elif c > 0:                         #for x no solution
            ans=0
        elif c == 0 and a != 0 and b != 0:
            ans=0
        elif b - a > 0:                     #for y no solution
            ans=0

        elif a == 0 and b == 0 and c < 0:   #for x
            ans=2
        elif a < 0 and a == b and c == 0:   #for z
            ans=2
        elif a == 0 and b < 0 and c == 0:   #for y
            ans=2
        elif a == 0 and b < 0 and c < 0:    #for x,y
            ans=4
        elif 0 > a == b < 0:                #for x,z
            ans=4
        elif a ** 2 * (a - b) + c == 0:      #for z,y
            ans=4
        else:
            ans=8
        ans1.append(ans)

        def solve(A,B,C):
        
            Z , X , Y = 0,0,0
            if A > 0:
                return 0
            elif A == 0:
                Z = 1
            else:
                Z = 2

            if a < 0 and c < 0 and a!=b:
                return 8

            if A-B > 0:
                Y = 2
            elif A-B == 0:
                Y = 1
            else:
                # print("y")
                return 0


            if -((A*A)*((A-B)*(A-B))) - C > 0:
                X = 2
            elif -((A*A)*((-B+A)*(-B+A))) - C == 0:
                X = 1
            else:
                # print("x")
                return 0
            return X*Y*Z
        A,B,C =map(int, line.split())
        ans=solve(A=A,B=B,C=C)
        ans2.append(ans)

for i in range(1_000):
    if ans1[i]!=ans2[i]:
        print(f'{i+1}:->J{ans1[i]}>-<S{ans2[i]}')
# with open('output2.txt', 'a') as hh:
#     for val in anss:
#         hh.write(f'{val}')
