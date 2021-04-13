import requests
from bs4 import BeautifulSoup
from math import *
import webbrowser
import wget
import os.path
from fonction_scrapping import scrapping_one_book, scrapping_one_category, scrapping_images
os.makedirs("images_Books")
output_directory = "images_Books"

url_category = "http://books.toscrape.com/catalogue/category/books/travel_2/"
#url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/"
#url_category = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/"
#url_category = "http://books.toscrape.com/catalogue/category/books/classics_6/"


response = requests.get(url_category)
if response.ok:
    links = scrapping_one_category(url_category) #la fonction scrapping_one_category retourne une liste. links est une variable dans laquelle je mets le résultat de la fonction
    #je passe en paramètre l'url de ma catégorie. la fonction utilise ce paramètre pour faire la requete.get
    #print(links)
    soup = BeautifulSoup(response.text, 'lxml')
    categorie = soup.find('div', {'class' : 'page-header action'}).find('h1') #récupère nom de la catégorie
    #links affiche les liens de tous les livres de la catégorie

for link in links: #boucle for : je cherche dans les liens
    book_info = scrapping_one_book(link) #j'appelle la première fonction(les infos du livre)
    #print(book_info) #cherche les infos de tous les livres de la catégorie
    urls_image = scrapping_images(link)

    wget.download(urls_image, out=output_directory) #télécharge les images

    with open ("images.txt", "a+") as file: 
        file.write(urls_image + '\n') 

    with open ('infos_' + str(categorie.text) + '.csv', 'a+') as file:
        file.write('product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
        file.write(str(book_info))



 

    


