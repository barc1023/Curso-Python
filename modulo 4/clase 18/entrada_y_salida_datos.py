 
 #crear un programa que pida nombre y apellido al usuario
 
print('¡buenas noches!, porfavor ingrese los siguientes datos')

nombre = input('ingrese su nombre:  ')
apellido = input('ingrese su apellido:  ')
edad = int(input('ingrese su fecha de nacimiento.  '))

def calcular_edad(añoactual, edadnacimiento):
    return añoactual- edadnacimiento

print(f"tu nombre es: {nombre} {apellido} y tu edad es {calcular_edad(2024, edad)}")