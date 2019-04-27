
#Existen varios metodos del objeto String desde los cuales podemos facilitarnos la vida a la hora de resolver ciertos
#problemas con string. Vamos a resolver el ejercicio propuesto en el pdf:


#El ejercicio podria realizarce de manera mas optima, pero usaremos varios metodos para ilustrar:
while(True):
    condicion=False
    direccion = (input("Introduce tu dirección de correo electronico:"))

    #find: me informa en que posicion se encuentra una subcadena, si no la encuentra retorna '-1'
    if(direccion.find("@") != -1):

        #count: informa cuantas veces se encuentra una subcadena en el texto ingresado
        if(0<direccion.count("@")<2):

            #endswith me informa si la cadena finaliza en la subcadena especificada:
            if(not direccion.endswith("@") and direccion.find("@")!=0):

                print("Has introducido la direccion correcta")
                break

    print("Has introducido una direccion incorrecta: por favor vuelve a introducir un dato")

