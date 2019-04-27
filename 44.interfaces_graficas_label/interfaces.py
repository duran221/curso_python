
#Importando la libreria de tkinter:

from tkinter import *

#Creando la ventana principal
ventana = Tk()

#Se crea el frame o panel para visualizar contenido:
frame= Frame(ventana,width=500,height=500)

#Es muy importante empaquetar el Frame:
frame.pack()

#Un label puede contener muchos atributos, tambien se puede mostrar imagenes en el
texto1= Label(frame,text="Hola este es un label",bg="blue", fg="white", font=("Comic Sans MS",18))
texto1.place(x=100,y=200)

#Si no vas a usar mas adelante el label tambien puedes ovbiar la escritura anterior de la siguiente manera:

Label(frame,text="Hola2",bg="Red", fg="white").place(x=50,y=50)


#Tambien si lo deceas puedes agregar imagenes en formato gif y png de la siguiente manera:

imagen= PhotoImage(file="iconos/python.png")

Label(frame, image=imagen).place(x=200,y=250)

#Ejecutando el bucle que permite mostrar la ventana
ventana.mainloop()
