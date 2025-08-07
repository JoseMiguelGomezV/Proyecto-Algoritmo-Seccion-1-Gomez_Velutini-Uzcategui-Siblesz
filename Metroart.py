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

  print("Cargando nacionalidades...")
  url_nacionalidades = get_url_nacionalidades()
  self.nacionalidades = obtener_contenido_nacionalidades(url_nacionalidades)
  print("Sistema listo para usar")

  while True:
    print("\nOpciones:")
    print("1. Buscar obras por departamento")
    print("2. Buscar obras por nacionalidad del autor")
    print("3. Buscar obras por nombre del autor")
    print("4. Mostrar detalles de una obra por ID")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
      print("Lista de departamentos disponibles:")
      for depto in self.departamentos:
          print(f"{depto.id_departamento}: {depto.nombre}")
      dept_id = input("Ingrese el ID del departamento: ")
      depto_nombre = None
      for d in self.departamentos:
          if str(d.id_departamento) == dept_id:
              depto_nombre = d.nombre
              break
      if not depto_nombre:
          print("ID de departamento no valido")
          return
      ids = buscar_objetos(depto_nombre)
      if not ids:
          print("No se encontraron obras para ese departamento")
          return
      cargadas = 0
      while cargadas < len(ids):
          print("\nMostrando 20 obras:")
          for i in range(cargadas, min(cargadas + 20, len(ids))):
              datos = obtener_objeto_por_id(ids[i])
              if datos:
                  obra = self._crear_objeto_obra_desde_datos(datos)
                  print("ID:", obra.id_obra, ", Titulo:", obra.titulo, ", Autor:", obra.artista.nombre)
          cargadas += 20
          if cargadas >= len(ids):
              print("\nNo hay mas obras que mostrar para este departamento")
              break
          mas = input("¿Desea ver otras 20 obras? (s/n): ")
          if mas.lower() != 's':
              break
      input("Presiona Enter para volver al menu...")

    elif opcion == "2":
      if self.nacionalidades:
        print("Lista de nacionalidades: ")
        for n in self.nacionalidades:
          print(n)
        
      






      elif opcion == "3":
                nombre = input("Ingrese el nombre del autor: ")
                ids = buscar_objetos(nombre)
                if not ids:
                    print("No se encontraron obras para ese autor.")
                    return
                cargadas = 0
                while cargadas < len(ids):
                    print("\nMostrando 5 obras:")
                    mostradas = 0
                    for i in range(cargadas, len(ids)):
                        datos = obtener_objeto_por_id(ids[i])
                        if datos and nombre.lower() in datos.get('artistDisplayName','').lower():
                            obra = self._crear_objeto_obra_desde_datos(datos)
                            print("ID:", obra.id_obra, ", Título:", obra.titulo, ", Autor:", obra.artista.nombre)
                            mostradas += 1
                        if mostradas == 5:
                            break
                    if mostradas == 0:
                        print("Ya se mostraron todas las obras disponibles.")
                        break
                    cargadas += mostradas
                    if cargadas >= len(ids):
                        print("\nNo hay más obras que mostrar para este autor.")
                        print("Ya se mostraron todas las obras disponibles.")
                        break
                    mas = input("¿Desea ver otras 5 obras? (s/n): ")
                    if mas.lower() != 's':
                        break
                input("Presiona Enter para volver al menú...")









      
