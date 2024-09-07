 #se usa (elif) cuando se encuentran varias opciones

numero = int(input("introduzca un nimero: "))

if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es cero")