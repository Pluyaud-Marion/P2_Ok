import requests
from bs4 import BeautifulSoup
from math import *
import wget
from fonction_scrapping import scrapping_one_book, scrapping_all_category, scrapping_one_category, scrapping_images
import os.path
os.makedirs("images_Books")
output_directory = "images_Books"

url_site = 'http://books.toscrape.com/index.html'
liste_urls_completes = []
response = requests.get(url_site)
if response.ok:
    liste_urls_incompletes = scrapping_all_category(url_site) #variable qui contient le résultat de la fonction
    for url_incomplete in liste_urls_incompletes:
        liste_urls_completes.append('http://books.toscrape.com/' + url_incomplete) #on rajoute ds liste_urls_completes, le http et urls incomplets
    print(liste_urls_completes)         
#1 : affiche les liens de toutes les catégories sous forme de liste
    
links_livres = []
for url_complete in liste_urls_completes[40:]: #tant qu'on est dans les urls des catégories #supprime le premier (page d'accueil)
    links_livres.append(scrapping_one_category(url_complete)) #rajoute chaque lien dans la liste/ url_complete = les urls des catégories
    print(links_livres)
#2 : affiche les urls de tous les livres des catégories sous forme de liste 

book_info = []
for link_livre in links_livres:
    for link_dun_livre in link_livre:   
        book_info.append(scrapping_one_book(link_dun_livre))
print(book_info)

with open ('infos.csv', 'a+') as file:
        file.write('product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
        file.write(str(book_info))

for link_livre in links_livres:
    for link_dun_livre in link_livre:
        urls_image = scrapping_images(link_dun_livre)
    print(urls_image)

    with open ("images.txt", "a+") as file: 
        file.write(urls_image + '\n')
    wget.download(urls_image, out=output_directory)
#4 : télécharge les images + créé un fichier txt avec les liens de toutes les images"""