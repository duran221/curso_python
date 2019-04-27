import pickle
import io

class Persona():

    def __init__(self,nombre,genero,edad):

        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print(f"Se ha creado la persona con el nombre {self.nombre}")


    #Permite convertir en cadena de texto la informacion del objeto: es decir que al hacer un print del objeto muestra informacion
    #legible
    def __str__(self):
        #Nomenclatura especial usada para devolver las tres variables
        return "{} {} {}".format(self.nombre,self.genero,self.edad)


class ListaPersonas():

    personas=[]

    def __init__(self):
        #Se abre el archivo en modo de lectura y escritura:
        lista_de_personas= open("fichero_externo","ab+")

        #Se desplaza nuevamente el cursor hacia el inicio:
        lista_de_personas.seek(0)

        try:
            #Cada que se  llama al constructor se carga la variable personas con la informacion del archivo binario:
            self.personas= pickle.load(lista_de_personas)
            print("Se  cargaron {} personas del fichero externo ".format(len(self.personas)))

        except:
            print("El fichero está vacío")
        finally:
            #Cerrando y eliminando el archivo de memoria principal
            lista_de_personas.close()
            del (lista_de_personas)

    """Agrega una persona a la lista y le guarda en un archivo binario
    
    """
    def agregar_personas(self,p):
        #Una vez almacenada la persona en la coleccion
        self.personas.append(p)
        #Guardamos la persona en el fichero externo
        self.guardar_personas_fichero()


    def mostrar_personas(self):
        #Recorre la coleccion de personas mostrandolas
        for p in self.personas:

            print(p)

    """Metodo que permite guardar en un archivo externo una colección de personas
    
    """
    def guardar_personas_fichero(self):
        #Apertura del archivo en escritura binaria:
        lista_de_personas=open("fichero_externo","wb")

        #Haciendo la escritura del objeto sobre el archivo
        pickle.dump(self.personas,lista_de_personas)

        #Cerrado y borrado del archivo en memoria
        lista_de_personas.close()
        del (lista_de_personas)

    """Simplemente imprime la informacion del fichero externo
    
    """
    def mostrar_info_fichero(self):

        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)
            print("*******************")


lista_personas= ListaPersonas()

p= Persona("Sandra","Femenino",23)
lista_personas.agregar_personas(p)

p1= Persona("Aleja","Femenino",20)
lista_personas.agregar_personas(p1)

p2= Persona("Alex","Masculino",21)
lista_personas.agregar_personas(p2)

p3= Persona("Juana","Femenino",19)
lista_personas.agregar_personas(p3)

print("**************************")
lista_personas.mostrar_info_fichero()
