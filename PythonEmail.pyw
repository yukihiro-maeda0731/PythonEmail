import smtplib, ssl
import requests
from bs4 import BeautifulSoup

def read_creds():
    user = passw = ""
    with open("credentials.txt", "r", encoding="utf-8") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw

def check_inventory():
    url = "https://www.pokemoncenter-online.com/?p_cd=4521329322735"
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c.decode("CP932"), "lxml")
    all=soup.find_all("div",{"class":"detail"})
    print(c)
    inventory_existence_flg = False
    return inventory_existence_flg


port = 465

sender, password = read_creds()

receiver = sender

message = """\
Subject: Inventory Notification

We have new inventory.

"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    if(check_inventory()):
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("メールを送信しました")