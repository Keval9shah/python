import requests
from bs4 import BeautifulSoup
import smtplib


URL = input("Enter URL : ")

Email = input("Enter your Email : ")

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.117 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# title = soup.find("class": "._35KyD6").get_text()
title = soup.find("span", {"class": "_35KyD6"}).get_text()
# title = soup.select('._35KyD6').get_text()
print(title)
pr = input('Enter price to compare : ')
pr = int(pr)
print(type(pr))

price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
price = price.replace(',','')
price = int(price[1:])
print(price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #key is encrypted by simple pass
    server.login('skeval904@gmail.com', 'p{ousmxrpxk{cmcg')

    subject = 'Test mail'
    body = 'Aa rahi link \n'+URL+'\n'+str(price)
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'skeval904@gmail.com',
        Email,
        msg
    )
    print("Email has been sent")
    server.quit()


if price < pr:
   send_mail()
