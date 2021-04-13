import requests
from bs4 import BeautifulSoup
from math import *
import wget
from fonction_scrapping import scrapping_one_book
import csv


url_dun_livre = input("Veuillez saisir l'url d'un livre : ")

response = requests.get(url_dun_livre)
if response.ok:
       book_info = scrapping_one_book(url_dun_livre) 
print(book_info)
            #affiche les infos pour un livre

with open ('infos_un_livre.csv', 'w') as file:
       file.write('product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url \n')
       file.write(str(book_info))

            #met toutes les infos dans un fichier csv"""
