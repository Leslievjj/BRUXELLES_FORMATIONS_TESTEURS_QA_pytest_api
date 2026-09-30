import requests



BASE_URL= "http://localhost:8000"
TIMEOUT=5

def test_health_repond_ok():
    response = requests.get(f"{BASE_URL}/api/health", timeout=TIMEOUT)
    # requete fait 

    assert response.status_code == 200, response.text
    # affiche tous les details avec reponse text pour avoir tout le
    #  message de fail cuando por ejemplo pongo un api incorrecto "healtgfgfg"

    assert response.headers["content-type"].startswith("application/json")


    assert response.json()["status"] == "ok"

    # json schema valide la structure
    #  ici on tste avec python test api:test integration maintenat on teste l'api avant on testait
    #  functions

