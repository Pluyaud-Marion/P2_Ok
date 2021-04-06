import requests
from bs4 import BeautifulSoup
import urllib

url = 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'
reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'lxml')
    product_page_url = url
    tds = soup.findAll('td') #liste des 7 tds
    #print(tds)
    #0 : upc
    #2 : including tax
    #3 : excluding tax
    #5 : stocks
    title = soup.find('h1')
    product_description = soup.find('article', {'class' : 'product_page'}).findAll('p')
    category = soup.find('ul', {'class' : 'breadcrumb'}).findAll('li')
    review_rating = soup.find('p', {'class' : 'star-rating'})
    #print(review_rating['class'][1])
    image_url= soup.find('div',{'class' : 'item active'}).find('img')
    #print('http://books.toscrape.com/' + image_url['src'][6:])

    informations = ("product_page_url : " + url + "upc : " + tds[0].text + " , title : " + title.text + " , price_including_tax : " + tds[2].text +" , price_excluding_tax : " + tds[3].text + " , number_available : " + tds[5].text + " , product_description : " + product_description[3].text + ", category : " + category[2].text + ", review_rating : " + review_rating['class'][1] + " , image_url : " + 'http://books.toscrape.com/' + image_url['src'][6:])

    print(informations)