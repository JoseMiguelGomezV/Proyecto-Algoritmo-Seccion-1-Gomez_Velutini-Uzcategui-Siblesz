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
      else:
        print("No se pudo obtener la lista de nacionalidades.")
        nacionalidades_lower = [n.lower() for n in self.nacionalidades]

        nacionalidad = input("Ingrese la nacionalidad: ")
        if nacionalidad.lower() not in nacionalidades_lower:
                    print("Nacionalidad no válida.")
                    return
        ids = buscar_objetos(nacionalidad)
        if not ids:
                    print("No hay obras para esta nacionalidad")
                    return
        cargadas = 0
        while cargadas < len(ids):
                    print("\nMostrando 20 obras:")
                    mostradas = 0
                    for i in range(cargadas, len(ids)):
                        datos = obtener_objeto_por_id(ids[i])
                        if datos and datos.get('artistNationality','').lower() == nacionalidad.lower():
                            obra = self._crear_objeto_obra_desde_datos(datos)
                            print("ID:", obra.id_obra, ", Título:", obra.titulo, ", Autor:", obra.artista.nombre)
                            mostradas += 1
                        if mostradas == 20:
                            break
                    cargadas += mostradas
                    if cargadas >= len(ids):
                        print("\nNo hay más obras que mostrar para esta nacionalidad.")
                        break
                    mas = input("¿Desea ver otras 20 obras? (s/n): ")
                    if mas.lower() != 's':
                        break
        input("Presiona Enter para volver al menú...")
      

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


    elif opcion == "4":
                obra_id = input("Ingrese el ID de la obra: ")
                obra = self._obtener_obra_por_id_con_cache(int(obra_id))

                if obra:
                    print(f"\nTítulo: {obra.titulo}")
                    print(f"Nombre del Artista: {obra.artista.nombre}")
                    print(f"Nacionalidad del artista: {obra.artista.nacionalidad}")
                    print(f"Fecha de nacimiento: {obra.artista.nacimiento}")
                    print(f"Fecha de muerte: {obra.artista.muerte}")
                    print(f"Tipo: {obra.clasificacion}")
                    print(f"Año de creación: {obra.fecha_creacion}")
                    print(f"Departamento: {obra.departamento.nombre}")

                    if obra.imagen:
                        ver_img = input("\n¿Deseas ver la imagen de la obra? (s/n): ").lower()
                        if ver_img == 's':
                            self._guardar_y_mostrar_imagen(obra.imagen, f"obra_{obra.id_obra}")
                    else:
                        print("\nNo hay imagen disponible para esta obra.")
                    input("Presiona Enter para volver al menú...")
                else:
                    print("No se encontró la obra.")
                    input("Presiona Enter para volver al menú...")
                  

   elif opcion == "5":
                print("Saliendo del sistema...")
                break
   else:
                print("Opción no válida.") 
              

   def _obtener_obra_por_id_con_cache(self, id_obra: int) -> Obra:
        """
        Obtiene una obra. Primero busca en el caché, si no la encuentra,
        la pide a la API y la guarda en la caché para el futuro.
        """
        if id_obra in self.obras_cache:
            print("(Obtenido desde la caché)")
            return self.obras_cache[id_obra]
        
        datos_obra = obtener_objeto_por_id(id_obra)
        if datos_obra:
            return self._crear_objeto_obra_desde_datos(datos_obra)
        return None

    
   def _crear_objeto_obra_desde_datos(self, datos: dict) -> Obra:
        """Método auxiliar para crear un objeto con los datos de una obra a partir de un diccionario de datos de la API."""
        artista = Artista(
            nombre=datos.get('artistDisplayName', 'Desconocido'),
            nacionalidad=datos.get('artistNationality', 'Desconocida'),
            nacimiento=datos.get('artistBeginDate', 'N/A'),
            muerte=datos.get('artistEndDate', 'N/A')
        )
        departamento = Departamento(
            id_departamento=datos.get('department', 'N/A'),
            nombre=datos.get('department', 'Desconocido')
        )
        id_obra = datos.get('objectID')
        obra = Obra(
            id_obra=id_obra,
            titulo=datos.get('title', 'Sin Título'),
            artista=artista,
            clasificacion=datos.get('classification', 'No clasificado'),
            fecha_creacion=datos.get('objectDate', 'Desconocida'),
            imagen=datos.get('primaryImageSmall', ''),
            departamento=departamento
        )
        if id_obra:
            self.obras_cache[id_obra] = obra
        return obra


   def _guardar_y_mostrar_imagen(self, url: str, nombre_base_archivo: str):
        """
        Descarga una imagen desde una URL y la guarda en un archivo, optamos por mostrarla.
        """
        print("Descargando imagen...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            content_type = response.headers.get('Content-Type')
            extension = '.png'  
            if content_type:
                if 'image/png' in content_type:
                    extension = '.png'
                elif 'image/jpeg' in content_type:
                    extension = '.jpg'
                elif 'image/svg+xml' in content_type:
                    extension = '.svg'

            nombre_archivo_final = f"{nombre_base_archivo}{extension}"

            with open(nombre_archivo_final, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")

        except requests.exceptions.RequestException as e:
            print(f"Error al hacer el request: {e}")
            return None
        except IOError as e:
            print(f"Error al escribir el archivo: {e}")
            return None

        img = Image.open(nombre_archivo_final)
        img.show()







      
