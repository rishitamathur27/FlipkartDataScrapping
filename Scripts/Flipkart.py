from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url= 'https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers= page_soup.findAll("div", {"class": "_3O0U0u"})
#print(len(containers))

#print(soup.prettify(containers[0]))
container=containers[0]

#print(container.div.img["alt"])

price = container.findAll("div", {"class":"_1uv9Cb"})
#print(price[0].text)

rating = container.findAll("div", {"class":"niH0FQ _36Fcw_"})
#print(rating[0].text)

filename= "productss.csv"
f= open(filename, "w")

headers="Product_Name, Pricing, Ratings\n"
f.write(headers)

for container in containers:
    prod_name= container.div.img["alt"]

    price_container = container.findAll("div", {"class":"_1uv9Cb"})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div", {"class":"niH0FQ _36Fcw_"})
    rating = rating_container[0].text

    print("Product_Name:" + prod_name)
    print("Price:" +price)
    print("Ratings:" +rating)

    f.write(prod_name+ " , " + price + " , " + rating+ "\n" )
f.close()












