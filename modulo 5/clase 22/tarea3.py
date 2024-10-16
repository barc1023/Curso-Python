 # crear una funcion que transforme de grados celcius a fahrenheit
 
celsius = int(input("ingrese su temperatuda en grado C°:  "))

def celsius_a_fshrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print(celsius_a_fshrenheit(celsius))