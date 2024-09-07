 # operadores y expresiones

 # ((b*b) - (4*A*c)) / (2 * a)

a = float(input("ingrese a:  "))
b = float(input("ingrese b:  "))
c = float(input("ingrese c:  "))

expr = float (((b*b) - (a*a*c)) / (2*a))
print(expr)

 #los operadores se relacionan con los signos (+, -, /, *), tambien los relacionales, opeadores logicos 

a = 1
b = 2
print (a >=b)

 # ejemplo 2

x = 10
x += 5
print(f"el valor de x despues de 'x += 5' es: {x}" )
 
 #operadores unarios 'son los que rabajan con unidades'

a = 5
print( a ++ 1) #esta incrementando
#print( a -= 3) #esta decrementando
print( a ** 3) #esta elevando a la potencia
print( a ** (1/2)) #para buscar la raiz cuadrada

 # las xpreciones son combinacion de operadores y variables
