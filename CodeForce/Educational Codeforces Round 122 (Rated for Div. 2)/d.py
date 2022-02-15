from sys import stdin, stdout


def equal(num: int, goal: int, k) -> int:
    cnt = 0
    if num == goal: return cnt
    else:
        while k > 0 or num != goal:
            if num/num + num <= goal: num += num/num
            
    return cnt


for _ in range(int(stdin.readline())):

    n, k = map(int, stdin.readline().split())

    b = [0] + list(map(int, stdin.readline().split()))
    c = [0] + list(map(int, stdin.readline().split()))

    w = []

    
