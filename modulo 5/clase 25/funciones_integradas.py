  # practica

print('buenas noches, adivina un numero del 1 al 10: ')
num = int(input('numero:  '))
numero = 7

while True:
    
    if num != numero:
        print(f"el numero selccionado es el: {num}, lastimosamente este no es el numero secreto! ")
        
    elif num == numero:
        print("feliciodades, has escpgido el numero ganador")
    break

  # clase
  
num_str = ('42')
num_int = int(num_str)
num_float = float(num_str)
text = str(8)
booleano = bool(1)

  # funciones matematicas 
  
abs()  # transforma culaquier numero negativo o positivo en un numero apsoluto
round() # redondea cualquier numero decimal 
max()  # para buscar el numero mayor
min()  # para buscar el numero menor
sum()  # para sumar elementos de lista
sorted()  # para ordenar elementos de mayor a menor
reversed()  #para revertir el flujo 
enumerate()  # para indicar el indice y el valor de los elementos 
type() # muestra el tipo de dato