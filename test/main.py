from os import (walk,path,mkdir)
# dir_path=path.dirname(path.realpath(__file__))
# print(dir_path)
folder='CSES'
dirPath= path.join('D:/Programming/CompetitiveProgramming',folder)

if path.isdir(dirPath):
	try:
		mkdir(folder)
		print('created')
	except FileExistsError:
		raise FileExistsError('exists')
else:
	print('exists')



