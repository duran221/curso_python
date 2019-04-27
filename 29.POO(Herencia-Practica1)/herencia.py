
#1. Creando el supertipo o Super clase o Clase Padre:

class Automovil:

    #Constructor de esta super clase, y que heredaran las clases hijas
    def __init__(self, marca,modelo):
        #Las variables estarán a disposicion de las clases que hereden
        self.marca=marca
        self.modelo=modelo
        self.encendido=False
        self.aceleracion=False

    #Estos metodos tambien estaran a disposicion de las clases que hereden
    def arrancar(self):
        self.encendido=True

    def acelerar(self):
        self.aceleracion=True

    def apagar(self):
        self.encendido=False

    def estado(self):
        print(f"El estado del vehiculo: marca: {self.marca}, modelo: {self.modelo} encendido: {self.encendido}")

#La sintaxis para denotar que una clase heredará de otra es muy simple:
class Moto(Automovil):
    pass


#Al instanciar el objeto se hace necesario el definir los atributos que recibe el constructor de la clase padre:
moto1= Moto("Suzuki","1994")

#Ya el objeto puede acceder sin problemas a las variables y metodos de la clase padre:
moto1.arrancar()

moto1.estado()
