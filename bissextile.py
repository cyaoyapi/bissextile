#!/usr/bin/python
#-*- coding:utf-8 -*-

"""Ce module vous permet de tester si une année est bissexitle ou pas"""

print("Ce programme vous permet de tester si une année est bissexitle ou pas.\n")

quitter = raw_input("Voulez-vous demarrez le programme ?\nTapez 'o' pour 'oui' et 'n' pour 'non'\n")

while quitter.upper() == "O":
	annee = int(raw_input("Entrez l'année : \n"))
	if annee%400 == 0:
		print annee," est une année bissextile.\n"
	elif annee%100 == 0:
		print annee," est une année bissextile.\n"
	elif annee%4 == 0:
		print annee," est une année bissextile.\n"
	else:
			print annee," n'est pas une année bissextile.\n"

	quitter = raw_input("Voulez-vous continuez le programme ?\nTapez 'o' pour 'oui' et 'n' pour 'non'\n")

print("Fin du programme. Merci et à bientôt!\n")