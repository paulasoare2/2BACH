#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(a,b):
	resultado=a+b
	return resultado
	
def resta(a,b):
	resultado=a-b
	return resultado
	
def division(a,b):
	resultado=a/b
	return resultado
	
def multiplicacion(a,b):
	resultado=a*b
	return resultado
	
a = int(input("Introduzca un numero:"))
b = int(input("Introduzca un numero:"))
final="n"
	
while final<>"S":
	opcion = raw_input("Elija una opcion (S,R,M,D):")
	
	if opcion=="S" or opcion=="s": 
		resultado=suma(a,b)
		print resultado
	elif opcion=="R" or opcion=="r":
		resultado=resta(a,b)
		print resultado
	elif opcion=="D" or opcion=="d":
		resultado=division(a,b)
		print resultado
	elif opcion=="M" or opcion=="m":
		resultado=multiplicacion(a,b)
		print resultado
	final=raw_input("¿Quieres finalizar (S)?")
