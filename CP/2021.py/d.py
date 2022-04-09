import time

def main(R,x,y):
    d = (x**2+y**2)**0.5
    k = 10
    for i in range(1, 11):
        if d <= R*i/10:
            return k    
        k -= 1
        if k == 0:
            return (0)
            
R, x, y = map(int, input().split())

start_time = time.time()
print(main(R, x, y))

print("--- %s seconds ---" % (time.time() - start_time))