
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

def get_url_nacionalidades():
    return "https://drive.google.com/file/d/1tJEU6_VEeO6xFH8fssSfkw4M8MaN6U5A/view?usp=sharing"

def obtener_contenido_nacionalidades(url):
    import requests
    import re
    match = re.search(r"/d/([\w-]+)", url)
    if match:
        file_id = match.group(1)
        raw_url = f"https://drive.google.com/uc?export=download&id={file_id}"
        try:
            r = requests.get(raw_url)
            r.raise_for_status()
            contenido = r.text
            nacionalidades = [line.strip() for line in contenido.splitlines() if line.strip()]
            return nacionalidades
        except:
            return []
    return []

