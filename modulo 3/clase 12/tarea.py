 # crear una lista en la cual se muestre el primer lugar el segundo lugar y el tercer lugar de los competidoress de las olimpiadas en nuestro deporte favorito.

print("ganadores en atletismos de las olimpiadas del 2024")

ganadores = ["Markus rooth", "Leo Neouebauer", "Lindon Victor"]

for k, ganador in enumerate(ganadores, start=1):
    print(f"{k}: {ganador}")