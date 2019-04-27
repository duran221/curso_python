#Importando todos los metodos de la libreria tkinter:

from tkinter import *

#Inicializando o creando la ventana:
ventana= Tk()

#Añadiendo un titulo a la ventana
ventana.title("Ventana de pruebas")

#Impedir Redimencionar una ventana: recibe dos parametros booleanos 'width' y 'height',ambos en cero no permite redimencionar,
#En uno admite redimencionar, TAMBIEN PUEDE USARSE TRUE O FALSE:
ventana.resizable(0,0)

#Asignar tamaño a la ventana:
ventana.geometry("650x350")

#El metodo config incluye varios parametros de configuracion entre los cuales podemos incluir el background de la pagina:
ventana.config(bg="#ffffff")

#Para que la ventana sea visible debe ser ejecutada en una especie de bucle infinito, para eso se usa mainloop():
#Siempre debe estar al final:
ventana.mainloop()