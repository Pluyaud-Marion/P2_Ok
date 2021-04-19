import requests
from bs4 import BeautifulSoup
from math import ceil
import wget
from fonction_scrapping import scrapping_one_book, scrapping_images, category_book_to_csv
import csv
import os.path
import re

if not os.path.exists("books_toscrap_one_book"):
       os.mkdir("books_toscrap_one_book")
os.chdir("books_toscrap_one_book")

url_dun_livre = input("Veuillez saisir l'url d'un livre : ")

response = requests.get(url_dun_livre)
if response.ok:
       response.encoding = 'utf-8'
       book_info = scrapping_one_book(url_dun_livre) #appel de fonction 1 : récupère les infos d'un livre

urls_image = scrapping_images(url_dun_livre) #appel de fonction 5 : récupère l'url de l'image

wget.download(urls_image) # télécharge l'image à partir de l'url de l'image

with open ('infos_un_livre.csv', 'w', newline ='') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerow(book_info)


