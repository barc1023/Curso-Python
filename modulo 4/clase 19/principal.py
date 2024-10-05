
import atencion_al_cliente

print("solicitudes comunes que presenta nuestro departamento: quejas, solicitudes de afiliacion, sujerencias de nuestros clientes")

print(atencion_al_cliente.quejas)
print(atencion_al_cliente.afilacion)
print(atencion_al_cliente.sujerencias)

from atencion_al_cliente import usuarios

for i, l in enumerate(usuarios):
    print(l)
    
