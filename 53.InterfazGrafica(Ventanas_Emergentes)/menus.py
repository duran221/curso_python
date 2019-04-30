from tkinter import *
#El modulo messagebox debe ser importado por de aparte:
from tkinter import messagebox

ventana= Tk()

#Se puede crear ventanas emergentes de la siguiente manera:
#Creamos una funcion la cual va a desencadenar una ventana de información:
def mostrar_info():
    #Mostrando una ventana emergente de información:
    #Primer parametro:titulo
    #Segundo parametro: texto del cuadro de información
    messagebox.showinfo('Procesador de Cristian','Procesador de textos version 8.1')

def licencia_estado():
    #Mostrando una ventana de advertencia:
    messagebox.showwarning('Licencia','Tipo de licencia GNU')


def cerrar_programa():
    #Tambien podemos realizar acciones mediante la opción 'askquestion' la cual permite asignada a una variable tomar
    #decisiones posteriormente:
    valor=messagebox.askquestion('Salir','¿Deceas salir de la aplicación?')

    #Al seleccionarse la opcion 'si', cerrar la ventana:
    if valor=="yes":
        ventana.destroy()


def finalizar_aplicacion():

    #A diferencia de la opción anterior esta opción arroja valores booleanos True o False:
    valor= messagebox.askokcancel('Salir','¿Deceas salir de la aplicacion?')

    if valor:
        ventana.destroy()

def nuevo_documento():
    #La ventana ofrece las opciones reintentar y cancelar la cual puede ser asignada a una variable
    valor= messagebox.askretrycancel('Reintentar','No se ha podido crear el documento')

    if valor:
        messagebox.showerror('Error','Imposible reintentar')


#Creamos una variable de tipo menú y la ubicamos dentro de la ventana
menu_principal= Menu(ventana)

#En la configuración asignamos el menú a la ventana raiz:
ventana.config(menu=menu_principal,width=300,height=300)

#Creamos las opciones de menú que tendrá nuestra opcion desplegable, este submenú se ubicará a su vez en menu_principal:
#tearoff elimina unas lineas punteadas que se agregan a cada submenú por defecto:
menu_archivo= Menu(menu_principal,tearoff=0)


#Si queremos agregar opciones nuestro menu lo haremos mediante:
menu_archivo.add_command(label='Nuevo', command=nuevo_documento)
#La siguiente linea agrega un separador a nuestras opciones:
menu_archivo.add_separator()
menu_archivo.add_command(label='Guardar')
menu_archivo.add_command(label='Guardar Como')
menu_archivo.add_separator()
menu_archivo.add_command(label='Cerrar',command=finalizar_aplicacion)
menu_archivo.add_command(label='Salir',command=cerrar_programa)


#Opciones de menú de edición:
menu_edicion= Menu(menu_principal,tearoff=0)

menu_edicion.add_command(label='Copiar')
menu_edicion.add_command(label='Pegar')
menu_edicion.add_separator()
menu_edicion.add_command(label='Undo')
menu_edicion.add_command(label='Redo')


menu_herramientas= Menu(menu_principal)


menu_ayuda= Menu(menu_principal,tearoff=0)

menu_ayuda.add_command(label='Licencia',command=licencia_estado)
#Como ya es conocido mediante el parametro 'command' llamamos la función que muestra la ventana emergente:
menu_ayuda.add_command(label='Acerca De',command=mostrar_info)


#Al hacer esto veremos que no basta con crear las opciones, debemos agregar la opción y el texto que se mostrará:
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_principal.add_cascade(label="Edicion", menu=menu_edicion)
menu_principal.add_cascade(label="Herramientas", menu=menu_herramientas)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)




ventana.mainloop()