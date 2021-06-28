import os
os.system('pip install requests')
import requests, re
print ('''

 ███████████                              █████               █████ █████           ████            ███   █████   
░░███░░░░░███                            ░░███               ░░███ ░░███           ░░███           ░░░   ░░███    
 ░███    ░███  █████  █████ ████  ██████  ░███████    ██████  ░░███ ███   ████████  ░███   ██████  ████  ███████  
 ░██████████  ███░░  ░░███ ░███  ███░░███ ░███░░███  ███░░███  ░░█████   ░░███░░███ ░███  ███░░███░░███ ░░░███░   
 ░███░░░░░░  ░░█████  ░███ ░███ ░███ ░░░  ░███ ░███ ░███ ░███   ███░███   ░███ ░███ ░███ ░███ ░███ ░███   ░███    
 ░███         ░░░░███ ░███ ░███ ░███  ███ ░███ ░███ ░███ ░███  ███ ░░███  ░███ ░███ ░███ ░███ ░███ ░███   ░███ ███
 █████        ██████  ░░███████ ░░██████  ████ █████░░██████  █████ █████ ░███████  █████░░██████  █████  ░░█████ 
░░░░░        ░░░░░░    ░░░░░███  ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░░░  ░███░░░  ░░░░░  ░░░░░░  ░░░░░    ░░░░░  
                       ███ ░███   Code by Shirgil & GHz7                  ░███                                    
                      ░░█████ [github: https://github.com/psychoxploit]  █████                                   
                       ░░░░░░                                            ░░░░░   

''')
r = requests.session()
def memek(kontol):
    for keyword in kontol:
        keyword = keyword.strip()
        result = open('wd.txt', 'r').read().splitlines()
        for res in result:
            res = res.strip()
            results = keyword+' \t'+res
            print(results)
            with open('Dork.txt','a+') as xn:
                xn.write(results+'\n')

if __name__ == "__main__":
	try:
		xnx = open(input('list:'),'r',encoding='utf-8').read().splitlines()
		memek(xnx)
	except Exception as w:
		print(w)

input("ALL DONE")