#!/usr/bin/python
#-*- coding: utf-8 -*-


from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta



class Juego:
    def __init__(self):
    	self.laberinto=None

    delf laberinto2Habitaciones(self):
    	self.laberinto=Laberinto()

    	hab1 = Habitacion(1)
    	hab2 = Habitacion(2)

    	puerta=Puerta()
    	puerta.lado1=hab1
    	puerta.lado2=hab2

    	hab1.sur=puerta
    	hab2.norte=puerta

    	hab1.norte=Pared()
    	hab1.este=Pared()
    	hab1.oeste=Pared()

    	hab2.sur=Pared()
    	hab2.este=Pared()
    	hab2.oeste=Pared()

    	self.laberinto.agregarHabitacion(hab1)
    	self.laberinto.agregarHabitacion(hab2)

    	juego = Juego()
    	juego.laberinto2Habitaciones()

