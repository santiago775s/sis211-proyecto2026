class Socio:
    def __init__(self, id_socio, nombre):
        self.id_socio = id_socio
        self.nombre = nombre
        self.historial = []

    def registrar_prestamo(self, isbn):
        self.historial.append(isbn)

    def obtener_historial(self):
        return list(self.historial)

    def __str__(self):
        return f"[{self.id_socio}] {self.nombre}"
