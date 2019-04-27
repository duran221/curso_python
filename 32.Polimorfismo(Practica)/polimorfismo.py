
#Creamos distintas clases que comparten un metodo en común
class Coche():

    def desplazamiento(self):
        print("Me estoy desplazando con cuatro ruedas")


class Moto():

    def desplazamiento(self):
        print("Me estoy desplazando con dos ruedas")


class Camion():

    def desplazamiento(self):
        print("Me estoy desplazando con seis ruedas")



#Gracias al polimorfismo es posible que el parametro que ingresa 'vehiculo' pueda ser un Camion,una Moto o un Coche:
#Siendo así es posible adaptar el metodo a cualquier objeto que contenga el metodo en su clase
def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

#Creando el objeto, puede ser una Moto,un Camion o un Coche:
vehiculo= Moto()

#Aplicando polimorfismo con la funcion:
desplazamiento_vehiculo(vehiculo)

