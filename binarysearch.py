from string import ascii_uppercase

num:int=int(input())
alph:list=list(ascii_uppercase)
# last:int=num%26-1
ans:str=""
while num>26:
	num//=26
	ans+='A'

if num>0:ans+=alph[num-1]

print(ans)