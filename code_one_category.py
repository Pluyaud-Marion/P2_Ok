import requests
from bs4 import BeautifulSoup
from math import *
import wget
import os.path
import csv
import re
from fonction_scrapping import scrapping_one_book, scrapping_one_category, scrapping_images, scrapp_category,category_book_to_csv


url_category = input("Veuillez saisir l'url d'une catégorie : ")

#url_category = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
#url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

if not os.path.exists("books_toscrap"):
    os.mkdir("books_toscrap")
os.chdir("books_toscrap")

links = scrapping_one_category(url_category)
 #j'appelle fonction 3 qui renvoie la liste de tous les livres d'une catégorie (mis ds variable "links")
nom_categorie = scrapp_category(url_category) #j'appelle fonction 2 qui scrappe nom de la catégorie

category_book_to_csv(links,nom_categorie) #création du fichier csv avec le nom de la catégorie

if not os.path.exists("images_books_one_category"): #création dossier image
    os.mkdir("Images_books_one_category")
os.chdir("Images_books_one_category")

for link in links: #pour chaque livre dans tous les livres
    urls_image = scrapping_images(link) #j'appelle fonction 5 qui récupère les urls des images
    wget.download(urls_image) #télécharge l'image grace à son url




    
