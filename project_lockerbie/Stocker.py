from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

with open('companies_5.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

#print(your_list[1][1])

for i in range(1,100):
  uClient =  uReq("https://finance.yahoo.com/quote/"+your_list[i][1])
  page_html = uClient.read()
  uClient.close()
  page_soup = soup(page_html,"html.parser")

  price = page_soup.find_all("span")

  print(price[17].text)


#-------------------------------





#print(container[0])


"""
file = "companies_5.csv"
f = open(file,"w")
headers = "Name, Symbol, Industry, Initial_Offer_Date, Shares_in_Millions, Intial_Offer\n"
f.write(headers)
"""