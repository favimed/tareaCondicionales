primerNumero = int(input("Escribe el primer numero: "))
segundoNumero = int(input("Escribe el segundo numero: "))
tercerNumero= int(input("Escribe el tercer numero: "))
if (primerNumero > segundoNumero and primerNumero > tercerNumero):
    print("El numero más grande es:", primerNumero)
elif(tercerNumero > segundoNumero and tercerNumero > primerNumero):
    print("El numero más grande es:", tercerNumero)
elif (primerNumero == segundoNumero == tercerNumero):
    print("Los tres numeros son iguales")
else:
    print("El numero más grande es:", segundoNumero)
    
    