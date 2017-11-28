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
		suma/=i
	print "El resultado de la suma es:", suma
	return
	
def promediolista(lista):
	suma=0.0
	for i in range(0,len(lista)):
		suma=suma+lista[i]
	promedio=suma/len(lista)
	print "El promedio de la lista es:", promedio
	
lista=[]
crealista(lista)
sumalista(lista)
promediolista(lista)
