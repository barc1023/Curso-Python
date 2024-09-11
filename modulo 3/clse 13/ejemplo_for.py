        # ejemplo 1

nombres = ['ana', 'juan', 'pedro']

for nombre in nombres:  # se crea una nueva variable llamada (nombre)
    print(f"las letras del nombre: {nombre}")
    for letras in nombre:   # se crea la variable (letras) y trabajara dentro de la variable (nombre)
        print(letras) 


        # ejemplo 2

frutas = ['manzana', 'pera', 'uvas']
colores = ['rojo', 'verde']

for fruta in frutas: # bucle externo
    for color in colores:  # bucle interno
        print(f"{fruta} de color {color}")