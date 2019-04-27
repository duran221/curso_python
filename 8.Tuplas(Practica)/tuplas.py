

#Creando una tupla:

tupla1= ("Hola",45,True,12.5,True)

#Imprimiendo una tupla:
print(tupla1)
print("**********************************")

#Imprimiendo un elemento de la tupla:
print(tupla1[2])
print("**********************************")

#Como no podemos acceder mediante index a los elementos de una tupla, podemos crear una lista a partir de la tupla:
lista1= list(tupla1)
print(lista1[:])
print("**********************************")

#Contar cuantas veces se encuentra un elemento en una lista:
print(tupla1.count(True))
print("**********************************")


#Longitud de un array:
print(len(tupla1))
print("**********************************")


#Crear una tupla unitaria:
tupla2= ("Cristian",)
print(tupla2)
print("**********************************")

#Desempaquetando una tupla:
saludo,numero1,bool1,numero2,bool2= tupla1

print(numero1)
print(numero2)
print(bool1)
print(bool2)
print(saludo)
print("**********************************")


