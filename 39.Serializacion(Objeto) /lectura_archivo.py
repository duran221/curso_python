####################Lectura del archivo#########################

import pickle

#Importando la clase automovil de nuestro modulo serializacion:
from serializacion import Automovil

#Abriendo el archivo en modo de 'lectura binaria'
fichero_leido= open("coches","rb")

#Cargando una coleccion de coches almacenada en el archivo leido:
lista_coches= pickle.load(fichero_leido)

#Cerrando el archivo en memoria:
fichero_leido.close()

#Recorriendo la coleccion de coches obtenida con el metodo load():
for coche in lista_coches:

    print(coche.estado())
    print("**********************")

