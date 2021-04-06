import requests
from bs4 import BeautifulSoup
from math import *
import webbrowser
from fonction_scrapping_one_book import scrapping_one_book, scrapping_one_category

#url_category = "http://books.toscrape.com/catalogue/category/books/travel_2/"
#url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/"
#url_category = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/"
url_category = "http://books.toscrape.com/catalogue/category/books/classics_6/"

#input("tapez l'url d'une catégorie : ")
response = requests.get(url_category)
if response.ok:
    links = scrapping_one_category(url_category) #la fonction scrapping_one_category retourne une liste. links est une variable dans laquelle je mets le résultat de la fonction
    #je passe en paramètre l'url de ma catégorie. la fonction utilise ce paramètre pour faire la requete.get
    print(links)
#links affiche les liens de tous les livres de la catégorie

for link in links: #boucle for : je cherche dans les liens
    book_info = scrapping_one_book(link) #j'appelle la première fonction(les infos du livre)
    #print(book_info)
    with open ('infos_all_livres.csv', 'w') as file:
        file.write('product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
        file.write(str(book_info))

  

###DOIT FAIRE AFFICHER TOUTES LES INFOS DE TOUS LES LIVRES DANS LE FICHIER CSV###




    


