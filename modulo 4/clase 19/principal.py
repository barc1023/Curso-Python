
import atencion_al_cliente

print("solicitudes comunes que presenta nuestro departamento: quejas, solicitudes de afiliacion, sujerencias de nuestros clientes")

print(atencion_al_cliente.quejas)
print(atencion_al_cliente.afilacion)
print(atencion_al_cliente.sujerencias)

import atencion_al_cliente
from atencion_al_cliente import usuarios

for x in usuarios:
    for n in x:
        print(n, x[n])