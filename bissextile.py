#!/usr/bin/python
#-*- coding:utf-8 -*-

"""Ce module vous permet de tester si une année est bissexitle ou pas"""

print("Ce programme vous permet de tester si une année est bissexitle ou pas.\n")

quitter = raw_input("Voulez-vous demarrez le programme ?\nTapez 'o' pour 'oui' et 'n' pour 'non'\n")

while quitter.upper() == "O":
	try:
		annee = int(raw_input("Entrez l'année : \n"))
		if annee < 0:
			raise ValueError("L'année que vous que vous avez saisie est négative.\n")
	except ValueError:
		print "L'année que vous avez saisie est soit négative ou est une alphanumérique.\n"
	else:
		if (annee%400 == 0) or (annee%4 == 0 and annee%100 != 0):
			print annee," est une année bissextile.\n"
		else:
			print annee," n'est pas une année bissextile.\n"
	finally:
		quitter = raw_input("Voulez-vous continuez le programme ?\nTapez 'o' pour 'oui' et 'n' pour 'non'\n")

print("Fin du programme. Merci et à bientôt!\n")