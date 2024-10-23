
 # crear una funcion lambda que tenga tres argumentos, multiplicara los primeros dos y el resultado lo dividira x el tercero
 
operaciones = lambda b, s, r : (b * s) / r
print(operaciones(3, 5, 2))


 # ejercico 3
 
 # verificar si un numero es par
 
verificador = lambda x :  x % 2== 0
 # para saber si es inpar se utiliza la siguiente asignacion(!=)
print(verificador(34))

 # ejercicio 4
 # funcion lambda con condiciones
 
mayor = lambda a,b : a if  a>b else b
print(mayor(23,24))