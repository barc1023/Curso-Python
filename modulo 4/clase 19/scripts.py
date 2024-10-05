
 # los script son sinonimos de modulos (los modulos son cualquier archivo que termine en .py)

import configuraciones

print(configuraciones.base_url)
print(configuraciones.time)
print(configuraciones.usuario)
print(configuraciones.contraseña)


from configuraciones import base_url, time, contraseña, usuario

print(contraseña)