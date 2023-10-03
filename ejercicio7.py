edad = int(input("¿Cuantos años tienes?: "))
if (edad >= 16):
    ingresos = int(input("¿Cuanto ganas al mes?: "))
    if (ingresos >= 1000):
        print ("Tienes que tributar")
    else:
        print ("No tienes que tributar")
else:
    print ("No eres lo suficientemente mayor")