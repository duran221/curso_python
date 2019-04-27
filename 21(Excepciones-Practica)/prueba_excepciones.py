def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	#Esta estructura nos permite capturar errores en ejecucion y decidir que hacer con estos sin que se 'caiga' el programa
	#Su funcionamiento es muy similar a el de un 'if' y permite continuar el flujo de ejecucion en caso de generar errores
	try:
		# // retorna una division entera
		return num1//num2
	except ZeroDivisionError:
		print("No se puede realizar divisiones por cero")

op1=(int(input("Introduce el primer n�mero: ")))

op2=(int(input("Introduce el segundo n�mero: ")))		
	
operacion=input("Introduce la operaci�n a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operaci�n no contemplada")


print("Operaci�n ejecutada. Continuaci�n de ejec�ci�n del programa ")