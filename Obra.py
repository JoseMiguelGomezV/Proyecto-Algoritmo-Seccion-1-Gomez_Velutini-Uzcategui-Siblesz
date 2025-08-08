class Obra:
    def __init__(self, id_obra, titulo, artista, clasificacion, fecha_creacion, imagen, departamento):
        self.id_obra = id_obra
        self.titulo = titulo
        self.artista = artista  
        self.clasificacion = clasificacion
        self.fecha_creacion = fecha_creacion
        self.imagen = imagen
        self.departamento = departamento

    def show_resumen(self):
        """Muestra una versión corta de la información de la obra, para listas."""
        print(f"ID: {self.id_obra}, Titulo: {self.titulo}, Autor: {self.artista.nombre}")

    def show_detalles(self):
        """Muestra toda la información detallada de la obra."""
        print(f"\nTítulo: {self.titulo}")
        self.artista.show_detalles()
        print(f"Tipo: {self.clasificacion}")
        print(f"Año de creación: {self.fecha_creacion}")
        print(f"Departamento: {self.departamento.nombre}")
