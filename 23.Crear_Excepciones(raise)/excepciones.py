#Importando la libreria matematica:

import math

def calcula_raiz(num):

    if(num<0):
        #La instruccion permite LANZAR excepciones, tambien podemos crear nuestras propias excepciones, cosa que veremos adelante:
        raise ValueError("No se puede calcular la raiz a un numero negativo")

    else:

        return math.sqrt(num)

#Como nosotros hemos lanzado una excepcion en el metodo se hace necesario encerrar la llamada en un try, ya que si se genera
#La excepcion el programa se caeria.
try:
    print("Su calculo ha sido realizado: "+str(calcula_raiz(2)))

except ValueError as e:
    print("Se ha generado un error: "+ str(e))


print("Ejecucion terminada")


