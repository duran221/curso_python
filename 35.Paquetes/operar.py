
#Lo primero es indicar que en la carpeta de cada PAQUETE se debe incluir un archivo adicional '__init__.py' es OBLIGATORIO INCLUIRLO.

#Crear los directorios incluyendo el archivo anteriormente y el modulo a ser utilizado.

#Para importar desde un paquete basta con hacer lo siguiente:

from operaciones_matematicas.operaciones_basicas.operaciones_basicas import sumar

#Otra forma bastante interesante de importar un archivo COMPLETO:
import operaciones_matematicas.redondeo_potencia.redondeo_potencia as operacion

#Importando todos los metodos del modulo:
from operaciones_matematicas.operaciones_basicas.operaciones_basicas import *

sumar(5,1)

operacion.redondeo(8.156)

multiplicar(9,5)

