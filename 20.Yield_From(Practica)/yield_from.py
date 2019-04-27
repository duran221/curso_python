
#Cuando en python vemos un asterisco anteponiendo al argumento significa que vamos a enviar varios argumentos o parametros
#NO sabemos cuantos, y que ademas los vamos a enviar en forma de tupla:
#Ejemplo de yield:
def devuelve_ciudades(*ciudades):

    for elemento in ciudades:

        for subelemento in elemento:
            yield subelemento


ciudades_devueltas= devuelve_ciudades("Bogota","Cali","Armenia","Pereira","Medellin")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print("****************************")


#Yield from me permite simplificar la estructura de ese for anidado que realizamos anteriormente, veamos:
def devuelve_ciudades2(*ciudades):

    for elemento in ciudades:

        yield from elemento


ciudades_devueltas2= devuelve_ciudades2("Bogota","Cali","Armenia","Pereira","Medellin")

print(next(ciudades_devueltas2))
print(next(ciudades_devueltas2))
print("****************************")