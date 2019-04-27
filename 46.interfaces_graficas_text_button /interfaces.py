
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

#Se crea un StringVar() el cual me permite asignar una variable a nuestra caja de texto 'txt_nombre':
texto_nombre= StringVar()

#textvariable permite asociar 'texto_nombre' a nuestra caja de texto
txt_nombre= Entry(frame,textvariable=texto_nombre)
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

#Creando el label Informacion para nuestro text
lbl_txtInfo= Label(frame,text="Informacion")
lbl_txtInfo.grid(row=4,column=0,padx=10,pady=10)

#Para crear una caja de entrada de texto text basta con: las configuraciones funcionan como si fuera un input:
text_info= Text(frame,width=20,height=10)
text_info.grid(row=4,column=1,padx=10,pady=10)


#El widget text por si solo no maneja un scroll, para añadir un scroll funcional debemos crear un objeto de tipo
#Scrollbar, con comand y 'yview', primero asigno el scroll a el text_info y luego establezco visualizacion vertical
scroll_vertical= Scrollbar(frame, command=text_info.yview)

#con nsew conseguimos que le scroll se adapte al widget 'text_info'
scroll_vertical.grid(row=4, column=2,sticky="nsew")

#Para hacer que el posicionador de el escroll funcione correctamente usamos la propiedad 'yscrollcommand':
text_info.config(yscrollcommand=scroll_vertical.set,bg="orange",fg="white")


def  codigo_boton():
    #con set modificamos el contenido de la entrada de texto txt_nombre:
    texto_nombre.set("Cristian")



#Creando un boton con el texto 'Enviar' y asignando la funcion 'codigo_boton':
btn_envio= Button(ventana, text="Enviar", command=codigo_boton)

#Empaquetando el boton:
btn_envio.pack()



ventana.mainloop()
