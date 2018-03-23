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


