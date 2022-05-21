#HTTP y Rest
from turtle import home
import requests, json
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1') #pido primera prenda de prendas
print(pedido) 
'''<Response [200]>'''
print(pedido.json())
'''devuelve un estilo de diccionario python:{'id': 1, 'tipo': 'pantalon', 'talle': 35}'''
pedido2 = requests.get('https://macowins-server.herokuapp.com/prendas')
print(pedido2.json())
'''[{'id': 1, 'tipo': 'pantalon', 'talle': 35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36}, {'id': 3, 'tipo': 'pantalon',
 'talle': 37}, {'id': 4, 'tipo': 'pantalon', 'talle': 38}, {'id': 5, 'tipo': 'pantalon', 'talle': 39}, {'id': 6, 'tipo': 
 'pantalon', 'talle': 40}, {'id': 7, 'tipo': 'pantalon', 'talle': 41}, {'id': 8, 'tipo': 'pantalon', 'talle': 42}, {'id':
  9, 'tipo': 'pantalon', 'talle': 43}, {'id': 10, 'tipo': 'pantalon', 'talle': 44}, {'id': 11, 'tipo': 'remera', 'talle':
   'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, {'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 
   'remera', 'talle': 'L'}, {'id': 15, 'tipo': 'remera', 'talle': 'XL'}, {'id': 16, 'tipo': 'saco', 'talle': 'XS'}, 
   {'id': 17, 'tipo': 'saco', 'talle': 'S'}, {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, 
   {'id': 19, 'tipo': 'saco', 'talle': 'L'}, {'id': 20, 'tipo': 'saco', 'talle': 'XL'}]'''
#devuelve una lista de diccionarios de todas las prendas

print(len(pedido2.json()))
'''20'''

#saber si hay un valor 400
pedido3=requests.get('https://macowins-server.herokuapp.com/prendas/400')
print(pedido3)
'''<Response [404]> : status'''

print(pedido.headers)
'''{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1',
 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '50', 
 'Etag': 'W/"32-i8e+gZ5GUBVXp/2hTq5pj1i9+f8"', 'Vary': 'Accept-Encoding', 
 'Date': 'Mon, 09 May 2022 14:45:05 GMT', 'Via': '1.1 vegur'}'''

print(pedido3.status_code)
'''404'''
print(pedido.status_code)
'''200'''

#Desafio IV
desafioIV=requests.get('https://macowins-server.herokuapp.com/prindas/1')
# print(desafioIV)
# print(desafioIV.json())
'''<Response [404]>'''

print(pedido.content)
'''b'{\n  "id": 1,\n  "tipo": "pantalon",\n  "talle": 35\n}'''

#DesafioVI
pedido4=requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
print(pedido4.json())
'''[{'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 
{'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'},
 {'id': 15, 'tipo': 'remera', 'talle': 'XL'}]'''

#desafioVII
pedido5=requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&taalle=XS')
print(pedido5.json())
'''[{'id': 11, 'tipo': 'remera', 'talle': 'XS'}, {'id': 12, 'tipo': 'remera', 'talle': 'S'}, 
{'id': 13, 'tipo': 'remera', 'talle': 'M'}, {'id': 14, 'tipo': 'remera', 'talle': 'L'}, 
{'id': 15, 'tipo': 'remera', 'talle': 'XL'}]'''


#DESAFIO VIII
'''la URI de cerebral significa los recuerdos del día de hoy sobre el tema http. 
Usa el protocolo cerebro, hasta ahora el protocolo que usabamos era http. 
El string tutoriales://http/introductorio#7 es una URI'''

#Resolucion de errores
'''timeout=5 sirve para que trasncurran 5 segundos de no encontrar la página para que lanze un error'''

# import os
# hostname = "google.com"
# response = os.system("ping -c 1 " + hostname)
#Acceso denegado. La opción -c requiere privilegios administrativos.

#Desafio IX

#6. Cabeceras
'''el content-type es application/json; charset=utf-8. Esto es porque el link esta usando parametros para armar listas de
lo que contienen los links'''
# linkPropio: https://macowins-server.herokuapp.com/posts/home

#Desafio XI

#8
'''Los métodos HTTP permiten comunicar al servidor lo que se quiere realizar con un resource bajo una URL. Los más
utilizados siendo: POST, GET, PUT, DELETE y HEAD.'''
'''Get se utilizaba para obtener información de un URL al aplicar un parametro. El delete elimina un recurso
especifico'''

#9
data = {'id': 21}
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
print(r)
'''devuelve el codigo 201, el cual significa created'''

data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=data)
'''data sirve para introducir cual será el nuevo recurso.
No creó el contenido que queríamos porque no introducimos en data que el id de la nueva prenda sería 22'''

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)
print(r.status_code)
requests.get('https://macowins-server.herokuapp.com/prendas').json()

# requests.delete('https://macowins-server.herokuapp.com/prendas', )
xxx=requests.get('https://macowins-server.herokuapp.com/prendas/')
print(xxx.json())


#desafio XV
'''Github, infobae, UNQ y ucema utilizan rutas REST'''
#desafio XVI
''''''
