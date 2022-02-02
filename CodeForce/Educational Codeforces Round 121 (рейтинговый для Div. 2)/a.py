from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    
    letters = [' '] + list(stdin.readline())
    letters.pop()
    stdout.write(str(letters) + '\n')

    new_letters = [' ' for i in range(len(letters) + 1)]
    for i in range(1, len(letters) - 1):
        new_letters[i + 2] = letters[i]
    stdout.write(str(new_letters) + '\n') 


        








