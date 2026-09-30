"""Point de départ : un script d'exploration « façon J2 ».

Il affiche des choses. Il ne dit jamais si c'est correct.
Le J4 commence ici : on le transforme en tests.
"""
import requests

BASE_URL = "http://localhost:8000"

response = requests.get(f"{BASE_URL}/api/events", timeout=5) 
# timeout a 5 para tener acceso al cntenido de la reponse (contiene status, haders,etc)
print(response.status_code)
print(response.headers.get("content-type"))
# aqui s eve el tipo de body mais il faut pasarlo a json/ dict python

# rechercher avec un mot cle on filtre eso haciamos con query params eso permite filtrar elementos pero aqui hay parametro de ruta... events/1 es para puntear

for event in response.json():
    print(event["id"], event["title"], "-", event["city"], "-", event["status"])

detail = requests.get(f"{BASE_URL}/api/events/{response.json()[0]['id']}", timeout=5)
print(detail.status_code)
print(detail.json())
