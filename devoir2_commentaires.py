#coding: utf-8

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont encore précédées de trois dièses ###

### D'abord, le nom de ton script ne se terminait pas par «.py»...

import csv

### Je commence par modifier légèrement le nom du fichier afin de permettre à ton code de rouler sur mon ordi

fichier = '../grants.csv'
f1 = open(fichier)
document = csv.reader(f1)
n = 0

#Puisque le fond est composé de trois subventions, il faut faire 3 recherche:

editeurs = "Aide aux éditeurs"
innovation = "Innovation commerciale"
initiative = "Initiatives collectives"

#Le fun commence. On veut imprimer chaque subvention (ligne) qui ont l'une de nos variables identifiées plus haut.

for ligne in document:
	
	if any(editeurs in colonne for colonne in ligne) or any(innovation in colonne for colonne in ligne) or any(initiative in colonne for colonne in ligne):	
		
		#On veut maintenant connaître en quelle année ces subventions ont été allouées
		date = ligne[13]

### Astucieuse méthode pour trouver l'année.
### Je n'y avais pas pensé!
### Ma méthode était plutôt celle-ci : annee = ligne[13][:4]
### Les deux sont bonnes :)

		annee = date.split("-")

		n += 1
		print(n, annee[0], ligne)

### Ton code est bon, mais il ne permet malheureusement pas de filtrer les subventions du Fonds du Canada pour les périodiques (FCP)
### Il en identifie 4844
### Or, certaines «Initiatives collectives» ne concernent pas le Fonds du Canada pour les périodiques et touchent plutôt le monde du livre

### La solution, un seul «if», mais avec un «or»:
### «if "Fonds du Canada pour les périodiques" in ligne[17] or "FCP -" in ligne[17]:»
### Cela t'en donne 4608 et se rapproche davantage de ce que l'on cherche.