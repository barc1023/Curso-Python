 # crear una funcion args que multiplique los numero que le damos

numeros = input("ingrese sus numeros separados por una coma: ").split(",")

numeros = [int(num)for num in numeros]

def multiplicar(*args):
    total = 1
    for i in args:
        total *= i
        print(f"el resultado es: {total}")

multiplicar(*numeros)