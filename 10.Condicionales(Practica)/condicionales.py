
sal_presidente= int(input("Ingrese un salario"))

sal_director= int(input("Ingrese un salario"))

sal_jefe_area= int(input("Ingrese un salario"))

sal_administrativo= int(input("Ingrese un salario"))

#Podemos anidar varios operadores en una unica condicion como en el ejemplo siguiente:
if(sal_administrativo<sal_jefe_area<sal_director<sal_presidente):
    print("Todo funciona bien")

else:
    print("Algo esta mal")

#Podemos usar tambien para denotar valores asi:

valor=20
#Preguntando si el valor es mayor a cero y menor que 100
if(0<valor<100):
    print("Mayor que cero y menor que 100")
else:
    print("No cumple")