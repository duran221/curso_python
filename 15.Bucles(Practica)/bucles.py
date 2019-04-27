
#Se puede comprobar si un correo electronico tiene el formato correcto de una manera muy sencilla:

email= "cristian@gmail.com"
contador=0

#Podemos recorrer una cadena de texto de la siguiente manera:
for i in email:
    if(i=="@" or i=="."):
        contador+=1

if(contador>=2):
    print("Formato correcto")

else:
    print("Formato incorrecto")

print("********************************")



#Haciendo uso de 'range':
for i in range(5):
    print(i)

print("********************************")


for i in range(2,5):
    print(i)

print("********************************")
