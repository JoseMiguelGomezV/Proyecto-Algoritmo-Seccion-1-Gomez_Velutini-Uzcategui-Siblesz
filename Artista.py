class Artista:
    def __init__(self, nombre, nacionalidad, nacimiento, muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nacimiento = nacimiento
        self.muerte = muerte

    def show_detalles(self):
        print(f"Nombre del Artista: {self.nombre}")
        print(f"Nacionalidad del artista: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.nacimiento}")
        print(f"Fecha de muerte: {self.muerte}")
