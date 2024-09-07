 # crear un programa que pregunte el nom bre del producto y luego el costo y al final mostrar el nombre del producto y el precio con el descuento, el prograga se debe llamar aplicador de 35% de descuentoz

print('bienvenido a nuestra tienda online. ')
print('mi nombre es OLI tu ayudante personal, el dia de hoy quiero regalarte un descuento especial del 35% en todos los productos de la casa')
print('porfavor ingresar el nombre y precio del producto deseado y descubre su precio con descuento:')

produto =input("producto ") 
precio =float(input('precio ')) 

precio_nuevo = precio * 0.35

print(f" ¡HOLA! soy yo de nuevo, su producto seleccionado tiene un valor de: $/{precio} ,¡no te preocupes! OLI te ayudara con eso, Aqui lo tienes! &/{precio_nuevo:.2f} un precio especial solo para ti.")
print("fue un gusto poder ayudarte, espero poder verte otra vez. ¡OLI te desea buenas noches!")