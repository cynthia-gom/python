# Práctica 2
#Como te habrás dado cuenta, al ver el index de posts, y leer los datos, nos damos cuenta que el ID de los posts es incremental.
#Es decir, el primer post tiene el ID de 1, el segundo de 2 y así consecutivamente hasta el 100.
#Escribe un iterador (for loop) que haga interpolación o concatenación de strings por la totalidad de los posts (son 100 posts).
#Debes concatenar el URL de index más los números del 1 al 100 y haz un request para cada uno, e imprime el título del post.

import requests
import json

URL = "https://jsonplaceholder.typicode.com/posts/"

request_nuevo = requests.get(URL)

#print(request_nuevo.text)
#print(type(request_nuevo.text))

parsed = json.loads(request_nuevo.text)
#print(parsed)
#print(type(parsed))



for elemento in parsed:
    a = elemento["id"]
    URLpost = URL + str(a)
    print(URLpost, elemento["title"])
