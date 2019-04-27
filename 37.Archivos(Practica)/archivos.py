
#Importando el metodo necesario para poder ABRIR un archivo:
from io import open

                            #Escribiendo en un archivo:

#Almacenando en la variable la apertura del archivo, 'open' recibe dos parametros:
#(1.EL NOMBRE DEL ARCHIVO A ABRIR,EL TIPO DE ACCESO AL ARCHIVO,lectura(r),escritura(w),agregar(a)):
archivo_texto= open("archivo.txt","w")

#Si 'archivo.txt' no existe, python automaticamente lo crea

frase="Estupendo dia para estudiar python \n el viernes"

#El metodo 'write' me permite escribir en el archivo la cadena de texto almacenada en 'frase':
archivo_texto.write(frase)

#Cerrando el archivo en memoria (Muy importante)
archivo_texto.close()

                    # Leyendo un archivo:


#Abriendo esta vez el archivo en modo 'lectura':
archivo_texto=open("archivo.txt","r")

#Este metodo comentado me permite leer todo el archivo
#texto= archivo_texto.read()

#Pero es mas útil almacenar linea a linea del archivo en un array:
lineas_texto= archivo_texto.readlines()

archivo_texto.close()

print("************************")
print(lineas_texto)


                    #Agregando a un archivo:

#Abriendo el archivo pasando como argumento una a de 'append':
archivo_texto= open("archivo.txt","a")

#Escribiendo la nueva linea en el archivo:
archivo_texto.write("\n Siempre es una buena ocasion para estudiar python")

#Cerrando como siempre el archivo:
archivo_texto.close()


#Verificar los cambios hechos en el archivo.

                #Abriendo el archivo como lectura y escritura:

archivo_texto2= open("archivo2.txt","w")

archivo_texto2.write("Estupendo dia para estudiar python \nel viernes \nSiempre es una buena ocasion para estudiar python")
print("***************************")
archivo_texto2.close()


#Abriendo nuestro archivo en modo de lectura y escritura:
archivo_texto2= open("archivo2.txt","r+")

print(archivo_texto2.read())

#el metodo seek me permite posicionar el cursos en un numero de caracteres determinado: por ejemplo aqui posicionamos el cursor al inicio:
archivo_texto2.seek(0)
print("\n")

#Al leer nuevamente el archivo, como el cursor fue posicionado al inicio, leerá el archivo desde el caracter cero:
print(archivo_texto2.read())

archivo_texto2.close()
print("*********************")

archivo_texto2= open("archivo2.txt","r+")

#Si agregamos un argumento a 'read' estamos indicando que nos lea hasta por ejemplo el caracter 10
print(archivo_texto2.read(10))

#Como el cursor está ubicado en el caracter 10, leerá de ahi en adelante:
print(archivo_texto2.read())

print("**********************")
#Ubicando el cursor en la mitad de el texto almacenado:
archivo_texto2.seek(0)
archivo_texto2.seek(len(archivo_texto2.read())/2)
print(archivo_texto2.read())
print("*************************")
#Como podemos ver se ubica el cursor en el centro de la cadena, y a partir de alli lee el contenido

#Reiniciando el cursor al principio:
archivo_texto2.seek(0)

#Vamos por ejemplo a posicionar el cursor al final de la primera linea:
archivo_texto2.seek(len(archivo_texto2.readline()))

#El archivo es leido pero no se incluye la primera linea
print(archivo_texto2.read())
print("***********************")
archivo_texto2.close()

#Lectura y escritura:
archivo_texto2= open("archivo2.txt","r+")

#Vamos a reemplazar una linea del texto que tenemos: en primer lugar almacenamos las lineas en una lista:
lista_texto= archivo_texto2.readlines()

#Modificamos la posicion 1 de la lista:
lista_texto[1]="Esta linea se ha incluido desde el exterior\n"

#Posicionamos nuevamente el cursor en el caracter 0:
archivo_texto2.seek(0)

#Con el metodo writelines que reciba una lista reemplazamos el contenido por lo que hay en la lista:
archivo_texto2.writelines(lista_texto)

#Ovbiamente cerramos el archivo:
archivo_texto2.close()