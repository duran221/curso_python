
from tkinter import *

ventana= Tk()

#Estamos indicando que vamos a almacenar numeros enteros, contrario de 'StringVar()':
varOpcion= IntVar()

"""Imprime por pantalla la opción seleccionada.

"""
def imprimir_valor():

    #Preguntando si la opción seleccionada corresponde a masculino:
    if(varOpcion.get()==1):

        informacion.config(text="Masculino")
    else:

        informacion.config(text='Femenino')

#Un simple titulo informativo
titulo_informativo= Label(ventana,text="Seleccione una opción").pack()

#El Radiobutton me permite seleccionar una Única opcion entre varias disponibles, mediante 'value' es posible gestionar lo que se selecciona:
Radiobutton(ventana, text="Masculino", variable=varOpcion, value=1, command=imprimir_valor).pack()

Radiobutton(ventana, text="Femenino", variable=varOpcion, value=2, command=imprimir_valor).pack()

informacion= Label(ventana)
informacion.pack()

ventana.mainloop()