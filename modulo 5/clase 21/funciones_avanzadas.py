 # sintaxis
 
 # siempre empieza con la funcion (def) seguido del nombre que le darmos a la variable
def saludar():
    print("hola")
    
saludar("marko")

  # ejemplo 1
  
def multiplicar (num1, num2):
    resultado = num1 * num2
    return resultado

print(multiplicar(7,3))

   # ejemplo 2
   
def calcular (peso, altura):
    calculo = peso / (altura**2)
    return calculo

print(calcular(23,45))

   # ejemplo 3
   
def calcularMaxMin(lista):
    return (max(lista),min(lista))

valMax, valMin = calcularMaxMin(1,2,3,4,5,6,6,7,6)
print("el valor maximo es", valMax)
print("el valor minimo", valMin)