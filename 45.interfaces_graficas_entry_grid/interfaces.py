
#Importando la libreria tkinter
from tkinter import *

#Creando la ventana
ventana= Tk()

#Creando el panel o Frame
frame= Frame(ventana, width=500,height=500)

#Importante-Empaquetar el frame:
frame.pack()

#En lugar de pack() o place() se es posible añadir el metodo grid() el cual nos permite ubicar los elementos como
#si se tratase de una matriz manejando posiciones como (0,0) (0,1) etc..

lbl_nombre= Label(frame,text="Nombre")
lbl_nombre.grid(row=0,column=0,sticky="w",padx=10,pady=10)

txt_nombre= Entry(frame)
txt_nombre.grid(row=0,column=1,padx=10,pady=10)

#El metodo config nos permite gestionar las mismas opciones que posee el widget Label:
txt_nombre.config(fg="red", justify="center")


lbl_apellido= Label(frame,text="Apellido")
lbl_apellido.grid(row=1,column=0,sticky="w",padx=10,pady=10)

txt_apellido= Entry(frame)
txt_apellido.grid(row=1,column=1,padx=10,pady=10)

lbl_edad= Label(frame,text="Edad")
lbl_edad.grid(row=2,column=0,sticky="w",padx=10,pady=10)

txt_edad= Entry(frame)
txt_edad.grid(row=2,column=1,padx=10,pady=10)


lbl_contra= Label(frame,text="Contraseña")

#'sticky' me permite alinear el texto del label con posiciones cardinales: n,s,e,w (en inglés)
lbl_contra.grid(row=3,column=0,sticky="w",padx=10,pady=10)

txt_contra= Entry(frame)
txt_contra.grid(row=3,column=1,padx=10,pady=10)
#Es posible manejar un campo de contraseñas indicando al metodo config el simbolo que se decea mostrar:
txt_contra.config(show="-")

ventana.mainloop()
