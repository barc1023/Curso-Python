
 #practica 1
productos_del_super = ["arroz", "carne", "embutidos", "leche", "miniestra"]
print(productos_del_super)

 #practica 2
productos_del_super2 = ["cereales", "lacteos", "granos", "carnes",["embutidos", "vegetales"]]
print(productos_del_super2[4][1])

#practica 3
cosas_por_hacer = ["lavar", "fregar", "barrer", ["doblar ropa", "limpiar baño"]]
print(cosas_por_hacer[3][0])

 #practica 4 (añadir un elemento nuevo usando .appernd)
lista = ["pollo", "arrez", "carne"]
lista.append('leche')
print(lista)

 #practica 5 (añadir varios elementos usando .extend)
lista_nueva = ["arroz", "pollo"]
lista_nueva.extend(["carne", "lacteos", "cereales"])
print(lista_nueva)
print(lista_nueva[2], lista_nueva[4])

 # practica 6 (eliminar un elemento de la lista usando del)
otra_lista = ["papel", "lapiz", "borrador", "hojas"]
del otra_lista[3] # del otra_lista[0 : 2]
print(otra_lista)
