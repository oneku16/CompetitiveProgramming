from sys import stdin
import math


for _ in range(int(stdin.readline())):


    n = int(stdin.readline())
    
    c = 1
    d = 1

    if n % 2 == 0:

        n -= 2

        a = n // 2
        b = n // 2

        while math.gcd(a,b) != 1:

            a -= 1
            b += 1
    else:
        n -= 2

        a = math.ceil(n/2)
        b = math.floor(n/2)
        while math.gcd(a,b) != 1:

            a -= 1
            b += 1
        


    print(a,b,c,d)

    

