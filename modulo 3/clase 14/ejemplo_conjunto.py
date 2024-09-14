  # ejemplo 1

paises = ['mexico', 'argentina', 'panama', 'china', 'japon']
conjunto = set(paises)
conjunto.add('chile') # se usa (add)  para agregar un solo elemento y para agregar mas de uno se utiliza (update)
conjunto.remove('mexico') # se esta eliminando un elemento, tambien puede utilizarce (discard)

print(conjunto)

  # ejemplo 2

conjunto1 = {1,2,3,4}
conjunto2 = {2,4,6,8}

conjunto_1 = set(conjunto1)
conjunto_2 = set(conjunto2)

conjunto_unido = conjunto_1.union(conjunto_2)
print(conjunto_unido) # los datos repetidos se eliminaran

  # ejemplo 3

a = {1,2,3,4}
b = {2,4,6,8}

ca = set(a)
cb = set(b)

conjunto_u = ca.intersection(cb)

print(conjunto_u)