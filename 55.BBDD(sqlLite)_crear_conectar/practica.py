
#Lo primero es importar el modulo que nos permite gestionar la base de datos de SQLITE:
import sqlite3

#Abriendo ó creando una base de datos en caso de que ésta no exista: y almacenandola en la variable 'mi_conexion':
mi_conexion= sqlite3.connect("mi_primer_base")


#Seguido debemos crear el cursor o puntero que nos permite manipular la base de datos:
cursor= mi_conexion.cursor()

#Luego utilizando dicho cursor debemos ejecutar la consulta:(La linea esta comentada porque ya fue ejecutada para crear la tabla):

#cursor.execute("CREATE TABLE PRODUCTOS(NOMBRE VARCHAR(30), PRECIO INTEGER, SECCION VARCHAR(20))")



#Vamos a insertar datos en nuestra base de datos (por ahora unos pocos):
cursor.execute("INSERT INTO PRODUCTOS VALUES('Arroz Maxi-Arroz',1800,'Granos')")

#Luego de ejecutar la, como dicha consulta realizará cambios estructurales en la tabla debemos confirmar la accion mediante:
mi_conexion.commit()


#Cerrar la conexion:
mi_conexion.close()