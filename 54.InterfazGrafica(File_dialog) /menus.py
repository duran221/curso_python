from tkinter import *

#Importando el modulo de tkinter necesario para abrir archivos:
from tkinter import filedialog


ventana= Tk()

#La función que me permite invocar la ventana para abrir archivos:
def abrir_archivo():
    #filedialog=me permite mostrar una ventana para abrir ficheros el cual recibe los siguientes parametros:
    #title: Un titulo
    #initialdir: (opcional) una ruta desde la cual empezaria a buscar la ventana
    #filetypes: Una tupla con los tipos de archivos que mostraria nuestra ventana de apertura de archivos.
    archivo= filedialog.askopenfilename(title="Abrir",initialdir='/home',filetypes=(("Archivo de Texto","*.txt"),("Todos los archivos","*.*")))


    #Por ultimo en la variable 'archivo' se almacena la ruta de el archivo que hemos seleccionado para posteriormente ejecutar alguna accion:
    print(archivo)



Button(text='Abrir', command=abrir_archivo).pack()

ventana.mainloop()


