 # ejemplo del video
 
def multiplicar(a,b): # se crea la funcionmultiplicar
    return a*b  #  se agregan las intrucciones

resultado = multiplicar(24,5) + 4 # se puede jugar con la funcion

print(f"mi edad es: {resultado}") # se imprime la funcion con una cadeda de texto

 # ejemplo de la clase 
 
def sumas(a,b):  # funciom para sumar
    respuesta = a+b
    return respuesta

suma = sumas(13,5)
print(suma)

  # ejemplo 2
  
def operaciones(a,b):
    suma = a + b
    resta = a - b
    multipl0 = a * b
    return suma, resta, multipl0

resultado_suma, resultado_resta, resultado_multiplo = operaciones(2,7)
print(resultado_suma)
print(resultado_multiplo)
print(resultado_resta)