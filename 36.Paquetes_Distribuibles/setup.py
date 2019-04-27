
#1.Debes importar la funcion setup del modulo setuptools, en caso de que genere error debes instalar el modulo:
from setuptools import setup

#2.Usamos la funcion y como argumentos ingresamos lo siguiente:
setup(
    #Especificando el nombre del paquete
    name="paquete_calculos",
    #La version de distribucion
    version="1.0.0",
    #Una breve descripcion del paquete que estamos distribuyendo
    description="Paquete de redondeo y potencia",
    #Por supuesto, los creditos, el autor
    author="Cristian Duran",
    #una direccion de correo electronico
    author_email="cristianfernandoduran@gmail.com",

    url="no_hay.com",
    #Propiedad mas IMPORTANTE, debemos especificar donde se encuentra el paquete o subpaquete que queremos empaquetar:
    #El primer elemento es el nombre del paquete,En segundo lugar la ruta del subpaquete escribiendo la ruta completa:
    packages=["calculos","calculos.operaciones_matematicas.redondeo_potencia"]


)


#3. Para empaquetar nuestros archivos abrimos una consola y localizamos la ruta donde se encuentre el archivo 'setup.py'
#creado previamente:

#4. Para crear el paquete vasta con teclear lo siguiente: python3 setup.py sdist
#5. En el directorio creará una carpeta dist, esa carpeta contiene el paquete que sera distribuido.

#6. Para instalar el paquete basta con abrir el terminal en la ruta donde tenemos nuestro paquete y teclear lo siguiente:
# pip3 install nombre_paquete

#Ya puedes usar el paquete
#
#Si todo ha ido bien ya puedes usar tus librerias desde cualquier archivo que lo requiera ya que esta instalado en tu ordenador:

#Desinstalar el paquete:
# pip3 uninstall nombre_paquete