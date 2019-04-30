#Lo primero es importar el modulo que me permite gestionar bases de datos:

import sqlite3

#Segundo crear ó conectar a una base de datos:

conexion= sqlite3.connect("mi_base_datos")

#Creando un cursor para ejecutar las consultas:
cursor= conexion.cursor()

#Ejecutando la consulta que creará la tabla (se comenta porque solo se ejecutará la primer vez)
#cursor.execute('CREATE TABLE PRODUCTOS (NOMBRE VARCHAR(30), PRECIO INTEGER, SECCION VARCHAR (20))')

###################################Insertar Datos#######################################################


"""
Quitar los comentarios de triple linea para ver el funcionamiento de las inserciones:

#Para realizar varias inserciones podemos crear una lista de TUPLAS, dichas tuplas contienen los datos que vamos a insertar:

lista_productos= [
    ('ACER K10',450000,'INFORMATICA'),
    ('LECHE COLANTA',2000,'LACTEOS'),
    ('LICUADORA UNIVERSAL',50000,'ELECTRODOMETICOS'),
    ('ARROZ ROA x 1000gr',3400,'GRANOS')

]


#Luego insertando nuestra lista de productos en la base de datos con executemany (varios):
#La consulta empieza común y corriente, los interrogantes implican las columnas en las cuales se realizarán las inserciones
#como segundo parametro la lista de productos que se decea insertar:

cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",lista_productos)


"""

###################################Obtener Datos#######################################################

#Para visualizar la información traida desde nuestra base de datos basta con realizar una simple consulta:
cursor.execute("SELECT * FROM PRODUCTOS")

#La consulta es ejecutada, sin embargo para obtener una LISTA de nuestros productos usamos el 'fetchall' similar a php:
lista_productos= cursor.fetchall()

#Imprimiendo los resultados:
print(lista_productos)


#Pero lo anterior me lista la información de una manera muy desorganizada, podemos recorrer esta lista con un for e imprimir lo que necesitamos:
print("**********************************************************************************")
for producto in lista_productos:
    #Como lista_productos contiene una tupla, se accede a las posiciones de dichas tuplitas:
    print(f'Nombre: {producto[0]} , Sección: {producto[2]}')





#IMPORTANTE, CONFIRMAR LOS CAMBIOS PARA QUE ÉSTOS SE REALICEN SOBRE LA BASE DE DATOS:
conexion.commit()

#Se cierra la conexión:
conexion.close()