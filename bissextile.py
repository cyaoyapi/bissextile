#!/usr/bin/python
#-*- coding:utf-8 -*-

annee = int(raw_input("Entrez l'année : \n"))

if annee%4 == 0:
	if annee%100 == 0:
		if annee%400 == 0:
			print annee," est une année bissextile.\n"
		else:
			print annee," n'est pas une année bissextile.\n"
	else:
		print annee," est une année bissextile"
else:
	print annee," n'est pas une année bissextile.\n""