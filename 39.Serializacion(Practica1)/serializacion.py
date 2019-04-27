#Serializando colecciones

#Importando la libreria que nos permite convertir y leer nuestros archivos en binario:
import pickle

##############Creando un fichero binario: #################3

lista= ["Hola","Esta es","Una","Lista"]

#Se crea un archivo con permisos 'wb' escritura binaria
fichero_binario= open("lista_nombres","wb")

#usamos metodo dump que nos permite guardar el fichero de la lista cifrado en binario
pickle.dump(lista,fichero_binario)

#Cerrando el archivo en memoria
fichero_binario.close()

#Eliminando el archivo:
del (fichero_binario)


###########Abrir un archivo binario################

#Abriendo el fichero con permisos de 'rb' lectura binaria
fichero= open("lista_nombres","rb")

#El metodo pickle.load permite cargar o leer un archivo binario:
lista= pickle.load(fichero)


print(lista)
