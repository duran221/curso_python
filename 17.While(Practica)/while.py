import math
#Validar la introduccion correcta de una edad:

edad= int(input("Ingrese su edad"))

while(edad<5 or edad>100):
    print("Has introducido una edad incorrecta")
    edad = int(input("Ingrese su edad"))

print("Gracias por colaborar")
print("Su edad es: "+str(edad))


#Validando el ingreso correcto de un numero para calcular una raiz:
print("*****************************************")
print("Programa para calculos de raiz cuadrada:")

numero= int(input("Ingrese un numero"))

contador=0

while(numero<0):
    print("No se puede realizar hallar la raiz de un numero negativo")

    if(contador==2):
        print("Has excedido el maximo de intentos permitidos")
        break;

    numero = int(input("Ingrese un numero"))
    if(numero<0):
        contador+=1

if(contador<2):
    solucion= math.sqrt(numero)
    print("La raiz cuadrada del numero "+str(numero) + "es " +str(solucion))


