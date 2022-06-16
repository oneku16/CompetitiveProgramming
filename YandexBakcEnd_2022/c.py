###############################
#       author: Elnazar       #
#  created: 16/06/2022 14:55  #
###############################

# libs
from sys import stdin, stdout
from collections import defaultdict, Counter
from json import dumps, loads
# import multiprocessing, time
# from typing import List
# import itertools 
# import threading
# import queue
# from math import inf, gcd
# import heapq


# my stdio 
str_stdin = lambda: stdin.readline()[:-1]
strs_stdin = lambda: list(map(str, stdin.readline()[:-1].split()))
int_stdin = lambda: int(stdin.readline())
ints_stdin = lambda: list(map(int, stdin.readline().split()))


def output(val):
    if type(val) is list:
        length = len(val) 
        for elem in range(length): stdout.write(f"{val[elem]}" + " \n"[(length - 1) == elem])
    else: stdout.write(f"{val}\n")


def day_to_str(date: str):
        date = list(date.split('.'))
        return f'{date[-1]}.{date[1]}.{date[0]}'


def filter_item(my_json: dict):
    return (filters["NAME_CONTAINS"].lower() in my_json["name"].lower()) and (filters["PRICE_GREATER_THAN"] <= my_json["price"] <= filters["PRICE_LESS_THAN"]) and (filters["DATE_AFTER"] <= day_to_str(my_json["date"]) <= filters["DATE_BEFORE"])


def solve():
    
    with open("input.txt") as file: lines = file.readlines()

    my_json = loads(lines[0])
    global filters
    filters = Counter()
    for line in lines[1:]:
        name, val = line.strip().split()
        filters[name] = val

    filters["PRICE_GREATER_THAN"] = int(filters["PRICE_GREATER_THAN"])
    filters["PRICE_LESS_THAN"] = int(filters["PRICE_LESS_THAN"])
    filters["DATE_AFTER"] = day_to_str(filters["DATE_AFTER"])
    filters["DATE_BEFORE"] = day_to_str(filters["DATE_BEFORE"])

    with open("output.txt", 'w') as file: file.write(dumps(sorted(filter(filter_item, my_json), key = lambda item: item['id'])))


if __name__ == "__main__": solve()
