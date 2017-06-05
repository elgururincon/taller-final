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

import random                                       # importar modulo random
import time                                         # importar modulo time

class JuegoDeLaVida():                              # creacion de clase principal

### El método __init__ es un método especial de una clase en Python. El objetivo fundamental del 
### método __init__ es inicializar los atributos del objeto que creamos.
    
    def __init__(self, fila, columna):

        self.fila = fila                                  
        self.columna = columna                            
        
# devuelve una lista con vida aleatoria donde 0 es que esta muerto y 1 esta vivo
# (f = lambda argumentos: resultado) --> funcion lambda retorna automaticamente True
        
        filaVivo = lambda: [random.randint(0, 1) for n in range(self.columna)]   
        self.juego = [filaVivo() for n in range(self.fila)]               # creacion de tablero con 0 y 1

        self.vivo = 1                                     # vivos  == True
        self.muerto = 1                                   # muertos == true

    def __str__(self):                    #funcion (__str__) que devuelve el tablero como una cadena de caracteres

        tablero = ''                                      # cadena vacia
        for fila in self.juego:
            for vecino in fila:
                tablero += ' ● ' if vecino else ' . '     # agregra un caracrter especial dpenediendo el valor
            tablero += '\n'


        return tablero

    def vecinos(self, fila, columna):                     # funcion que devulve el numero de vecinos 
        
### calculamos las permutaciones posibles en las posiciones de los vecinos , y los guarda en una lista nueva
        distancia= [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
### funcion que lee los limites del tablero
        limite = lambda i, j: (i in range(self.fila) and j in range(self.columna))

        total = 0                                         # contador total de vecinos
        
        # df --> distancia de fila
        # dc --> distancia de culumna
        for df, dc in distancia:
            if limite(df + fila, dc + columna):                 # valida la condicion de los vecinos
                total += self.juego[df + fila][dc + columna]    # agrega valor al contador total 
        return total

    def recorrido(self):                                  # metodo que define el recorrido 

        gameaux = self.juego
        
        for df in range(self.fila):                        
            for dc in range(self.columna):
                total = self.vecinos(df, dc)

                if (total < 2 or total > 3) and gameaux[df][dc]:                # condicion de validacion
                    gameaux[df][dc] = 0                                         # muere o sigue muerta
                    
                elif total == 3 and not gameaux[df][dc]:                        # condicion de validacion
                    gameaux[df][dc] = 1                                         # vive o sigue viva
                    


fila = int(input("numero de filas >> "))                      # preguntamos al usuario cantidad de filas
columna = int(input("numero de columnas >> "))                # preguntamos al usuiario cantidad de columnas

juego = JuegoDeLaVida(fila, columna)                    # llamamos la clase con los atributos fila y columna

iteraciones = 0                                         # contador de iteraciones

### mientras la cantidad de vecinos ya sean vivos o muertos sea diferente a 0 haga
while juego.vivo > 0 or juego.muerto > 0:               

        juego.recorrido()                             # llamamos al juego desde la funcion recorrido
        print(juego)                                  # imprime juego
        iteraciones += 1                              # agrega 1 al contador de iteraciones
        time.sleep(1)                                 # funcion de tiempo que sirve para imprimir el juego
        
print" Total: = %d " %iteraciones                     # imprime la cantidad de iterciaones totales
