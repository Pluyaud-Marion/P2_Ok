import requests
from bs4 import BeautifulSoup
from math import *

url = 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'

def scrapping_one_book(url_dun_livre):
    response = requests.get(url_dun_livre)   
    if response.ok:
        soup = BeautifulSoup(response.text,'lxml')
        product_page_url = url_dun_livre #le paramètre de ma fonction
        title = soup.find('h1')
        tds = soup.findAll('td') #liste des 7 tds
        universal_product_code = tds[0].text
        price_excluding_tax = tds[2].text
        price_including_tax = tds[3].text
        number_available = tds[5].text
        image= soup.find('div',{'class' : 'item active'}).find('img')
        image_url = 'http://books.toscrape.com/'+ image['src'][6:]
        rating = soup.find('p', {'class' : 'star-rating'})
        review_rating = rating['class'][1]
        category_find = soup.find('ul', {'class' : 'breadcrumb'}).findAll('li')
        category = category_find[2].text
        description = soup.find('article', {'class' : 'product_page'}).findAll('p')
        product_description = description[3].text
        
      
        book_info = {
            'product_page_url': product_page_url, #problème sur les urls. affiche toujours la même
            'universal_product_code(upc)': universal_product_code,
            'title': title.text,
            'price_including_tax': price_including_tax,
            'price_excluding_tax': price_excluding_tax,
            'product_description': product_description,
            'category': category,
            'review_rating': review_rating,
            'image_url':  image_url            
            }
            #dictionnaire créé avec toutes les infos d'un livre
    return book_info

#url_category = "http://books.toscrape.com/catalogue/category/books/travel_2/"
#url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/"
#url_category ="http://books.toscrape.com/catalogue/category/books/historical-fiction_4/"
url_category = "http://books.toscrape.com/catalogue/category/books/classics_6/"

def scrapping_one_category(urls_all_book_category): 
    response = requests.get(urls_all_book_category)#requete ds les urls de la catégorie
    links = []
    soup = BeautifulSoup(response.text, 'lxml')
    nombre_livres = soup.find('form', {'class' : 'form-horizontal'}).find('strong')
    nombre_pages = ceil(int(nombre_livres.text) / int(20))
    categorie = soup.find('div', {'class' : 'page-header action'}).find('h1') #récupère nom de la catégorie

    if nombre_pages > 1:
        for i in range(1, nombre_pages+1):
            url_pages= url_category + 'page-' + str(i) + '.html' #pour que ça parcourt toutes les pages
            response = requests.get(url_pages)
            if response.ok:
                soup = BeautifulSoup(response.text,'lxml')
                #categorie = soup.find('div', {'class' : 'page-header action'}).find('h1') #récupère nom de la catégorie
                livre = soup.findAll('article')
                for article in livre:
                    a = article.find('a')
                    link = a['href'] #donne les urls incomplètes
                    links.append('http://books.toscrape.com/catalogue/' + link[9:]) #complète l'url
            

    else: 
        url_une_page = url_category + 'index.html'
        response = requests.get(url_une_page)
        if response.ok:
            soup = BeautifulSoup(response.text,'lxml')
            categorie = soup.find('div', {'class' : 'page-header action'}).find('h1') #récupère nom de la catégorie
            livre = soup.findAll('article')
            for article in livre:
                a = article.find('a')
                link = a['href']
                links.append('http://books.toscrape.com/catalogue/' + link[9:])
        return links


