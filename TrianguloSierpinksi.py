/*
# Solution for a class exercise.
#
# Created by Cristian David Rincon on June 2017.
# Copyright (c) 2017  Cristian David Rincon. All rights reserved.
#
# This file is part of DataStructures course.
#
# DataStructuresCourse is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, version 2.
*/

niveles = int(raw_input("cuantos niveles deseas?"))               
A1 = [0 , 1, 0]                                                   
reglas = {7:0, 6:0, 5:0, 4:1, 3:0, 2:0, 1:1, 0:0}                 
A2 = []
tablero = ''
base = len(A1) + niveles * 2


def imprimeTablero(array):
	global base
	while len(array) < base:
		array.insert(0,0)
		array.append(0)
	tablero = ''
	for i in range(0, base):
		if array[i] == 0:
			tablero += ' '
		else:
			tablero += 'X'
	print tablero

def siguienteNivel(nivelActual):
	global niveles, base
	nivelNuevo =[]
	for i in range(1, base - 1):
		aux = nivelActual[i-1:i+2]
		aux.reverse()
		espacio = 0
		for j in range(0,3):
			espacio += (2**j) * aux[j]

		nivelNuevo.append(reglas[espacio])
	
	nivelNuevo.insert(0,0)
	nivelNuevo.append(0)
	return nivelNuevo

for i in range(0,niveles):
	imprimeTablero(A1)
	A1 = siguienteNivel(A1)
      
