import requests
from bs4 import BeautifulSoup
from math import *
import wget
from fonction_scrapping import scrapping_one_book, scrapping_all_category, scrapping_one_category, scrapping_images, scrapp_category
import os.path
import csv
import re
os.mkdir("Books.toscrap")
os.chdir("Books.toscrap")

url_site = 'http://books.toscrape.com/index.html'
liste_urls_completes = []
response = requests.get(url_site)
if response.ok:
    liste_urls_incompletes = scrapping_all_category(url_site) #variable qui contient le résultat de la fonction
    for url_incomplete in liste_urls_incompletes:
        liste_urls_completes.append('http://books.toscrape.com/' + url_incomplete) #on rajoute ds liste_urls_completes, le http et urls incomplets
    #print(liste_urls_completes)       
#1 : affiche les liens de toutes les catégories sous forme de liste


links_livres = []
for url_complete in liste_urls_completes[1:3]: #tant qu'on est dans les urls des catégories #supprime le premier (page d'accueil)
    links_livres.append(scrapping_one_category(url_complete)) #rajoute chaque lien dans la liste/ url_complete = les urls des catégories
print(links_livres)
#2 : affiche les urls de tous les livres des catégories sous forme de liste 

book_info = []
for link_livre in links_livres:
    for link_dun_livre in link_livre:   
        book_info.append(scrapping_one_book(link_dun_livre))
#print(book_info)


for url_complete in liste_urls_completes[1:3]:
    os.mkdir(str(scrapp_category(url_complete)))
    #os.chdir(str(scrapp_category(url_complete)))
    with open ('infos_' + str((scrapp_category(url_complete)))+ '.csv', 'w', newline ='') as csvfile:
        for link_livre in links_livres:
            for link_dun_livre in link_livre: #2 boucles car link_livre est une liste alors on reboucle à l'intérieur pour chercher chaque url
                fieldnames = ['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(scrapping_one_book(link_dun_livre)) #avec books_info ne fonctionnait pas car était une liste, j'appelle donc ma fonction



os.mkdir("images_Books")
os.chdir("images_Books")


for link_livre in links_livres:
    for link_dun_livre in link_livre:
        urls_image = scrapping_images(link_dun_livre)
    #print(urls_image)
        
        with open ("urls_images.txt", "a+") as file: 
            file.write(urls_image + '\n')

        wget.download(urls_image) 

#4 : télécharge les images dans le dossier images_books + créé un fichier txt avec les liens de toutes les images