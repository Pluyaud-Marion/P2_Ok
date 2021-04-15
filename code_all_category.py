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
urls_incompletes = scrapping_all_category(url_site) #j'appelle fonction 4 qui récupère la liste des urls des catégories incomplètes
for url_incomplete in urls_incompletes:
    liste_urls_completes.append('http://books.toscrape.com/' + url_incomplete) #reforme l'url et fait une liste


for url_complete in liste_urls_completes[1:3]: #tant qu'on est dans les urls des catégories 
    if not os.path.exists(str(scrapp_category(url_complete))):
        os.mkdir(str(scrapp_category(url_complete)))
    os.chdir(str(scrapp_category(url_complete)))

    links_livres = scrapping_one_category(url_complete)#j'appelle fonction 3 qui récupère liste des livres d'une catégorie
    category_book_to_csv(links_livres,str(scrapp_category(url_complete))) #j'appelle fonction 6 qui ouvre le fichier csv et y mets les infos d'une catégorie

    if not os.path.exists("images_" + (str(scrapp_category(url_complete)))):
        os.mkdir("images_" + (str(scrapp_category(url_complete))))   
    os.chdir("images_" + (str(scrapp_category(url_complete))))

    for link_livre in links_livres: #reboucle = pour chaque livre : scrap url image + télécharge images 
        urls_image = scrapping_images(link_livre) #j'appelle fonction 5 qui récupère urls des images
        wget.download(urls_image)
    os.chdir("../..")

    
"""
1/BOUCLE 1 : pour chaque url de catégorie ds tous les urls de catégorie
-création dossier catégorie
-appelle fonction 3 : récupère les liens de tous les livres de la catégorie
-appelle fonction 6 : met les infos de chaque livre ds fichier csv
-ds le dossier de la catégorie --> création dossier images_catégorie
-ds le dossier images_catégorie =
2/BOUCLE 2 : pour chaque livre ds tous les livres de la catégorie
-appelle fonction 5 : récupère les urls des images de la catégorie
-télécharge les images à partir des urls
3/boucle finie pour une catégorie --> on remonte au dossier parent x 2 et on recommence la boucle sur une autre catégorie
"""

"""
1/création dossier books_toscrap
va à l'intérieur
2/pour chaque url de catégorie ds tous les urls de catégories création dossier de la catégorie
-va à l'intérieur
-on y met le csv avec les infos sur tous les livres
3/à l'intérieur du dossier de la catégorie on créée dossier image_catégorie
-va à l'intérieur
4/ds le dossier image_Catégorie, pour chaque livre : on télécharge l'image

5/a chaque tour de boucle on remonte de 2 crans et on repart
    -books_toscrap
    -catégorie
    -image_catégorie
"""

"""

"""
       
     
