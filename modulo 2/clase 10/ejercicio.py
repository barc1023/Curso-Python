 #el clima
print("bienvenido a nuestro programa 'EL CLIMA'")
clima = input("cuentenos, ¿que tal el dia de hoy? 'SOLEADO' 'NUBLADO' 'LLUVIOSO' ")

if clima  == "soleado" :
    print("¡QUE CALOR! viste ligero, toma una sombrilla, usa mucho protector solar y mantente hidratado.")

elif clima == "lluvioso":
    print("¡HORA DE RELAJARSE! prepara chocolate caliente y disfruta leyendo un libro.")

elif clima == "nublado": 
    print("¿LLOVERA? lleva contigo un paraguas, si te mojas te puedes resfriar.")

else:
    print("los datos ingresados no son correctos, porfavor pruebe de nuevo.")