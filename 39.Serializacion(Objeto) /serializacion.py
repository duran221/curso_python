##############Escritura del archivo#################

#Importando la libreria pickle necesaria para codificar en binario nuestro objeto:
import pickle

class Automovil():

    def __init__(self,marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.marcha= False
        self.acelera=False


    def arrancar(self):

        self.marcha=True

    def acelerar(self):
        self.acelera=True

    def estado(self):

        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Marcha: {self.marcha}, Aceleracion: {self.acelera}")


#Creando las instancias de la clase Automovil y almacenando en una lista:
auto1= Automovil("Chevrolet","Spark")
auto2= Automovil("Mazda","Coupe")
auto3= Automovil("Renault","Clio")


coches= [auto1,auto2,auto3]

#Abriendo o creando un archivo en modo de escritura binaria:
fichero= open("coches","wb")

#Dumpeando el archivo, es decir almacenando nuestro objeto codificado en el fichero
pickle.dump(coches,fichero)

#Respectivos cierre y eliminacion de memoria:
fichero.close()

del (fichero)



