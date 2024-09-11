 #bucles anidados: un bucle dentro de otro bucle

fila = int(input('cuantas filas quieres?  '))
columna = int(input('cuantas columnas quieres?  '))
simbolo = input('ingrese un simbolo  ')

for i in range(fila):
    for j in range(columna):
        print(simbolo, end="")
    print()

 # syntaxis

for elemento_interno in coleccion_externa:
    for elementos_internos in coleccion_interna:
        print()#operaciones con elementos_externos y elementos_internos