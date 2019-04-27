
#Utilizada si deceas importar el modulo, al usar un metodo o variable o clase deberás anteponer el nombre del modulo:
import funciones_matematicas

#Importando un metodo o variable del modulo, usado cuando no es necesario importar todo el modulo:
from funciones_matematicas import potencia

#Se importan todos los metodos,clases y variables del modulo funciones_matematicas
from funciones_matematicas import *


#La llamada hace uso del 'import funciones_matematicas'
funciones_matematicas.sumar(3,4)

#Haciendo uso del 'from funciones_matematicas import potencia'
potencia(5,2)


