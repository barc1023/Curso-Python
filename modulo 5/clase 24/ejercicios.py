
  # crear una funcion lambda y una comun para restar dos parametros
  
  # ejercicio con funcion lambda
  
print(" ingrese dos numeros: *separados por una coma*")
nums = input("numeros: ").split(",")

nums = [int(num) for num in nums]

def resta(*args):
    total = 0
    for i in args:
        total -= i
        print(f" el resultado de la resta es: {total}")
        
resta(*nums)


  # ejercicio con funcion comun

restas = lambda b, s : b - s
print(restas(7, 2))