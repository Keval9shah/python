import requests
from bs4 import BeautifulSoup
import os.path

URL = input("Enter site to copy : ")

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

save_path = "C:/Users/KEVAL/Desktop/Charm/"

name_of_file = input("What is the name of the file: ")

completeName = os.path.join(save_path, name_of_file+".html")

file = open(completeName, "w", encoding="utf-8")

file.write(soup.prettify())

file.close()

print("html file "+name_of_file+".html created at "+completeName)
