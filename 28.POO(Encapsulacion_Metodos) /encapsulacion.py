
#La sintaxis para la creacion de clases es la siguiente:

class Auto:

    #Constructor de clase, encargado de inicializar las variables principales y objetos:
    def __init__(self):

        #Declarando una variable privada, de esta manera no es accesible desde afuera de la clase
        self.__llantas=4
        self.__largo_chasis=200
        self.__ancho=100

    #Metodos del nuestra clase Auto:
    def arrancar(self):

        condicion= self.__realizar_checkeo()

        if(condicion):

            print("El auto esta encendido")
        else:
            print("Hubo un problema al realizar el checkeo")


    def estado(self):
        print(f"El auto tiene {self.__llantas} llantas, un largo de {self.__largo_chasis} y de ancho {self.__ancho}")


    #Como el chequeo que realiza el vehiculo generalmente se hace de manera interna no conviene que esta accion sea ejecutada
    #Exteriormente ya que es ejecutada de manera automatica al encender el vehiculo por ello el metodo
    #Debe ser ENCAPSULADO:
    def __realizar_checkeo(self):

        gasolina=True
        aceite=True
        averias=False

        print("Realizando checkeo del automovil")
        if( gasolina and aceite and not(averias)):
            return True
        else:
            return False


#Instanciando un objeto:
auto1= Auto()

auto1.arrancar()

auto1.estado()

print("************************")

#Dado que estamos intentando modificar un una variable privada, veremos como el valor asignado a esta en la clase no se altera:
auto1.__llantas=2
auto1.estado()

#Si exteriormente invocamos el metodo encapsulado '__realizar_checkeo' nos generará error ya que el motodo se encuentra encapsulado
