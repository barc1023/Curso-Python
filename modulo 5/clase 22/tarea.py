
 # crear una funcion que verifique si un numero es par o inpar
 
num1 = int(input("por favor ingrese un numero:  ")) 

def calcular(num1):
   
    if num1 %2 ==0:
        print(f"el numero: {num1} es par")
        
    else:
        print("el numero es impar")
        
    return calcular

calcular(num1)

  # crear una funcion que calcule el parametro 
  
ancho = int(input("ingrese el ancho de su rectangulo:  "))
altura = int(input("ingresse la altura de su rectangulo:  "))

def area_rectangulo(ancho,altura):
    resultado = ancho * altura
    return resultado

print(area_rectangulo(ancho, altura))
