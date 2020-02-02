import requests
from bs4 import BeautifulSoup
import os.path
from os import path

URL = input("Enter site to copy : \n")

t = [l for l in URL.split("://")]
y = [l for l in t[1].split("www.")]
if len(y) == 2:
    z = [x for x in y[1].split("/")]
elif len(y) == 1:
    z = [x for x in y[0].split("/")]
y = [x + '.' for x in z[0].split(".")]
y[-1] = ''
y[-2] = y[-2][:-1]
n = ''.join(y)

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

save_path = "C:/Users/KEVAL/Desktop/Charm/"
completeName = os.path.join(save_path, n+".html")

c = 0
while path.exists(completeName):
    c = c+1
    n = n+"("+str(c)+")"
    completeName = os.path.join(save_path, n + ".html")

file = open(completeName, "w", encoding="utf-8")
file.write(soup.prettify())
file.close()

print("\n\nhtml file   "+n+".html   created at "+completeName+"\n\n")
