from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


uClient =  uReq("https://www.iposcoop.com/last-100-ipos/")
page_html = uClient.read()
uClient.close()
file = "companies_5.csv"
f = open(file,"w")
headers = "Name, Symbol, Industry, Initial_Offer_Date, Shares_in_Millions, Intial_Offer\n"
f.write(headers)

page_soup = soup(page_html,"html.parser")

container = page_soup.find_all("tr")
for j in range(1,len(container)):
    contain =container[j].find_all("td")
    Name = contain[0].a.string
    Symbol = contain[1].a.string
    Industry = contain[2].a.string
    intial_offer_date=""
    for i in range(9, 19):
        intial_offer_date= intial_offer_date+ contain[3].string[i]
        if(i==18):
            print(" ")



    Shares_in_milli =contain[4].string
    intial_offer = contain[5].string
    f.write(Name+","+Symbol+","+Industry+","+intial_offer_date+","+Shares_in_milli+","+intial_offer+"\n")

    print("")
    #print(contain[0].a.string)
"""
for i in range(0,len(contain)):
    print(contain[i].a.string)
"""