from sys import stdin, stdout
from art import tprint
from time import localtime, strftime
import requests
from bs4 import BeautifulSoup as BS
import os


def get_id(url: str) -> str:

	req = requests.get(url) 
	source = BS(req.content, "html.parser")
	contests = source.find_all(class_ = "roundbox sidebox")[0].find("a").get("href")
	
	return contests

def get_codeforces(url = get_id("https://codeforces.com/contests")) -> str:
	
	url = "https://codeforces.com" + url
	req = requests.get(url)
	source = BS(req.content, "html.parser")
	codeforces = source.find_all("div", class_ = "datatable")[0].find_next("td").text
	return codeforces


def creat(folder_name: str):

	current_time = strftime("%d/%m/%Y %H:%M", localtime())
	user_info = f"###############################\n#        author: oneku        #\n# created at {current_time} #\n###############################\n"

	dir_path = os.path.dirname(os.path.realpath(__file__))
	folder_name = list(folder_name[2:folder_name.index(")") + 1])
	# folder_name[-2] = "2"
	folder_name = "".join(folder_name)

	folder_path  = os.path.join(dir_path + "/CodeForce", folder_name)
	files = ['a.py', 'b.py', 'c.py', 'd.py', 'e.py']
	template = os.path.join(dir_path, "template.py")

	with open (template) as file: lines = ''.join(file.readlines())
	
	try:
		os.mkdir(folder_path)
		stdout.write(f"Directory {folder_name} created\n\n")
		
		for file in files:
			file_path = os.path.join(folder_path, file)
			file = open(file_path, 'w+')
			file.write(user_info)
			file.write(lines)
			file.close()
			stdout.write(f"file {file_path} created\n")
		tprint("GOOD LUCK!")
	except FileExistsError: stdout.write(f"Directory {folder_name} already exists\n")


def main():

	tprint("CODEFORCES")
	creat(folder_name = get_codeforces())
	# creat(folder_name = "Educational Codeforces Round 135 (Rated for Div. 2)")

if __name__ == '__main__': main()