# crear una funcion que multiplique 4 numeros y llamarla 3 veces

def multiplicar():
    num1 = int(input("ingrese su primer numero  "))
    num2 = int(input("ingrese su segundo numero  "))
    num3 = int(input("ingrese su tercernumero  "))
    num4 = int(input("ingrese su cuarto numero  "))
    
    resultado = num1*num4*num2*num3
    
    print(f"el resultado de la multiplicacio es: {resultado}")   

while True:

    multiplicar()

    respuesta = input("desea continuar? si/no  ")

    if respuesta == "si":
       print("recalculando")
       multiplicar()

    
    elif respuesta == "no":
        print("gracias por usar este programa")
        break
    
    else:
        print("comando equivocado")



  
