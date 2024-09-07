  # estructura de datos: lista
'''
mi_lista = ["panamá", 12 , 0.15 , true ]

provincias = ["bocas del toro", "panama oeste", "chiriqui"]

numeros_favoritos = [7, 6, 5, 2, 9]      
'''

 #ejemplo# 1
comidas_favoritas = ["arroz con pollo", "sopa de gallina dura", "pizza", "hamburguesa", "papas fritas con pollo asado"]
print(comidas_favoritas[-1]) # tambien usamos: "[1:4]" para hacer slicing de las tres del centro.

 #ejemplo# 2
comidas_favoritas = ["arroz con pollo", "sopa de gallina dura", "pizza", "hamburguesa", "papas fritas con pollo asado"]
comidas_favoritas[0] = "sushi" #remplazar cualquier elemento de la lista.
print(comidas_favoritas)

 #como eliminar un elemto de la lista
comidas_favoritas = ["arroz con pollo", "sopa de gallina dura", "pizza", "hamburguesa", "papas fritas con pollo asado"]
del comidas_favoritas[2] #del(delete) se utiliza para eliminar unelemento seleccionado.
print(comidas_favoritas)

 #ejemplo4 "metodo index" se utiliza para ver el indice de un elemento selecionado.
comidas_favoritas = ["arroz con pollo", "sopa de gallina dura", "pizza", "hamburguesa", "papas fritas con pollo asado"]
actualizado = comidas_favoritas.index("pizza")
print(actualizado)