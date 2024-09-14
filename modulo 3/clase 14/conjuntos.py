 # los conjuntos son un tipo de coleccion donde los elemtos estan desordenados
 # no pueden haaber otro tipo de colecciones dentro de un conjunto
 # no pueden haber valores duplicados
 
      # syntaxis

conjunto = set()  # para crear un conjunto se debe iniciar con el comando (SET)
conjunto = {1,2,3,4,5}

conjunto.add(6) # se agregan los datos de forma desordenada

conjunto.discard(3) # se elimina el dato seleccionado

conjunto.clear() # se eliminan todos los datos dentro del conjunto

print(conjunto)