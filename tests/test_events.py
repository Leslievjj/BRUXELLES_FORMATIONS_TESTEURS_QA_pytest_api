import requests

BASE_URL= "http://localhost:8000"
TIMEOUT=5

# verifier que el status est bien publie----

def test_event():
    response = requests.get(f"{BASE_URL}/api/events", timeout=TIMEOUT)
    # requete fait 

    assert response.status_code == 200, response.text
    # affiche tous les details avec reponse text pour avoir tout le
    # 

    assert response.headers["content-type"].startswith("application/json")

    # verifie si la liste est vide
    assert len(response.json())>0

def test_event_published():
    response= requests.get(f"{BASE_URL}/api/events", timeout=TIMEOUT)
    events = response.json()  
    for e in events:
        assert e["status"] =="published"

def test_events_structure():
    response = requests.get(f"{BASE_URL}/api/events", timeout=TIMEOUT)
    # requete fait 

    assert response.status_code == 200, response.text
    events = response.json()  
    # body es un dict json il faut que passe a python

    for event in events:
        assert "id" in event
        assert type(event["id"]) == int
        assert "title" in event
        assert type(event["title"]) == str
        assert "description" in event
        assert type(event["description"]) == str
        assert "city" in event
        assert "venue" in event
        assert "starts_at" in event
        assert "capacity" in event
        assert "status" in event
        assert "cover_color" in event

def test_events_casse():
    response = requests.get(f"{BASE_URL}/api/eventsss", timeout=TIMEOUT)
    # requete fait 

    events = response.json()

    for event in events:
        assert "id" in event
       
