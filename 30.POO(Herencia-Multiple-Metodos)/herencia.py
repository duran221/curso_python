
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

#La clase hereda de Automovil, asi sus metodos seran accesibles por esta clase:
class Furgoneta(Automovil):

    def carga(self,carga):

        self.cargado= carga

        if(self.cargado):
            return "El automovil está cargado"

        else:

            return  "El auto no está cargado"


#La sintaxis para denotar que una clase heredará de otra es muy simple:
class Moto(Automovil):

    hace_caballito=""

    #La clase puede tener sus propios metodos y usar sus propias variables:
    def caballito(self):
        self.hace_caballito="Estoy picando la moto"


    """Sobreescritura de metodos: para sobreescribir un método de la clase padre escribimos un metodo con igual nombre 
        e igual numero de parametros, asi, al momento de ejecutar el metodo se ejecutara éste y no el de la clase padre"""

    def estado(self):

        print(f"El estado del vehiculo: marca: {self.marca}, modelo: {self.modelo} encendido: {self.encendido}, {self.hace_caballito}")


#A su vez, cuatrimoto puede heredar de Moto, asi, cuatrimoto podra acceder a los metodos y variables de la clase Moto.
class Cuatrimoto(Moto):

    bomper=""


#Creando una nueva clase o supertipo VElectricos:
class VElectricos():


    def __init__(self):
        self.autonomia=True

    def cargar(self):
        self.cargando=True


class BiciElectrica(VElectricos,Automovil):
    pass




#Al instanciar el objeto se hace necesario el definir los atributos que recibe el constructor de la clase padre:
moto1= Moto("Suzuki","1994")

#Ya el objeto puede acceder sin problemas a las variables y metodos de la clase padre:
moto1.arrancar()
moto1.caballito()
moto1.estado()
print("*************************************")


#Como el objeto hereda de la superclase Vehiculo, se hace NECESARIO ingresar los parametros especificados por el constructor de esta:
cuatrimoto=Cuatrimoto("Yamaha","2015")
cuatrimoto.estado()
print("*************************************")


#Como furgoneta hereda de Automovil deberá usar su constructor, cabe aclarar que Moto no podrá acceder a los metodos de Furgoneta por ovbias razones:
camion= Furgoneta("Ford","Cargo")
camion.arrancar()
camion.carga(True)
camion.estado()
print("*************************************")

#Al declarar un objeto como BiciElectrica que hereda de dos clases o más debemos tener en cuenta qué constructor usar, pues bien usamos
#EL constructor de la superclase que esta más a la izquierda, en este caso usamos el constructor de VElectricos que no recibe ningun parametro.
bici= BiciElectrica()
print("*************************************")
