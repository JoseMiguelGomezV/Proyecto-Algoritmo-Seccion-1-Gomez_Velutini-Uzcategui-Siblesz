import requests
from PIL import Image

from repositorio import obtener_departamentos, obtener_objeto_por_id, buscar_objetos, get_url_nacionalidades, obtener_contenido_nacionalidades
from Obra import Obra
from Artista import Artista
from Departamento import Departamento

class MetroArt:
  """
  clase principal que gestiona la interaccion con el catalogo de arte
  """
  RESULT_LIMIT = 20
  PAGE_SIZE = 5

def __init__(self):
  self.departamentos = []
  self.nacionalidades = []
  self.obras_cache = {}

def start(self):
  print("Bienvenido al sistema MetroArt")
  print("Cargando departamentos...")
  deptos_dict = obtener_departamentos()
  if deptos_dict is None:
    print("No se pudieron cargar los departamentos")
    self.departamentos = []
  else:
    self.departamentos = [Departamento(d['departmentId'], d['displayName']) for d in deptos_dict]
    print(f"Departamentos encontrados: {len(self.departamentos)}")
    
