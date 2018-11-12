#Práctica 1
#Construye un iterador (for Loop) que consuma el índice de los posts https://jsonplaceholder.typicode.com/posts/ e imprima todos los títulos de los posts.
#Por favor nota la estructura de datos: El índice es una lista de diccionarios, es decir, empieza con corchetes. El json.loads() será capaz de leerlo, pero
#para imprimir los datos debes tener esto en cuenta

import requests
import json

request_nuevo = requests.get("https://jsonplaceholder.typicode.com/posts/")

#print(request_nuevo.text)
#print(type(request_nuevo.text))

parsed = json.loads(request_nuevo.text)
#print(parsed)
#print(type(parsed))

#print(parsed["userId"])
#print(parsed["id"])
#print(parsed["title"])
#print(parsed["body"])

#print(len(parsed))

#print(parsed[2]["title"]) #ejemplo

for elemento in parsed:
    print(elemento["title"])
