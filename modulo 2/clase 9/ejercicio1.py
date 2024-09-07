 #crear un programa que nos pida 4 notas y luego nos de el promedio
print('sea bienvenido a nuestra calculador de promedios')
print('por favor ingrese sus calificaciones:')

nota1 = int(input('ingrese su primera nota: '))
nota2 = int(input('ingrese su segunda nota: '))
nota3 = int(input('ingrese su tercera nota: '))
nota4 = int(input('ingrese su cuarta nota: '))

calificacion_final = (nota1+nota2+nota3+nota4) / 4

print("su promedio final es", calificacion_final )
print("gracias por usar nuestro programa, ¡tenga un buen dia!")