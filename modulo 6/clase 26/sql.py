   # bade de datos SQL : structure querty lenguage
   # ddl : data definition lenguage  (como definimos la inforacion)
   # dml : data manipulation lenguage
   # dcl : data control lenguage
   # crud : create, reed, update, delete 
   
'''
base de datos : son los sistemas que almacenan, organizan y gestinan la informacion 

              toda base de datos pose:
                                         columnas y tablas : las columnas son campos y las filas son los registros
                                               
bd relacionales : la informacion en su interior estan relacionados
usan una clave primaria para sus relaciones, la clave primaria es un campo importante,

 VENTAJAS 
1. integridad y consistencia
2. son ideales para datos estructurales
3. escaneabilidad
 
  DESVENTAJAS 
1. no son ideales para datos no structurales
2.

  EJEMPLOS 
1. mysql
2. postgresql
3. oracle
4. microsrt sql server

bd no relacionales : no estan basadas en tablas, son ideales cuando no se nececitan datos estructurados, su informacion esta organizada en documentos similares
a JSON o XML. puede almacenar datos clave-valor. puede presentar columnas
son ideales para sistemas que nececitan consistencia

 VENTAJAS
1. optimizar grandes volumenes de datos (priorizan la velocidad)
2. flexible
3. disponibilidad
4. son facilmente escaneables

 DESVENTAJAS
1. no son adecuados para consultas complejas
2. son menos concistentes 
  
  EJEMPLOS
  
1. mongosdb
2. redis
3. dynamodb
4. cassandra
5. hbase
6. neo4j
'''