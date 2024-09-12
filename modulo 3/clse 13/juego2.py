 #juego interactivo con while

jugadores = 2
intentos_permitidos = 3
numero_secreto = 7

jugador_actual = 1
while jugador_actual <= jugadores :
    print(f"jugador{jugador_actual}, intenta adivinar el numero secreto")
    intentos = 0
    while intentos < intentos_permitidos:
        intento = int(input(f"intento{intentos+1}: "))
        if intento == numero_secreto:
            print("¡correcto!")
            break
        else:
            print("¡incorrecto!")
        intentos -=1
    jugador_actual += 1
    print()