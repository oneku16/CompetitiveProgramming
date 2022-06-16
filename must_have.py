# prime checker
def is_prime(number):
    
    if number == 2: return True
    if number % 2 == 0: return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0: return False 
    return True

# bubble sort
def bubble_sort(a):
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1] :
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Binary exponentiation
def bin_pow(num = int, power = int) -> int:

    if not power: return 1
    if power % 2: return bin_pow(num, power - 1) * num
    else:
        num_b = bin_pow(num, power / 2)
        return num_b * num_b 

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def bfs(): pass


def dfs(): pass 