
palabra= "Python"

for i in palabra:

    if(i=="h"):
        #La instruccion continue permite ignorar el contenido o saltar a la siguiente iteracion sin leer el resto del contenido
        continue

    print(i)

print("**************************")

#Contar cuantas letras 'i' tiene la palabra 'Pildoras informaticas'

palabra="Pildoras informaticas"
cont=0

for i in palabra:
    #Si el caracter a evaluar en la iteracion no es i, salte a la siguiente iteracion:
    if(i!="i"):
        continue
    else:
        cont+=1

print(f"El total de letras i encontradas es {cont}")


#Usamos pass cuando deceamos por ejemplo declarar una funcion sin codigo aún:
def funcion():
    pass


#Validando un correo electronico con 'else':
print("************************************")
email="cristian@gmail.com"
for i in email:

    #Si en cuentra un '@' no alcanzara a ingresar en el 'else':
    if(i=="@"):
        arroba=True
        break

#Luego de que todo el bucle se ejecute, ingresara en esta instruccion:
else:
    arroba=False


print(arroba)
