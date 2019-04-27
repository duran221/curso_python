
#Realizando una funcion que me genere los primeros 'n' numeros pares:
#Funcion convencional
def pares(n):
    num=1
    lista=[]
    while(num<=n):
        lista.append(num*2)
        num+=1

    return  lista


print(pares(5))
print("**************************")

#Realizando el mismo proceso pero con una funcion generadora:

def pares2(n):
    num=1
    while(num<=n):
        #Usando la palabra reservada mediante la cual es posible retornar un objeto ITERABLE:
        yield num*2
        num+=1



#Como la funcion retorna un objeto iterable es necesario declararlo:
pares_objeto= pares2(6)

#Cuando el flujo llegue aqui invocara la funcion y esta quedara 'pausada hasta que sea llamada nuevamente'
print(next(pares_objeto))

print("Aqui hay mucho codigo")

print(next(pares_objeto))

print("Aqui hay mucho codigo")

print(next(pares_objeto))


