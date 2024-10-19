'''
funcion args:

nos permite crer funciones sin ninguntipo de limite en parametro.

ventajas

-flexibilidad:  una funcion acepta cualuier cantida de argumentos

simplicidad: evita la sobrecarga de las funciones

reutilizacion: se puede utilizar muchas veces dentro de un programa

'''

 # ejemplo 1
 
def nuevo(*args):
    for arg in args:
        print(arg)
        
nuevo()


 # ejemplo 2
 
def sumar (*args):
    total= 0
    for i in args:
        total += i        
    return total       
        
print(sumar(3,6,7,8,2,3,8,9,0))


 # ejemplo 3
 
def numero_max(*args):
    return max(args) 

print(numero_max(3,6,1,9,7))