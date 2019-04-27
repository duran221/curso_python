#Importando todos los metodos de la libreria tkinter:

from tkinter import *

#Inicializando o creando la ventana:
ventana= Tk()

#Añadiendo un titulo a la ventana
ventana.title("Ventana de pruebas")

#Impedir Redimencionar una ventana: recibe dos parametros booleanos 'width' y 'height',ambos en cero no permite redimencionar,
#En uno admite redimencionar, TAMBIEN PUEDE USARSE TRUE O FALSE:
ventana.resizable(True,True)

#Asignar tamaño a la ventana:
#ventana.geometry("650x350")

#El metodo config incluye varios parametros de configuracion entre los cuales podemos incluir el background de la pagina:
ventana.config(bg="#ffffff")

#Un frame nos permite dar usos como lienzo par ubicar distintos elementos tales como botones,cuadros de texto etc.etc
frame= Frame()


#Empaquetando el frame, OBLIGATORIO, el metodo tambien admite varios parametros:
frame.pack(side="right",anchor="n")

#Podemos indicar que el frame se expanda en ambas direcciones, en 'x' o en 'y'
#frame.pack(fill="both",expand="True")

#Se puede manejar distintas configuraciones tales como el tamaño del frame,color de fondo etc, recordar que la ventana
#Tk se adapta al tamaño asignado en el frame.
frame.config(bg="red")
frame.config(width="600",height="500")

#Cambiando el grosor del borde que por defecto se define en 0
frame.config(bd=10)

#Aplicando un tipo de borde especial
frame.config(relief="sunken")

#Cambiando el cursor por defecto de nuestro frame:
frame.config(cursor="pirate")

#Para que la ventana sea visible debe ser ejecutada en una especie de bucle infinito, para eso se usa mainloop():
#Siempre debe estar al final:
ventana.mainloop()

#Cabe aclarar que se puede utilizar los mismos metodos con la ventana raiz.