import requests
from bs4 import BeautifulSoup
from math import *
import webbrowser
import fonction_category #ou from fonction import all_category

url_site = 'http://books.toscrape.com/index.html'
lien = 'http://books.toscrape.com/'
reponse = requests.get(url_site)
if reponse.ok:
    urls = fonction_category.all_category(reponse) #ou si import all_category en haut --> urls = all_category(reponse)
    print(urls) #affiche les liens de toutes les catégories
    """urls = [] #liste des catégories
    soup = BeautifulSoup(reponse.text,'lxml')
    link = soup.find('ul', {'class' : 'nav nav-list'}).findAll('li')
    for li in link: #for li in li_link
        a=li.find('a')
        urls.append(a['href']"""
    

   
with open("all_category.txt",'w') as fichier:
    for url in urls:
        fichier.write(lien + url + '\n') #créé un fichier txt et y écrit toutes les urls des catégories

with open("all_category.txt", 'r') as entree_fichier: #utilise le fichier txt pour lire les infos et chercher à l'intérieur les urls de tous les livres (quand un seule page + quand plusieurs pages)
    for ligne in entree_fichier: 
        #url_category = ligne.strip() 
        url = url_category + 'page-1.html'
        response = requests.get(url)
        if response.ok: #bloc pour plusieurs pages
            soup = BeautifulSoup(response.text,'lxml')
            nombre_livres = soup.find('form', {'class' : 'form-horizontal'}).find('strong')
            nombre_pages = ceil(int(nombre_livres.text) / int(20))

            for i in range(1,nombre_pages+1):
                url_pages = url_category + 'page-' + str(i) + '.html'
                response = requests.get(url_pages)
                if response.ok:
                    soup = BeautifulSoup(response.text,'lxml')
                    categorie = soup.find('div', {'class' : 'page-header action'}).find('h1')
                    livre = soup.findAll('article')
                    for article in livre:
                        a = article.find('a')
                        link = a['href']
                        links.append('http://books.toscrape.com/catalogue/' + link[9:])
            print(links)

        else: #bloc pour une seule page
            url2 = url_category.replace('page-1.html', 'index.html')
            response = requests.get(url2)
            if response.ok:
                soup = BeautifulSoup(response.text,'lxml')
                categorie = soup.find('div', {'class' : 'page-header action'}).find('h1')
                livre = soup.findAll('article')
                for article in livre:
                    a = article.find('a')
                    link = a['href']
                    #links.append('http://books.toscrape.com/catalogue/' + link[9:])
                    links = 'http://books.toscrape.com/catalogue/' + link[9:]
            print(links)
"""
with open("url_"+ str(categorie.text) + ".txt", 'w') as file: #créé un fichier txt avec toutes les urls de tous les livres de la catégorie / #le nom du fichier txt s'adapte automatiquement au nom de la catégorie concernée
        for link in links:
            file.write(link + "\n")

with open('url_' + str(categorie.text) + ".txt", 'r') as infile: #dans le fichier txt qui affiche toutes les urls, cherche les urls des images / crée un fichier txt qui affiche les urls de toutes les images + ouvre page web avec chaque image
        with open('images_' + str(categorie.text) + '.txt', 'w') as outfile:
            for row in infile:
                links = row.strip()
                reponse = requests.get(links)
                if reponse.ok:
                    soup = BeautifulSoup(reponse.text, 'lxml')
                    image_debut = soup.find('div',{'class' : 'item active'}).find('img')
                    image_ok = ('http://books.toscrape.com/' + image_debut['src'][6:])
                    outfile.write(image_ok + '\n')

                #webbrowser.open(image_ok) 

with open('url_' + str(categorie.text) + ".txt", 'r') as infile:
        with open('infos_' +str(categorie.text) + ".csv", 'w') as outfile: #créé un fichier csv et y met les infos
            outfile.write('product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url\n')
            for row in infile:
                
                url = row.strip()
                reponse = requests.get(url)
                if reponse.ok:
                    soup = BeautifulSoup(reponse.text, 'lxml')
                    product_page_url = url
                    tds = soup.findAll('td')
                    title = soup.find('h1')
                    product_description = soup.find('article', {'class' : 'product_page'}).findAll('p')
                    category = soup.find('ul', {'class' : 'breadcrumb'}).findAll('li')
                    review_rating = soup.find('p', {'class' : 'star-rating'})
                    image_url= soup.find('div',{'class' : 'item active'}).find('img')

        
                    outfile.write(url + ',' + tds[0].text + ',' + title.text + ',' + tds[2].text + ',' + tds[3].text + ',' + tds[5].text + ',' + product_description[3].text + ',' + category[2].text + ','  + review_rating['class'][1]+ ',' + 'http://books.toscrape.com/' + ',' + image_url['src'][6:] + '\n')"""