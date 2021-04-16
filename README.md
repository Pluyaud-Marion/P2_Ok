# P2_Pluyaud_Marion  

Ce projet a pour objectif de récupérer les données du site http://books.toscrape.com/index.html 

Il a été réalisé avec la version 3.9.2 de Python. Vous pouvez l'installer  : https://www.python.org/downloads/release/python-392/  

Pour accéder aux informations du projet, vous devez d'abord télécharger le dossier P2_Pluyaud_Marion.zip via Github puis le décompresser à l'endroit de votre choix.

Ensuite vous devez vous rendre dans le repertoire du dossier (grâce au terminal si vous êtes sur Mac ou Linux, et de l'invite de commande sous Windows), pour créer et activer votre environnement virtuel à l’aide de la commande suivante : 

   ```python -m venv env```  --> pour créer l'environnement virtuel 

  ```source env/bin/activate``` --> pour l'activer sous Mac et Linux 

  ```env\Scripts\activate``` --> pour l'activer sous Windows

Une fois votre environnement virtuel activé, il sera nécessaire d'installer les paquets dans votre environnement pour que vous puissiez exécuter les scripts correctement. 

Pour cela, utilisez la commande : ```pip install -r requirements.txt ```


Vous pouvez désormais lancer l'exécution des différents scripts. 

Ce repository contient 4 scripts Python : 

  1/ "fonctions_scrapping.py" : ce fichier contient les 6 fonctions nécessaires à la bonne exécution des 3 scripts (vous trouverez à l'intérieur de chaque script des commentaires pour plus de lisibilité) 

  2/ "code_one_book.py" : il s'agit de la première étape du projet  --Les informations concernant un livre--

   Lancez l'exécution
   Vous devez à présent interagir avec le programme qui vous demande de choisir un livre  
   --> Faites un copier-coller du lien: http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html  

Un dossier "books_toscrap_one_book" va s'ouvrir dans le répertoire courant contenant l'exécution du script. Vous y trouverez : 

  -L'image de la couverture du livre 
  
  -Un fichier CSV comprenant les informations suivantes sur le livre que vous avez demandé : (Product_page_url / Universal_ product_code (upc) / Title / Price_including_tax / Price_excluding_tax / Number_available / Product_description / Category / Review_rating / Image_url)  


  3/"code_one_category.py" : il s'agit de la deuxième étape du projet  --Les informations concernant une catégorie de livres--

   Lancez l'exécution 
   Vous devez à présent interagir avec le programme qui vous demande de choisir une catégorie de livres  
   Faites un copier-coller du lien : http://books.toscrape.com/catalogue/category/books/mystery_3/index.html  

Un dossier "books_toscrap_one_category" va s'ouvrir dans le répertoire courant contenant l'exécution du script. Vous y trouverez : 

  -Un dossier nommé "Images" + le nom de la catégorie concernée, qui contient les images de couverture de chaque livre de la catégorie 
  
  -Un fichier CSV nomme « infos_books » + le nom de la catégorie concernée, comprenant les informations suivantes sur chaque livre de la catégorie : (Product_page_url / Universal_ product_code (upc) / Title / Price_including_tax / Price_excluding_tax / Number_available / Product_description / Category / Review_rating / Image_url)  


 
  4/"main.py" : il s'agit de l'étape principale du projet --Les informations concernant l’intégralité du site--

  Lancez l’exécution  

Vous n’avez pas besoin de renseigner d’éléments, le script va automatiquement parcourir chacune des 50 catégories du site et identifier chacun des livres de ces catégories. 

Un dossier « books_toscrap » va s’ouvrir dans le répertoire courant contenant l’exécution du script. Vous y trouverez : 

  -50 dossiers (un pour chaque catégorie) intitulés par le nom de chaque catégorie 
A l’intérieur de chaque dossier : 

   -Un dossier nommé « images » + le nom de la catégorie concernée = regroupant les images de couverture de chacun des livres de la catégorie 
    
   -Un fichier csv nommé « books_infos » + le nom de la catégorie concernée = comprenant les informations suivantes pour chaque livre de la catégorie : (Product_page_url / Universal_ product_code (upc) / Title / Price_including_tax / Price_excluding_tax / Number_available / Product_description / Category / Review_rating / Image_url)  

      

 
