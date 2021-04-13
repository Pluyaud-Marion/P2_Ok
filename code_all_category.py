import requests
from bs4 import BeautifulSoup
from math import *
import webbrowser

import wget
from fonction_scrapping import scrapping_one_book, scrapping_all_category, scrapping_one_category, scrapping_images

url_site = 'http://books.toscrape.com/index.html'
liste_urls_completes = []
response = requests.get(url_site)
if response.ok:
    liste_urls_incompletes = scrapping_all_category(url_site) #variable qui contient le résultat de la fonction
    for url_incomplete in liste_urls_incompletes:
        liste_urls_completes.append('http://books.toscrape.com/' + url_incomplete) #on rajoute ds liste_urls_completes, le http et urls incomplets
    #print(liste_urls_completes)
           
#1 : affiche les liens de toutes les catégories sous forme de liste
    
    for url_complete in liste_urls_completes[1:]: #tant qu'on est dans les urls des catégories #supprime le premier (page d'accueil)
        links_livres = scrapping_one_category(url_complete) #appelle la fonction 2 / url_complete = les urls des catégories
        #print(links_livres)
####AFFICHE LES LIENS DES LIVRES DES CATEGORIES QUI ONT UNE PAGE, ET AFFICHE [] POUR LES CATEGORIES QUI ONT PLUSIEURS PAGES


#2 : affiche les urls de tous les livres des catégories sous forme de liste 
    for link_livre in links_livres:   
        books_infos = scrapping_one_book(link_livre) #paramètre de ma fonction : les liens de tous les livres
    #print(books_infos)

#####AFFICHE QUE LES INFOS SUR LE DERNIER LIVRE

#3 : affiche les infos de tous les livres

    for link_livre in links_livres:
        urls_image = scrapping_images(link_livre) ###il faudrait mettre en paramètre links_livres et non link_livre, mais erreur
        print(urls_image)

    wget.download(urls_image) #télécharge les images

    with open ("images.txt", "w") as file: #vérifier si ok sur le nom du fichier
        file.write(urls_image) 


#4 : télécharge les images + créé un fichier txt avec les liens de toutes les images



