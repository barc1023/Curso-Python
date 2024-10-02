nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ") 

if edad.isdigit() and int(edad) > 18:
    edad = int(edad)
    print(f"Hola {nombre}, hemos verificado tu edad, porfavor disfrute de nuestro sitio web.")
else:
    print("lo sentimos, este sitio web esta dedicado a personas mayores de edad, lo invitamos a abandonar este sitio!")
 
 # la funcion strip verifica caracter por caracter nuestra cadena de texto
correo = input('introduce tu correo electronico: ').strip()

 # verifica si contiene @
 
if "@" in correo and "." in correo:
    print(f"hola {nombre}, tienes {edad} años y tu correo electronico es {correo}")
    
else:
    print('porfavor introduce un correo electronico valido.')