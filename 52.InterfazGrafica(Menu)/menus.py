from tkinter import *

ventana= Tk()

#Creamos una variable de tipo menú y la ubicamos dentro de la ventana
menu_principal= Menu(ventana)

#En la configuración asignamos el menú a la ventana raiz:
ventana.config(menu=menu_principal,width=300,height=300)

#Creamos las opciones de menú que tendrá nuestra opcion desplegable, este submenú se ubicará a su vez en menu_principal:
#tearoff elimina unas lineas punteadas que se agregan a cada submenú por defecto:
menu_archivo= Menu(menu_principal,tearoff=0)


#Si queremos agregar opciones nuestro menu lo haremos mediante:
menu_archivo.add_command(label='Nuevo')
#La siguiente linea agrega un separador a nuestras opciones:
menu_archivo.add_separator()
menu_archivo.add_command(label='Guardar')
menu_archivo.add_command(label='Guardar Como')
menu_archivo.add_separator()
menu_archivo.add_command(label='Cerrar')
menu_archivo.add_command(label='Salir')


#Opciones de menú de edición:
menu_edicion= Menu(menu_principal,tearoff=0)

menu_edicion.add_command(label='Copiar')
menu_edicion.add_command(label='Pegar')
menu_edicion.add_separator()
menu_edicion.add_command(label='Undo')
menu_edicion.add_command(label='Redo')


menu_herramientas= Menu(menu_principal)


menu_ayuda= Menu(menu_principal,tearoff=0)

menu_ayuda.add_command(label='Licencia')
menu_ayuda.add_command(label='Acerca De')


#Al hacer esto veremos que no basta con crear las opciones, debemos agregar la opción y el texto que se mostrará:
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_principal.add_cascade(label="Edicion", menu=menu_edicion)
menu_principal.add_cascade(label="Herramientas", menu=menu_herramientas)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)




ventana.mainloop()