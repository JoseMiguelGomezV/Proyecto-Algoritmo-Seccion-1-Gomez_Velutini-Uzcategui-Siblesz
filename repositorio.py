import requests

def obtener_departamentos():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data["departments"]
    except:
        return None

def obtener_todos_los_objetos():
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data["objectIDs"]
    except:
        return None

def obtener_objeto_por_id(obj_id):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data
    except:
        return None

def buscar_objetos(query):
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}"
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return data["objectIDs"]
    except:
        return None


def obtener_todas_nacionalidades():
    return "https://drive.google.com/file/d/1tJEU6_VEeO6xFH8fssSfkw4M8MaN6U5A/view?usp=sharing"

