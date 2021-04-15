import requests
from bs4 import BeautifulSoup
from math import *
import wget
from fonction_scrapping import scrapping_one_book, scrapping_images
import csv
import os.path
import re

os.mkdir("Books.toscrap")
os.chdir("Books.toscrap")

url_dun_livre = input("Veuillez saisir l'url d'un livre : ")

response = requests.get(url_dun_livre)
if response.ok:
       response.encoding = 'utf-8'
       book_info = scrapping_one_book(url_dun_livre) 
print(book_info)

urls_image = scrapping_images(url_dun_livre)    

os.mkdir("Image_one_book") #création d'un dossier image
output_directory = "Image_one_book" #change le répertoire pour mettre l'image
wget.download(urls_image, out=output_directory)

with open ('infos_un_livre.csv', 'w', newline ='') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(book_info)


       