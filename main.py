import requests
from bs4 import BeautifulSoup
from math import *
import wget
import os.path
import csv
import re
from fonction_scrapping import scrapping_one_book, scrapping_all_category, scrapping_one_category, scrapping_images, scrapp_category, category_book_to_csv

if not os.path.exists("books_toscrap"):
    os.mkdir("books_toscrap")
os.chdir("books_toscrap")

url_site = 'http://books.toscrape.com/index.html'

liste_urls_completes = []
urls_incompletes = scrapping_all_category(url_site) #appel de fonction 4 : récupère la liste des urls des catégories incomplètes
for url_incomplete in urls_incompletes:
    liste_urls_completes.append('http://books.toscrape.com/' + url_incomplete) #reconstitue l'url des catégories complète et les met dans une liste


for url_complete in liste_urls_completes[1:]: 
    if not os.path.exists(str(scrapp_category(url_complete))):
        os.mkdir(str(scrapp_category(url_complete)))
    os.chdir(str(scrapp_category(url_complete)))

    links_livres = scrapping_one_category(url_complete)#appel de fonction 3 : récupère liste de tous les livres d'une catégorie
    category_book_to_csv(links_livres,str(scrapp_category(url_complete))) #appel de fonction 6 : ouvre le fichier csv et y mets les infos des livres d'une catégorie

    if not os.path.exists("images_" + (str(scrapp_category(url_complete)))):
        os.mkdir("images_" + (str(scrapp_category(url_complete))))   
    os.chdir("images_" + (str(scrapp_category(url_complete))))

    for link_livre in links_livres: 
        urls_image = scrapping_images(link_livre) #appel de fonction 5 : récupère urls des images
        wget.download(urls_image)
    os.chdir("../..")

    

     
