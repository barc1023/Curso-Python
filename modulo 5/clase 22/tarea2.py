  # crear una funcion que calcule el parametro 
  
ancho = int(input("ingrese el ancho de su rectangulo:  "))
altura = int(input("ingresse la altura de su rectangulo:  "))

def area_rectangulo(ancho,altura):
    resultado = ancho * altura
    return resultado

print(area_rectangulo(ancho, altura))