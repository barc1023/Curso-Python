 # crear una funcion que sume todos los numeros que brinde el ususario
 
print('ingrese los numeros que desea sumar: ')
print('recuerde separar lus numero con una ","')

numeros = input('numeros:  ').split(",")
numeros = [int(num) for num in numeros]

def sumar(*args):
    total = 0
    for i in args:
        total += i
    print(f" el resultado de la suma es: {total}") 
    
sumar(*numeros)   
    