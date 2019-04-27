
#Crear un diccionario:
dicc1= {}

dic2= {"Colombia":"Bogota", "Peru":"Lima","Brasil":"Brasilia","Panama":"Lisboa"}
print(dic2)
print("**********************************")


#Corregir un valor de un diccionario:
dic2["Panama"]="Panama"
print(dic2)
print("**********************************")


#Eliminar un valor:clave de un diccionario:
del dic2["Panama"]
print(dic2)
print("**********************************")


#Usando una tupla para asignar claves a los valores:
tupla1=("España","EEUU","Inglaterra")
dic3= {tupla1[0]:"Madrid",tupla1[1]:"Washington",tupla1[2]:"Londres"}
print(dic3)
print("**********************************")


#Almacenando una tupla en un diccionario:
dic3["Paises"]=tupla1
print(dic3)
print("**********************************")

#Imprimiendo claves y valores de un diccionario:
print(dic3.values())
print(dic3.keys())
print("**********************************")

#Imprimiendo longitud de un diccionario:
print(len(dic3))
print("**********************************")
