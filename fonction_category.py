from bs4 import BeautifulSoup
import requests

def all_category(reponse):

    urls = [] #liste des catégories
    soup = BeautifulSoup(reponse.text,'lxml')
    link = soup.find('ul', {'class' : 'nav nav-list'}).findAll('li')
    for li in link: # ou for li in li_link
        a=li.find('a')
        urls.append(a['href'])
    return(urls)

