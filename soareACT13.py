#!/usr/bin/env python
# -*- coding: utf-8 -*-

def crealista(lista):
	valores = int(input("Dígame cuantos valores tiene la lista: "))
	for i in range (0, valores):
		num = int(input("Escribe un número:"))
		lista+=[num]
	print "La lista creada es:", lista
	return
def sumalista(lista):
	suma=0
	for i in lista:
		suma+=i
	print "El resultado de la suma es:", suma
	return
	
lista=[]
crealista(lista)
sumalista(lista)
