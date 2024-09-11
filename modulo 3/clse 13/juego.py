  # haremos una piramide pidiendo al usuario un numero y un simbolo

fila = int(input('introdusca el numero de fila que desea:  '))
simbolo = input('introduce el simbolo que desees:  ')

for i in range(1, fila + 1): # bucle externo, del 1 hata el numero que se coloque
    for j in range(i):   # bucle interno, imprimira (i) simbolos
        print(simbolo, end="")
    print()   # salta de linia al final de cada linea