
#Importando la libreria Tkinter
from tkinter import *

ventana= Tk()

mi_frame= Frame(ventana)

mi_frame.pack()

#Cadena o String asociado a la informacion que se muestra en pantalla:
numero_pantalla=StringVar()

#-----------------Variables globales:
operacion=''

#Variable donde se va almacenando el resultado de las sumas:
resultado=0

#-------------------Funciones:----------------------

"""Recibe un simbolo, ya sea numero o signo y lo concatena a la cadena.

    @:param {num}: Botón o numero pulsado    
    
"""
def numero_pulsado(num):

    global operacion

    #Preguntando si el usuario ha pulsado el botón suma:
    if(operacion!=''):
        #Escriba el nuevo numero
        numero_pantalla.set(num)

        #Para que al teclear el siguiente número empiece a concatenar:
        operacion=''

    else:
        #Concatene los numeros
        numero_pantalla.set(numero_pantalla.get() + num)

#----------------------------------Función Suma--------------------------
"""
    En cargado de realizar una suma cada vez que es pulsado el boton '+'.
    
    @:param {num}: Numero que se encuentra actualmente en pantalla.

"""
def suma(num):

    #Diciendole que tenga en cuenta que voy a operar con la variable global operacion:
    global operacion

    global resultado

    operacion='suma'

    #Sumando nuestro resultado,recordar que 'num' debe ser convertido a entero con 'int'
    resultado+=int(num)

    #Escribiendo el resultado en pantalla:
    numero_pantalla.set(resultado)



#-----------------------------------Función Obtener_Resultado-----------------------------

"""Permite mostrar en pantalla el resultado de la operación indicada.

"""
def el_resultado():

    global resultado

    numero_pantalla.set(resultado+int(numero_pantalla.get()))

    #El resultado debe ser reseteado para que al pulsar '+' nuevamente, éste no produzca un comportamiento no deceado
    resultado=0




#Creando y configurando la pantalla de nuestra calculadora:
pantalla_calculadora= Entry(mi_frame,textvariable=numero_pantalla)
#Con columnspan se le indica a la pantalla que ocupe 4 columnas para que el diseño no se nos dañe al añadir la botonera:
pantalla_calculadora.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla_calculadora.config(background="black",fg="#03f943",justify="right")

#Fila 1 de botones de numeros y signos de la calculadora:
boton_7= Button(mi_frame, text="7", width=3,command=lambda:numero_pulsado("7"))
boton_7.grid(row=2,column=1)

boton_8= Button(mi_frame, text="8", width=3,command=lambda:numero_pulsado("8"))
boton_8.grid(row=2,column=2)

boton_9= Button(mi_frame, text="9", width=3,command=lambda:numero_pulsado("9"))
boton_9.grid(row=2,column=3)

boton_dividir= Button(mi_frame, text="/", width=3,command=lambda:numero_pulsado("/"))
boton_dividir.grid(row=2,column=4)

#Fila 2 de botones de numeros y signos de la calculadora:


#Si al método que nececesitamos llamar en 'command' le agregamos un parentesis python interpreta que se debe ejecutar
#la función y asignar el resultado en command, cosa que por ahora no queremos y que se soluciona con funciones lambda:

#boton_4= Button(mi_frame,text="4",width=3,command=numero_pulsado("4"))


boton_4= Button(mi_frame,text="4",width=3,command=lambda:numero_pulsado("4"))
boton_4.grid(row=3,column=1)

boton_5= Button(mi_frame,text="5",width=3,command=lambda:numero_pulsado("5"))
boton_5.grid(row=3,column=2)

boton_6= Button(mi_frame,text="6",width=3,command=lambda:numero_pulsado("6"))
boton_6.grid(row=3,column=3)

boton_multiplicar= Button(mi_frame,text="X",width=3,command=lambda:numero_pulsado("X"))
boton_multiplicar.grid(row=3,column=4)


#Fila 3 de botones de numeros y signos de la calculadora:

boton_1= Button(mi_frame,text="1",width=3,command=lambda:numero_pulsado("1"))
boton_1.grid(row=4,column=1)

boton_2= Button(mi_frame,text="2",width=3,command=lambda:numero_pulsado("2"))
boton_2.grid(row=4,column=2)

boton_3= Button(mi_frame,text="3",width=3,command=lambda:numero_pulsado("3"))
boton_3.grid(row=4,column=3)

boton_resta= Button(mi_frame,text="-",width=3,command=lambda:numero_pulsado("-"))
boton_resta.grid(row=4,column=4)


#Fila 4 de botones de numeros y signos de la calculadora:

boton_0= Button(mi_frame,text="0",width=3,command=lambda:numero_pulsado("0"))
boton_0.grid(row=5,column=1)

boton_punto_d= Button(mi_frame,text=".",width=3,command=lambda:numero_pulsado("."))
boton_punto_d.grid(row=5,column=2)

boton_igual= Button(mi_frame,text="=",width=3,command=lambda:el_resultado())
boton_igual.grid(row=5,column=3)

boton_suma= Button(mi_frame,text="+",width=3,command=lambda:suma(numero_pantalla.get()))
boton_suma.grid(row=5,column=4)



ventana.mainloop()

