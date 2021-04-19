import requests
from bs4 import BeautifulSoup
from math import *
import wget
import os.path
import csv
import re
from fonction_scrapping import scrapping_one_book, scrapping_one_category, scrapping_images, scrapp_category,category_book_to_csv


url_category = input("Veuillez saisir l'url d'une catégorie : ")

if not os.path.exists("books_toscrap_one_category"):
    os.mkdir("books_toscrap_one_category")
os.chdir("books_toscrap_one_category")

links = scrapping_one_category(url_category) #appel de fonction 3 : renvoie liste de  tous les livres d'une catégorie
nom_categorie = scrapp_category(url_category) #appel de fonction 2 : récupère le nom de la catégorie

category_book_to_csv(links,nom_categorie) #création du fichier csv 

if not os.path.exists("images_" + (str(scrapp_category(url_category)))): 
    os.mkdir("images_" + (str(scrapp_category(url_category))))
os.chdir("images_" + (str(scrapp_category(url_category))))

for link in links: 
    urls_image = scrapping_images(link) #appel de fonction 5 : récupère les urls des images
    wget.download(urls_image) #télécharge l'image à partir de son url




    
