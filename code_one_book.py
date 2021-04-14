import requests
from bs4 import BeautifulSoup
from math import *
import wget
from fonction_scrapping import scrapping_one_book, scrapping_images
import csv
import os.path
os.makedirs("Image_one_book")
output_directory = "Image_one_book"
import re


url_dun_livre = input("Veuillez saisir l'url d'un livre : ")

response = requests.get(url_dun_livre)
if response.ok:
       response.encoding = 'utf-8'
       book_info = scrapping_one_book(url_dun_livre) 
print(book_info)

urls_image = scrapping_images(url_dun_livre)          

wget.download(urls_image, out=output_directory)

         
with open ('infos_un_livre.csv', 'w', newline ='') as csvfile:
       csvfile.write('product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url, \n')
       csvfile.write(str(book_info) + '\n')


       