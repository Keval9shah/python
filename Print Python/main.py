import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.flipkart.com/acer-swift-3-core-i5-8th-gen-8-gb-512-gb-ssd-windows-10-home-2-graphics-sf314-55g-thin-light-laptop/p/itmfhkkhgg2yvgzy?pid=COMFHKKHVGHUBYHW&lid=LSTCOMFHKKHVGHUBYHWZINLQQ&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=0cbf3e23-399c-43ba-b726-6a13086920de.COMFHKKHVGHUBYHW.SEARCH&ppt=sp&ppn=sp&ssid=4jwgt3bsv40000001578944921672&qH=7af2cda50a9e9b53'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


def check():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title = soup.find("class": "._35KyD6").get_text()
    title = soup.find("span", {"class": "_35KyD6"}).get_text()
    # title = soup.select('._35KyD6').get_text()

    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
    price = int(price[1:3] + price[4:7])
    print(title)

    if price < 47000:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('skeval904@gmail.com', 'tpzenvjazkwkoqoa')

    subject = 'Laptop sastu thai gayu'
    body = 'Aa rahi link \n https://www.flipkart.com/acer-swift-3-core-i5-8th-gen-8-gb-512-gb-ssd-windows-10-home-2-graphics-sf314-55g-thin-light-laptop/p/itmfhkkhgg2yvgzy?pid=COMFHKKHVGHUBYHW&lid=LSTCOMFHKKHVGHUBYHWZINLQQ&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=0cbf3e23-399c-43ba-b726-6a13086920de.COMFHKKHVGHUBYHW.SEARCH&ppt=sp&ppn=sp&ssid=4jwgt3bsv40000001578944921672&qH=7af2cda50a9e9b53'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'skeval904@gmail.com',
        'skeval904@gmail.com',
        msg
    )
    print('Email mokli didho')
    server.quit()


check()
