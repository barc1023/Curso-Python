 
 # ejemplo del video
 # ejemplo args
 
 
def unafuncion(*args):
    for i in args:
       print(i)
    
unafuncion("hola", "1", "hello")

def total(*args):
    total = sum(args)
    print(total)
    
total(300, 500, 433, 3454)

 # ejemplo kwargs
 
def empleado(**kwargs):
# keyword arguments
    for key, value in kwargs.items():
        print(f"{key} : {value}")

empleado(nombre="luis", puesto="programador", lenguaje= "java")        