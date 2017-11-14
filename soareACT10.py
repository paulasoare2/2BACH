#!/usr/bin/env python
# -*- coding: utf-8 -*-
print("Comprobador de años bisiestos")

fecha = int(input("Escriba un año y le diré si es bisiesto:"))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
	
	print("El anyo", fecha, "es un anyo bisiesto.")
else:
	print("El anyo", fecha, "no es un anyo bisiesto")
