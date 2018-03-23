import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_lockerbie.settings')


import django
django.setup()

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

from project_lockerbieapp.models import Symbol_record, Price

with open('companies_5.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

#print(your_list[1][1])

for i in range(1,100):
  uClient =  uReq("https://finance.yahoo.com/quote/"+your_list[i][1])
  page_html = uClient.read()
  uClient.close()
  page_soup = soup(page_html,"html.parser")

  time = time.strftime("%c")
  webpprice = page_soup.find_all("span")

  stored_price = Price.objects.get_or_create(stockprice=webpprice[17].text ,Time=time)
  stockinfo = Symbol_record.objects.get_of_create(sPrice= webpprice, Name=your_list[i][1])








"""""
topics = ["Search","Social","MarketPlcae"]

def add_topic():
    t = Topic.objects.get_or_create(Topic_Name=random.choice(topics))[0]
    t.save()
    return t

def populate(N = 3):
    for entry in range(N):
        top = add_topic()
        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()

        webpg = Webpage.objects.get_or_create(topics =top,url=fake_url,name= fake_name)[0]

        acc_recs = AcessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(20)
    print("Populating complete")
"""
