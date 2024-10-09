 # repaso de entrada y salida
 
nombre = input("cual es tu nombre?  ")

print(f"es un placer conocerte, {nombre}")

 # formateo de cadenas 
 
# ejemplo 1
 
nombres= "juan" # para string s
edad = 30 # para los enteros d y para los flotantes f

  # el operador % llama a una variable, tambienhay que poner que tipo de dato es
print("nombres: %s , edad: %d" %(nombre, edad))
  # imprimir con formateo de cadena con operador
  
# ejemplo 2
  
   # ulizar el operador .format()
nombr = " juan "
edd = 23

print("nombr : {}, edd : {}".format(nombr, edd))

# ejemplo 3

  # sw utiliza el formati .1f para indicar cuantos numero se quieran mostrar
precio = 800.95
print(f"el precio de una laftop es: {precio:.1f}")

# ejemplo 4

gasolina = 0.874
print(f" usted compro 7 litros, cada litro esta a {gasolina:.2f}")

# ejemplo 5

nombre = "fernando"
puntos = 12000

print(f"{nombre:>10} | {puntos:<10}")
