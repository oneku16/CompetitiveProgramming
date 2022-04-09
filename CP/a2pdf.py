from typing import List

def solve(itemn: List[int])->str:

    def converter(asciinums: List[int])-> str:
        answer = ""
        for nums in asciinums:
            answer += chr(nums)
        return answer 

    nums = [65, 80, 81]
    if itemn[-1] == max(itemn) and itemn.count(itemn[-1]) != len(itemn):
        i = len(itemn) - 1
        max_elem = max(itemn)
        while itemn[i] == max_elem:
            if itemn[i] == 81:
                itemn[i] = 65
                i-=1
            elif itemn[i] == 80:
                itemn[i] = 65
                i-=1
        itemn[i] = nums[nums.index(itemn[i]) + 1]
        return converter(itemn)

    elif itemn.count(itemn[-1]) == len(itemn):
        itemn[-1] = nums[nums.index(itemn[-1])+1]
        return converter(itemn) 
    
    elif itemn[-1] != max(itemn):
        itemn[-1] = nums[nums.index(itemn[-1])+1]
        return converter(itemn)





item = input()
itemn = [ord(i) for i in item]



print(solve(itemn))
