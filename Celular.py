class Celular:
    def __init__(self, marca, duracion):
        self.marca = marca
        self.duracion = duracion

    def sonar(self):
        print("{self.marca} esta sonando")

    def romper(self):
        print("{self.marca} esta rompiendose")

    def __str__(self):
        return "la marca del celular es {self.marca} y su duracion es {self.duracion}"    