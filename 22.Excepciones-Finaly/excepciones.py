
def divide():

    try:
        num1= int(input("Ingrese un numero: "))
        num2= int(input("Ingrese un numero: "))

        print("El resultado de la division es: "+str(num1/num2))

    #Es posible anidar una o mas excepciones para encerrar los distintos errores que se pueda producir
    except ValueError:
        print("Por favor ingrese un numero")

    #Tambien es posible renombrar la excepcion para imprimir el tipo de excepcion capturada
    except ZeroDivisionError as e:
        print(f"Se ha generado la siguiente excepcion: {e}")
        print("No es posible realizar divisiones por cero")


    #Esta instruccion ejecutara lo que haya encerrado dentro del bloque de codigo sin importar si se produce o no excepciones:
    finally:
        print("Ejecucion terminada")

divide()


def divide2():
    try:
        num1= int(input("Ingrese un numero: "))
        num2= int(input("Ingrese un numero: "))

        print("El resultado de la division es: "+str(num1/num2))

    #Con esta estructura, el programa intenta ejecutar lo que hay dentro del try, si se genera una excepcion esta NO se captura
    #Pero el programa no se cae, ejecuta la instruccion que hay en el finaly
    finally:
        print("Ejecucion terminada")

divide2()


