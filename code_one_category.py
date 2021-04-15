import requests
from bs4 import BeautifulSoup
from math import *
import wget
import os.path
from fonction_scrapping import scrapping_one_book, scrapping_one_category, scrapping_images
import csv
import re

url_category = input("Veuillez saisir l'url d'une catégorie : ")

#url_category = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
#url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
#url_category = "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
#url_category = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"

""" 
création du dossier Books.toscrap et modif du chemin pour y mettre les éléments + création dossier images
"""
os.mkdir("Books.toscrap")
os.chdir("Books.toscrap")
os.mkdir("Images_books_one_category")


response = requests.get(url_category)
if response.ok:
    links = scrapping_one_category(url_category) #la fonction scrapping_one_category retourne une liste. links est une variable dans laquelle je mets le résultat de la fonction
    #je passe en paramètre l'url de ma catégorie. la fonction utilise ce paramètre pour faire la requete.get
    print(links)
    soup = BeautifulSoup(response.text, 'lxml')
    categorie = soup.find('div', {'class' : 'page-header action'}).find('h1') #récupère nom de la catégorie
    #links affiche les liens de tous les livres de la catégorie

for link in links: #boucle for : je cherche dans les liens
    book_info = scrapping_one_book(link) #j'appelle la première fonction(les infos du livre)
    print(book_info) #cherche les infos de tous les livres de la catégorie
    urls_image = scrapping_images(link)

    output_directory = "Images_books_one_category"
    wget.download(urls_image, out=output_directory) #télécharge les images

    with open ("url_images.txt", "a+") as file: 
        file.write(urls_image + '\n') 

    with open ('books_infos_' + categorie.text + '.csv', 'a+', newline ='') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(book_info)
            


 

    


