
# toda funcion lambda se puede convertir en una funcion normal
# son funciones anonimas "mas simples"
#


  # sintaxys

 # solo se recomienda para funciones que retorna un soolo valor 
sumar = lambda n1, n2: n1 + n2
print(sumar(3,5))


  # ejemplo 1
 
elevarcuadrado = lambda numero : numero * numero
print(elevarcuadrado(5)) 
 
 
 # recursivida
 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

 