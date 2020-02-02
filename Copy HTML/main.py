import requests
from bs4 import BeautifulSoup
# import smtplib
import pyperclip

URL = input("Enter URL : ")

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
pyperclip.copy(soup.prettify())
print("Done, Copied to Clipboard")
    
