class pelota:
    def __init__(self, marca, ancho):
        self.marca = marca
        self.ancho = ancho

    def sonar(self):
        print("{self.marca} esta sonando")

    def romper(self):
        print("{self.marca} esta rompiendose")

    def __str__(self):
        return "la marca del celular es {self.marca} y su duracion es {self.ancho}"  