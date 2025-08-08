
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
    return "https://drive.google.com/uc?export=download&id=1tJEU6_VEeO6xFH8fssSfkw4M8MaN6U5A"

def obtener_contenido_nacionalidades(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        contenido = r.text
        """
        El codigo que se muestra a continuacion procesa el texto descargado y devuelve una lista de nacionalidades,
        al dividir el texto en líneas usando splitlines(), luego elimina líneas vacías y espacios innecesarios con strip()
        y finalmente retorna una lista donde cada elemento es una nacionalidad.
        """
        return [line.strip() for line in contenido.splitlines() if line.strip()]

    except:
        return []

