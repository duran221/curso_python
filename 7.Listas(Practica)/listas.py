
#Creando una lista vacia en python:
lista1= []

#Creando una lista con elementos:
lista2= ["Lucia","Cristian","Duran","Londoño"]

#Imprimir todos los elementos de la lista:
print(lista2[:])
print("**********************************")
#Accediendo a los elementos en de una lista en un rango especificado(el 3 no se incluye):
print(lista2[1:3])
print("**********************************")

#Accediendo a los 'n' primeros elementos:
print(lista2[:2])
print("**********************************")

#Accediendo a los 'n' ultimos elementos, en este caso desde el que tiene indice 2. hasta el final:
print(lista2[2:])
print("**********************************")

#Tambien puedes acceder a las ultimas posiciones usando numeros negativos:
print(lista2[-2])
print("**********************************")

            #Agregar elementos a el final de una lista:

lista2.append("Mora")
print(lista2[:])
print("**********************************")

            #Insertar elementos en cualquier posicion:

lista2.insert(2,"Yimmi")
print(lista2[:])
print("**********************************")


            #Agregar varios elementos a una lista:

lista2.extend(["Felipe","Ana","Lucia"])
print(lista2[:])
print("**********************************")

            #Obteniendo el index de un elemento en la lista:
print(lista2.index("Ana"))
print("**********************************")


            #Comprobando si un elemento se encuentra en la lista:

if("Juan" in lista2):
    print("Yes")
else:
    print("No")

print("**********************************")

            #Eliminar cualquier elemento de la lista:

lista2.remove("Lucia")
print(lista2[:])
print("**********************************")

            #Eliminar el ultimo elemento de una lista:

lista2.pop()
print(lista2[:])


            #Concatenando listas:
lista3=["Andres","Fernando"]
lista4= lista2+lista3
print(lista4[:])
print("**********************************")


            #Multiplicando listas:

lista3= lista3*3
print(lista3[:])
print("**********************************")


