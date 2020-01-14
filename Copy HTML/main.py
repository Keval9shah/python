import requests
from bs4 import BeautifulSoup
# import smtplib
import pyperclip

URL = input("Enter URL : ")

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


def check():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find("class": "._35KyD6").get_text()
    # title = soup.find("span", {"class": "_35KyD6"}).get_text()
    # title = soup.select('._35KyD6').get_text()

    # price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
    # price = int(price[1:3] + price[4:7])
    # print(title)
    pyperclip.copy(soup.prettify())
    print("Done, Copied to Clipboard")
check()
