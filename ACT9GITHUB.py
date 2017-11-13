#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rectangulo(x,y,z):
	for i in range(x):
		for j in range(y):
			print z,
		print " "


anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
caracter = raw_input("Caracter a elegir:")

rectangulo(anchura,altura,caracter)
