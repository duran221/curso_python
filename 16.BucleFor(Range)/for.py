
#La funcion range, usada en el for permite el uso de uno o mas parametros, veamos:

#Mostrando los numeros de cero a 4:
for i in range(5):
    #Podemos usar funciones 'f' para hacer concatenaciones especiales:
    print(f"Numero: {i}")

print("*******************")

#Podemos tambien delimitar un rango:
for i in range(5,10):
    print(f"Numero: {i}")

print("*******************")


#Adicional podemos usar un tercer parametro para indicar de cuanto en cuanto el contador incrementa o decrementa:
for i in range(0,27,3):
    print(f"Numero: {i}")

print("*******************")


email="jajaja@"
#Usando la funcion 'len':
for i in range(len(email)):
    print(email[i])

print("*******************")
