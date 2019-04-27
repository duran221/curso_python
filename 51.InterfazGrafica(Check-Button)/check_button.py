from tkinter import *

#Creación de la ventana:
ventana = Tk()

ventana.title("Check-Buttons")

#Creando una imagen, como la ruta se encuentra a la altura de el proyecto no es necesario especificar ruta:
imagen= PhotoImage(file='avion.png')

#Meto la imagen dentro de un contenedor tipo label para luego poder manipular su ubicación si es necesario:
Label(ventana,image=imagen).pack()


#Estas variables son necesarias para validar si nuestros check-buttons estan seleccionados:

playa= IntVar()
montana= IntVar()
turismo_rural= IntVar()


#Creación de la función que me permite realizar algo dependiendo de si se seleccionan o no las opciones:
def info():

    #Cadena en la cual voy a concatenar las opciones:
    texto=''
    if(playa.get()==1):
        texto+=' Playa'

    if(montana.get()==1):
        texto+=' Montaña'

    if(turismo_rural.get()==1):
        texto+=' Turismo Rural'

    #Mostrando la información
    lbl_info.config(text=texto)

#Para dar independencia de la imagen sobre nuestros check-button vamos a crear un frame:

frame= Frame(ventana)
frame.pack()

Label(frame,text='Elige destinos',width=50).pack()


#Creando nuestro primer check-button, es muy importante empaquetarlo:
#onvalue: el valor que asume la variable cuando se selecciona el check-button
#offvalue: el valor que asume la variable cuando no está seleccionada
#command: Determina cuando es pulsado el botón la acción que se realiza.
check1= Checkbutton(frame,text='Playa', variable=playa,onvalue=1,offvalue=0,command=info).pack()

check2= Checkbutton(frame,text='Montaña',variable=montana,onvalue=1,offvalue=0,command=info).pack()

check3= Checkbutton(frame, text='Turismo Rural',variable=turismo_rural,onvalue=1,offvalue=0,command=info).pack()


#Este label nos permite mostrar las opciones seleccionadas:
lbl_info= Label(frame)
lbl_info.pack()


#Hilo de ejecución:
ventana.mainloop()